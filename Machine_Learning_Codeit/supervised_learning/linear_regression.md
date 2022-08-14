# About Linear Regression (선형회귀)

Contents
> * 선형 회귀
    > * 용어
    > * 가설 함수 (Hypothesis Function)
    > * 평균 제곱 오차 (Mean Squred Error)
    > * 손실 함수 (Loss Function)

<br>

# 선형 회귀
* 선형 회귀란 무엇인가?
    * 가장 기본적인 머신러닝 알고리즘이다.
    * 특징: 데이터에 대한 최적선(line of best fit)을 찾는다.

<br>

* 선형 회귀 용어
    * 목표 변수(target, output variable): 맞추려고 하는 값 (집 값).
    * 입력 변수(input variable / feature): 목표 변수를 맞추기위해 사용하는 값 (집 크기).
    * 데이터 표현법: m=데이터 개수, x=입력 변수, y=목표 변수.

<br>

* 가설 함수 (Hypothesis Function)
    * 최적선을 찾아내기 위해 다양한 함수를 시도해 봐야 한다. 시도하는 이 함수 하나하나를 '가설 함수', 영어로는 'hypothesis function'이라고 부른다.
    * 찾으려는 선은 곡선이 아니라 직선이다. 즉, 일차 함수이다. y= ax + b로 표현된다. 결국 선형 회귀의 임무는 계수 a랑 상수 b를 찾아내는 것이다.
    * 선형 회귀: 가장 적절한 세타 값들을 찾아낸다. 세타 0 은 y = ax + b 에서 b를 의미한다.

<br>

* 평균 제곱 오차(MSE)
    * 가설 함수가 얼마나 좋은지 평가하는 하나의 방법, 선형 회귀에서 많이 쓰인다.
    * 데이터들과 가설 함수가 평균적으로 얼마나 떨어져 있는지 나타낸다.
    * 오차값 제곱후 데이터 개수로 나누기.
    * 제곱하는 이유 -> 더 큰 오차 부각하기 위해서.


<br>

* 손실 함수(Loss Function)
    * 가설 함수의 성능을 평가하는 함수
    * 손실 함수가 **작다** -> 가설 함수가 데이터에 잘 맞다.
    * 손실 함수가 **크다** -> 가설 함수가 데이터에 잘 안 맞다.