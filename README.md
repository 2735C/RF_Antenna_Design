# :star: TEAM: 캡스톤 설계 2팀  

## 🙋‍♂️팀원

| **정은지** | **유동옥** | **김태민** |
|:----------:|:----------:|:----------:|
| Team Leader | Antenna Performance <br> Improvement Developer | Antenna Performance <br> Improvement Developer |
| [<img src="/History/img/profile1.webp" width="250" height="250"><br />@mail](mailto:eunjijung1107@gmail.com) | [<img src="/History/img/profile2.png" width="250" height="250"><br />@mail](mailto:avanet9479@kw.ac.kr) | [<img src="/History/img/profile3.png" width="250" height="250"><br />@mail](mailto:steve3588@naver.com) |




## 🖊️Role

### :wolf: 정은지
**Team leader**<br>
**[HW]**
- Helical Antenna characteristic analysis <br>

**[SW]** 
- Integration of _Parallel Refractive Index_ as a custom CST optimization variable
- Implementation of MATLAB-controlled CST simulations for advanced optimization



### :tiger: 유동옥
**[HW]**
- Combline Antenna characteristic analysis
- Performance improvement of Combline Antenna model


###	:dragon: 김태민
**[HW]**
- Helical Antenna characteristic analysis
- Performance improvement of Helical Antenna model




## 🚀프로젝트 개요
**핵융합 플라즈마 가열 및 전류 구동용 RF 안테나 특성 분석 및 성능 향상 모델 도출** <br>
[ Analysis of RF antenna characteristics and development of a performance improvement model for nuclear fusion plasma heating and current driving. ]<br>


### 🧐연구의 필요성 및 기대 효과

**1. 핵융합 에너지 연구의 시장성**

- 최근 AI와 데이터 센터의 성장으로 전력 공급의 중요성이 떠오르면서 그 대안으로 핵융합 기술이 부각되고 있다.<br>중국은 대규모 자본을 투입하여 핵융합 기술에서 미국을 위협할 수준이며, 이에 대응해 미국은 민간 자본과 정부의 지원을 바탕으로 한 핵융합 스타트업 붐으로 상업적 핵융합 가능성을 제시하며 연구개발을 가속화하고 있다.<br> 이와 같이 현재 세계 각국에서 안정적인 에너지 공급을 위한 기술적 우위를 확보하기 위해 노력하고 있다. 

- 우리나라 정부 역시 2050 Net-Zero 달성을 표방하며 핵융합에너지 상용화를 위한 국제핵융합실험로(ITER) 공동개발사업과 핵융합선도기술개발사업을 지원하고 있다. <br>24년 7월 정부가 발표한 ｢핵융합에너지 실현 가속화 전략｣에서 ‘핵융합 기술혁신’을 내세운 점에서 핵융합 전력 생산 위한 핵심기술 개발의 중요성을 알 수 있다. 


**2. 핵융합 안테나의 필요성**

- 핵융합 연구에서 안테나는 플라즈마를 효과적으로 가열하고 안정적으로 제어하는 데 중요한 역할을 한다. <br> 플라즈마 가열 안테나는 플라즈마 온도를 핵융합 조건(수백만에서 수억 도)까지 올리기 위해 고주파(RF) 에너지를 전달하는 용도로 사용되며, 대표적으로 ICRH(Ion Cyclotron Resonant Heating)와 ECRH(Electron Cyclotron Resonant Heating) 방식이 있다.

- 전류 구동 안테나는 플라즈마 내부에 전류를 유도하여 자기장 구성을 제어하며, 이를 통해 플라즈마 안정성과 에너지 효율성을 향상시킨다. <br> 이에 해당하는 기술로는 LHCD(Lower Hybrid Current Drive), ECCD(Electron Cyclotron Current Drive), 그리고 최근 연구가 활발한 HCD(Helicon Current Drive) 등이 있다.<br>  ICCD(Ion Cyclotron Current Drive) 역시 ICRH의 전류 구동 응용으로 볼 수 있다. <br> 이 외에도 플라즈마 상태 분석을 위한 다양한 안테나 기술이 활용된다.

- MW(메가와트)급 고출력 RF 시스템은 핵융합 플라즈마 가열과 안정적 제어를 위해 필수적이다.<br>핵융합 반응을 위해서는 플라즈마 온도를 충분히 높여야 하며, ICRH, ECRH, LHCD 등의 RF 시스템을 통해 고출력 에너지를 전달한다. <br>또한, MW급 RF 전력은 플라즈마 내부의 난류(turbulence)나 불안정성(instability)을 억제하는 데도 활용되어 안정적인 플라즈마 유지에 기여한다. <br>따라서 MW급 전력을 안정적으로 처리할 수 있는 안테나 기술 개발이 매우 중요하다.

