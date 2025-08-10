import pandas as pd
import numpy as np
from scipy.fft import fft, fftfreq, fftshift
from scipy.signal import find_peaks
from scipy.integrate import simpson
import os

# Constants
FREQ = 476e6  # Frequency in MHz
C = 2.998e8  # Speed of light in m/s
""" You can set the file path for saving the n_parallel and directivity data according to your personal computer."""
save_directory = "D:\\eunjijung\\mail_for_Empire" 
PROCESSING_RANGE = (-15, 15)  # Processing range: [-15, 15]

def load_data():
    """Load the directly specified txt file, with doubled backslashes in the path."""
    file_path = "D:\\eunjijung\\mail_for_Empire\\KW_N_parallel_data\\test.txt"  # Directly specified txt file path
    return pd.read_csv(file_path, comment='#', delimiter='\t', header=None, names=['Length_mm', 'Re_V/m', 'Im_V/m'])

def process_signal(data, freq=FREQ, c=C):
    """Process the signal and return FFT result and spectrum."""
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
    """Calculate directivity based on the spectrum in the specified range."""
    mask_full_range = (n_nn >= PROCESSING_RANGE[0]) & (n_nn <= PROCESSING_RANGE[1])
    mask_partial_range = (n_nn >= 2) & (n_nn <= 4)
    integral_full_range = simpson(y=spectrum[mask_full_range], x=n_nn[mask_full_range])
    integral_partial_range = simpson(y=spectrum[mask_partial_range], x=n_nn[mask_partial_range])
    return (integral_partial_range / integral_full_range) * 100

def save_data(n_nn, spectrum, directivity):
    """Save n_parallel and directivity to separate text files."""
    os.makedirs(save_directory, exist_ok=True)  # Ensure the directory exists

    # Find the n_nn value where the power spectrum is 1 (maximum)
    max_indices = np.where(spectrum == 1)[0]
    peak_n_nn = n_nn[max_indices]

    # Save n_parallel (n_nn values where power spectrum is 1)
    n_parallel_path = os.path.join(save_directory, "n_parallel.txt")
    with open(n_parallel_path, 'w') as file:
        for n in peak_n_nn:
            file.write(f"{n:.6f}\n")
    print(f"n_parallel data saved to {n_parallel_path}")

    # Save directivity
    directivity_path = os.path.join(save_directory, "directivity.txt")
    with open(directivity_path, 'w') as file:
        file.write(f"{directivity:.2f}\n")
    print(f"Directivity data saved to {directivity_path}")

def main():
    """Main function to process signal data and save results."""
    data = load_data()  # Load a specific file directly
    n_nn, spectrum = process_signal(data)
    directivity = calculate_directivity(n_nn, spectrum)
    save_data(n_nn, spectrum, directivity)

if __name__ == "__main__":
    main()
