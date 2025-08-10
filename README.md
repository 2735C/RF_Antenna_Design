# :star: TEAM: 캡스톤 설계 2팀  

## 🙋‍♂️팀원

| **정은지** | **유동옥** | **김태민** |
|:----------:|:----------:|:----------:|
| Team Leader | Antenna Performance <br> Improvement Developer | Antenna Performance <br> Improvement Developer |
| [<img src="/img/profile1.webp" width="250" height="250"><br />@mail](mailto:eunjijung1107@gmail.com) | [<img src="/img/profile2.png" width="250" height="250"><br />@mail](mailto:avanet9479@kw.ac.kr) | [<img src="/img/profile3.png" width="250" height="250"><br />@mail](mailto:steve3588@naver.com) |




## 🖊️Role

### :wolf: 정은지
- Team leader
**[HW]**
- Helical Antenna characteristic analysis
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
[ **Analysis of RF antenna characteristics and development of a performance improvement model for nuclear fusion plasma heating and current driving.** ]<br>


### 🧐연구의 필요성 및 기대 효과

**1. 핵융합 에너지 연구의 시장성**

최근 AI와 데이터 센터의 성장으로 전력 공급의 중요성이 떠오르면서 그 대안으로 핵융합 기술이 부각되고 있다. 중국은 대규모 자본을 투입하여 핵융합 기술에서 미국을 위협할 수준이며, 이에 대응해 미국은 민간 자본과 정부의 지원을 바탕으로 한 핵융합 스타트업 붐으로 상업적 핵융합 가능성을 제시하며 연구개발을 가속화하고 있다. 이와 같이 현재 세계 각국에서 안정적인 에너지 공급을 위한 기술적 우위를 확보하기 위해 노력하고 있다. 
우리나라 정부 역시 2050 Net-Zero 달성을 표방하며 핵융합에너지 상용화를 위한 국제핵융합실험로(ITER) 공동개발사업과 핵융합선도기술개발사업을 지원하고 있다. 24년 7월 정부가 발표한 ｢핵융합에너지 실현 가속화 전략｣에서 ‘핵융합 기술혁신’을 내세운 점에서 핵융합 전력 생산 위한 핵심기술 개발의 중요성을 알 수 있다. 


**2. 핵융합 안테나의 필요성**

핵융합 연구에서 안테나는 플라즈마를 효과적으로 가열하고 안정적으로 제어하는 데 중요한 역할을 한다. 플라즈마 가열 안테나는 플라즈마 온도를 핵융합 조건(수백만에서 수억 도)까지 올리기 위해 고주파(RF) 에너지를 전달하는 용도로 사용되며, 대표적으로 ICRH(Ion Cyclotron Resonant Heating)와 ECRH(Electron Cyclotron Resonant Heating) 방식이 있다.

전류 구동 안테나는 플라즈마 내부에 전류를 유도하여 자기장 구성을 제어하며, 이를 통해 플라즈마 안정성과 에너지 효율성을 향상시킨다. 이에 해당하는 기술로는 LHCD(Lower Hybrid Current Drive), ECCD(Electron Cyclotron Current Drive), 그리고 최근 연구가 활발한 HCD(Helicon Current Drive) 등이 있다. ICCD(Ion Cyclotron Current Drive) 역시 ICRH의 전류 구동 응용으로 볼 수 있다. 이 외에도 플라즈마 상태 분석을 위한 다양한 안테나 기술이 활용된다.

MW(메가와트)급 고출력 RF 시스템은 핵융합 플라즈마 가열과 안정적 제어를 위해 필수적이다. 핵융합 반응을 위해서는 플라즈마 온도를 충분히 높여야 하며, ICRH, ECRH, LHCD 등의 RF 시스템을 통해 고출력 에너지를 전달한다. 또한, MW급 RF 전력은 플라즈마 내부의 난류(turbulence)나 불안정성(instability)을 억제하는 데도 활용되어 안정적인 플라즈마 유지에 기여한다. 따라서 MW급 전력을 안정적으로 처리할 수 있는 안테나 기술 개발이 매우 중요하다.

기존의 자기 유도 전류 구동 방식은 주로 펄스형 운전에 제한되는 반면, RF 전류 구동 방식은 연속 운전(steady-state operation)이 가능하여 차세대 핵융합로의 지속 가능한 운영을 목표로 한다. 특히 헬리콘 전파를 이용하는 HCD는 400~500 MHz 대역에서 높은 효율로 전류를 구동하는 기술로, LHCD를 보완하거나 대체할 가능성으로 주목받고 있다.


**연구 목적**

본 연구에서는 “핵융합 플라즈마 가열 및 전류 구동용 RF 안테나”라는 주제로 Parallel Refractive Index 개념을 바탕으로 하여 CST Simulation 기반으로 
Combline Antenna, Helical Antenna를 활용해서 기존 안테나의 성능을 분석 및 성능 향상을 목표로 하여 설계를 하고자 한다.

**기대 효과**

두 가지 형태(Combline, Helical)의 핵융합 발전을 위한 고효율 플라즈마 가열 안테나 설계를 진행하며 어느 유형의 안테나가 플라즈마 가열 안테나에 더 적합한지 비교 분석이 가능할 것이라 기대된다. 또한, 플라즈마 가열이라는 새로운 분야에서의 안테나의 활용도 및 기술의 성장을 예측할 수 있다.

## 🗓️개발 일정 2024.09.05 ~ 2024.12.16

### <개발 순서>

1. 관련 논문 분석                
2. 기존 안테나 특성 분석
- Reconstruction of the existing antenna model in CST and analysis of parameter-dependent characteristics    
3. Parallel Refractive Index 계산을 위한 파이썬 코드 분석            
4. Combline/Helical Antenna model 성능 개선
5. CST 내장 변수에 없던 Parallel Refractive Index를 최적화 변수로 구현 및 자동화      
6. MATLAB에서 CST 시뮬레이션을 원격 제어하여 다양한 최적화 알고리즘 적용 환경 마련   

## 개발 과정
> 더 많은 내용을 확인하고 싶으면 --> [[보고서]](/result/오성욱교수님_캡스톤설계2_2팀_최종%20보고서.pdf)


🔥🔥🔥🔥 디버깅 과정은 Trouble 슈팅 칸 만들거니까 개발 과정에는 결론만 적어주셈 🔥🔥🔥🔥

## (1) Fixed point modeling

### 

Fixed, float 개념부터 foarmat 관련 이야기랑 matlab 시행착오 등등 적으면 될 듯

## (2) RTL Simulation

### Butterfly Calculation

#### step 0
step마다 각각 twiddle factor가 다르니까 format이랑 연산 방법 등에 대해 소개하던가 코드 부분 발췌해서 설명하던가(허수 실수 교차 되는 거 등등)

#### step 1
솰라솰라

#### step 2
솰라솰라
### CBFP
솰라솰라

### 시뮬 사진 
아무 생각이 없다

## (3) Synthesis

합성 결과 사진 첨부 이건 제가 파일 zip 해제 안 해도 돼서 제가 넣을게요


## (4) Gate Simulation

### Testbench Code 핵심 첨부 및 설명
솰라솰라


### 시뮬 사진

이미지 

## (5) FPGA Targeting

### Vivado

vio 연결 설정이랑 xdc 설정 관해서 언급 및 사진, 결과 적기 