- 기존의 자기 유도 전류 구동 방식은 주로 펄스형 운전에 제한되는 반면, RF 전류 구동 방식은 연속 운전(steady-state operation)이 가능하여 차세대 핵융합로의 지속 가능한 운영을 목표로 한다. <br> 특히 헬리콘 전파를 이용하는 HCD는 400~500 MHz 대역에서 높은 효율로 전류를 구동하는 기술로, LHCD를 보완하거나 대체할 가능성으로 주목받고 있다.


**3. 연구 목적**

- 본 연구에서는 “핵융합 플라즈마 가열 및 전류 구동용 RF 안테나”라는 주제로 Parallel Refractive Index 개념을 바탕으로 하여 CST Simulation 기반으로 Combline Antenna, Helical Antenna를 활용해서 기존 안테나의 성능을 분석 및 성능 향상을 목표로 하여 설계를 하고자 한다.

**4. 기대 효과**

- 두 가지 형태(Combline, Helical)의 핵융합 발전을 위한 고효율 플라즈마 가열 안테나 설계를 진행하며 어느 유형의 안테나가 플라즈마 가열 안테나에 더 적합한지 비교 분석이 가능할 것이라 기대된다. <br>또한, 플라즈마 가열이라는 새로운 분야에서의 안테나의 활용도 및 기술의 성장을 예측할 수 있다.

## 🗓️개발 일정 2024.07.26 ~ 2024.12.16

### <개발 순서>

1. 관련 논문 분석                
2. 기존 안테나 특성 분석
[Reconstruction of the existing antenna model in CST and analysis of parameter-dependent characteristics]
3. Parallel Refractive Index 계산을 위한 파이썬 코드 분석            
4. Combline/Helical Antenna model 성능 개선
5. CST 내장 변수에 없던 Parallel Refractive Index를 최적화 변수로 구현 및 자동화      
6. MATLAB에서 CST 시뮬레이션을 원격 제어하여 다양한 최적화 알고리즘 적용 환경 마련   

## 개발 과정
> 더 많은 내용을 확인하고 싶으면 --> [[보고서]](/Project/오성욱교수님_캡스톤설계2_2팀_최종%20보고서.pdf)

**(1) Helical Antenna characteristic analysis**

**□ Helical Antenna 설계**

**1. 목표설정**

- S11 < -15dB, S21 >-1dB로 최소한의 반사와 최대의 전송이 이루어지게 S-parameter값 설정
- nll(Parallel Refractive Index) = 3
- 기존 KFE Reference 자료보다 더 많은 turn수로 높은 Directivity값을 얻음


**2. 설계 초기 과정**
**[KFE reference (step2)]**
- 기존 KFE Reference 자료에서는 인접한 Helical Line의 전류원 사이의 위상차를 90º로 설계하였음.
- 위상차를 90º로 설계하기 위해서 Helical Line의 한 주기의 길이를 5/4파장(790mm)로 설계하였음.

&nbsp;&nbsp;&nbsp; $n_{ll} = c \frac{k_{ll}}{\omega} \approx \frac{\Delta \phi}{D} \times \frac{c}{2 \pi f}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (1)

- 안테나에서 방사된 파의 Parallel Refractive Index nll​ 은 식 (1)로 표현될 수 있으며, D=52mm는 KSTAR 헬리콘 전류 구동에 최적의 값 nll = 3을 만족하도록 결정됨.
**[KWU (step2)]**
- 인접한 Helical Line의 전류원 사이의 위상차를 60º로 설계하였음.
- Helical Line의 한 주기의 길이를 7/6파장(735mm)로 설계하였음.     


|<img src="/History/img/img4.png" width="500" >|<img src="/History/img/img5.png" width="500" >|
--|--
|   **<KFE reference>**  | **<KWU>** |


----

**[KFE reference & KWU (step3)]**
- 기계적 강성을 강화하기 위해 각 Helical Line의 중간 지점에서 연결하는 구조가 도입 됨.
- GND와 Helical Line을 연결하며, 길이가 1/4 파장으로 설계함으로써 열린 효과를 얻을 수 있음.

- **[KFE reference & KWU (step4)]**
- 공간 제약을 고려하여 안테나의 크기를 600 mm × 361 mm로 축소하고, Faraday Shield를 추가하여 fast wave 성분의 E-field 방사를 촉진하였음.

**(2) Integration of _Parallel Refractive Index_ as a custom CST optimization variable**

