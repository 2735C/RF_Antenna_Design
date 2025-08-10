# Updated 2024-0315 HHWI
# CST 2024 sp2 version
# Imported data format for singlecase only
# Default, Power and Normalized (0, 1)
# Default Plot range, -15 to 15
# Stored directory should be changed before run, Default is Z:\\data_save

import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.integrate import simpson
import os

# Constants
FREQ = 476e6  # Frequency in MHz
C = 2.998e8  # Speed of light in m/s
save_directory = "\\tsclient\\D\\N_parallel"
PROCESSING_RANGE = (-15, 15)  # Processing range: [-15, 15]

def load_data():
    """Load data from a specific file without prompting the user."""
    file_path = "\\\\tsclient\\D\\N_parallel\\output.txt"  # 직접 지정한 파일 경로
    return pd.read_csv(file_path, comment='#', delimiter='\t', header=None, names=['Length_mm', 'Re_V/m', 'Im_V/m'])

def process_signal(data, freq=FREQ, c=C):
    """Process the signal and return FFT result and directivity."""
    complex_signal = data['Re_V/m'].to_numpy() + 1j * data['Im_V/m'].to_numpy()
    N = len(complex_signal)
    sample_spacing = (data['Length_mm'].iloc[-1] - data['Length_mm'].iloc[0]) / (N - 1) * 1e-3
    N_nn = 50 * 2**np.ceil(np.log2(N)).astype(int)

    fft_result_nn = fft(complex_signal, n=N_nn)
    fft_result_shifted_nn = fftshift(fft_result_nn)
    fft_result_shifted_magnitude_nn = np.abs(fft_result_shifted_nn)
    fft_result_shifted_magnitude_normalized_nn = fft_result_shifted_magnitude_nn / np.max(fft_result_shifted_magnitude_nn)
    spectrum = fft_result_shifted_magnitude_normalized_nn ** 2

    frequencies_nn = fftshift(fftfreq(N_nn, d=sample_spacing))
    n_nn = frequencies_nn * c / freq

    return n_nn, spectrum

def calculate_directivity(n_nn, spectrum):
    mask_full_range = (n_nn >= PROCESSING_RANGE[0]) & (n_nn <= PROCESSING_RANGE[1])
    mask_partial_range = (n_nn >= 2) & (n_nn <= 4)
    integral_full_range = simpson(y=spectrum[mask_full_range], x=n_nn[mask_full_range])
    integral_partial_range = simpson(y=spectrum[mask_partial_range], x=n_nn[mask_partial_range])
    return (integral_partial_range / integral_full_range) * 100

def plot_spectrum(n_nn, power_spectrum, directivity):
    """Plot the spectrum, annotate directivity and the top two peaks."""
    plt.figure(figsize=(10, 6), dpi=200)
    plt.plot(n_nn, power_spectrum, label='Power Spectrum')
    peaks, _ = find_peaks(power_spectrum, height=0)    # Find peaks in the power spectrum
    valid_peaks = (n_nn[peaks] >= PROCESSING_RANGE[0]) & (n_nn[peaks] <= PROCESSING_RANGE[1])   # Filter peaks to those within the plot range
    peak_freqs = n_nn[peaks][valid_peaks]
    peak_powers = power_spectrum[peaks][valid_peaks]

    # Sort peaks by power and select the top two
    sorted_indices = np.argsort(peak_powers)[::-1][:2]  # Change here to adjust the number of top peaks
    top_peaks_freqs = peak_freqs[sorted_indices]
    top_peaks_powers = peak_powers[sorted_indices]

    # Annotate the top two peaks on the plot
    for i, (freq, power) in enumerate(zip(top_peaks_freqs, top_peaks_powers)):
        plt.annotate(f'Peak {i + 1}: ({freq:.2f}, {power:.2f})', (freq, power),
                     textcoords="offset points", xytext=(5, -12), ha='center', color='red')
    plt.text(-9, max(power_spectrum) * 0.9, f'Directivity: {directivity:.2f}%', color='blue')     # Directivity annotation

    plt.title('Parallel Refractive Index Power Spectrum')
    plt.xlabel('Refractive Index (n)')
    plt.ylabel('Power Spectrum')
    plt.xlim([PROCESSING_RANGE[0], PROCESSING_RANGE[1]])
    plt.ylim([0, 1])
    plt.grid(True)
    plt.legend()
    plt.show()

def save_data(n_nn, spectrum):
    os.makedirs(save_directory, exist_ok=True)  # Ensure the directory exists
    filter_mask = (n_nn >= PROCESSING_RANGE[0]) & (n_nn <= PROCESSING_RANGE[1])   # Filter the data for the range -10 to 10
    n_nn_filtered = n_nn[filter_mask]
    spectrum_filtered = spectrum[filter_mask]
    fft_data_path = os.path.join(save_directory, "Power_Spectrum.csv")
    with open(fft_data_path, 'w', newline='') as file:  # Ensures no extra newline characters
        pd.DataFrame({'n_nn': n_nn_filtered, 'spectrum': spectrum_filtered}).to_csv(file, index=False)
    print(f"FFT spectrum data saved to {fft_data_path}")

def main():
    """Main function to process signal data and plot results."""
    data = load_data()  # 바로 특정 파일을 로드
    n_nn, spectrum = process_signal(data)
    directivity = calculate_directivity(n_nn, spectrum)
    print(f"Directivity(%): {directivity:.2f}%")
    plot_spectrum(n_nn, spectrum, directivity)
    save_data(n_nn, spectrum)

if __name__ == "__main__":
    main()