□ **N_parallel 및 Directivity 출력 VBA 코드 개발** <br>
**1. VBA 코드 개발의 필요성** <br>
- 해당 정보를 출력하기 위한 기존의 과정은 3개의 플랫폼을 거쳐야 했다.<br>
- CST Studio에서 E-field 정보를 txt 형태로 추출하고, 그 자료에서 문자 정보를 수작업으로 제거해야 파이썬 코드를 통해 Peak N_parallel과 Directivity 값을 구할 수 있었다.<br>
- CST에서 한 번 시뮬레이션을 돌릴 때마다 N_parallel 및 Directivity 결과를 확인하기 위해서는 위의 과정을 반복해야 하는 번거로움이 있었기에 과정을 단축하고자 VBA 코드를 작성했다. <br>

|<img src="/History/img/img1.png" width="800" >|
--|
|<div align = "middle"> **<기존의 N_parallel 및 Directivity 출력 과정 흐름도>**|


**2. VBA 코드 제작**
- E-field의 정보를 가져오는 코드는 다음과 같이 표현할 수 있다. 해당 코드에 나온 주소는 CST 내부 Navigation Tree의 Tables에 속한 1D Results에서 필요한 E-field 자료의 이름을 작성하면 된다. 

```VBA
 ' E-Field data extraction
    Set dataY = ResultTree.GetResultFromTreeItem("Tables\1D Results\curve1_e-field (f=0.476) (1)", "3D:RunID:0")
```

- E-field 정보를 저장할 txt의 위치와 이름을 설정한다. 경로는 본인 PC에 맞게 설정해 주면 되며, 해당 주소의 파일이 존재하지 않아도 시뮬레이션을 돌리면 자동 생성된다.
- 시뮬레이션을 돌릴 때마다 자동으로 덮어쓰기가 되므로 파일을 다른 주소에 새로 저장할 필요가 없어진다. 

```VBA
 ' File storage path
 Dim filePath As String
 filePath = "\\tsclient\D\N_parallel\output.txt"
 Dim fileNum As Integer
 fileNum = FreeFile()
```

- 해당 주소의 txt 파일에 E-field 정보(Length, Re, Im)를 저장하는 코드이다.

```VBA
 ' Save To data file (save only numeric values separated by tabs)
  For index = 0 To totalPoints - 1
     Re_Vm(index) = dataY.GetYRe(index)
     Im_Vm(index) = dataY.GetYIm(index)
     Length_mm(index) = dataY.GetX(index)

     ' Save data format as “length, real part, imaginary part”
     Print #fileNum, Length_mm(index) & vbTab & Re_Vm(index) & vbTab & Im_Vm(index)
  Next index
```

- 파일을 수동으로 선택하는 방식이던 기존 파이썬 코드를 수정하여 위의 VBA 코드에서 설정한 txt 주소에서 정보를 불러오도록 고정한다. 
- 코드를 아래와 같이 수정함으로써 사람의 개입을 줄이고 자동화 작업을 만들 수 있다. 

|<img src="/History/img/code1.png" width="1000" >|
--|
|<div align = "middle"> **수정** :arrow_down: |
|<img src="/History/img/code2.png" width="1000" >|

|<img src="/History/img/code3.png" width="1000" >|
--|
|<div align = "middle"> **수정** :arrow_down: |
|<img src="/History/img/code4.png" width="1000" >|

- N_parallel 및 Directivity를 출력하기 위한 파이썬 코드 주소를 설정한다. 

```VBA
 ' Python Address settings
 Dim scriptPath As String
 scriptPath = "\\tsclient\D\N_parallel_Sinlge_data_20241105.py"
```

- Visual Studio Code에서 시뮬레이션 돌린 결과를 불러오는 코드이다. 

```VBA
 ' Python execution
 Dim result As Double
 result = Shell("python """ & scriptPath & """", vbNormalFocus)
 ```

- 상기 언급된 VBA 코드를 사용하여, 패러데이 쉴드가 포함되지 않은 안테나의 경우 1분 이내, 쉴드가 포함된 경우 2-3분 내에 Peak N_parallel과 Directivity 값을 구할 수 있다.
- VBA Macro가 작동하는 동안 다른 Macro 선택지들의 비활성화를 확인함으로써 선택한 Macro가 동작하고 있음을 알 수 있다.

|<img src="/History/img/img2.png" width="1000" >|<img src="/History/img/img3.png" width="1000" >|
--|--
|<div align = "middle"> **<VBA Macro 실행 화면>**|<div align = "middle"> **<VBA Macro 실행 결과>**|

- 이렇게 만들어진 VBA 코드는 안테나 설계 시 중요한 평가 지표인 N_parallel 및 Directivity 출력 자동화 작업에 활용이 된다.


