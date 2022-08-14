# About how to do a data modeling

Contents
> * 데이터 모델링
> * 논리적 모델링
> * 정규화
> * 물리적 모델링


# 데이터 모델링
* 개념적 구조를 정하는 것 -> 논리적 모델링
* 데이터베이스 구축에 필요한 걸 정하는 것 -> 물리적 모델링

* 데이터 모델링 목적
    * 저장하고자 하는 데이터에서 Entity, Attribute, Realationship, Constraint 파악하기 위함
    * 데이터베이스를 구축할 때 기반이 될 모델 만들기

* Relation = 테이블 (row와 colum으로 만들어진 기본적인 데이터 테이블을 의미함)
    * Relation은 테이블을 나타내는 수학적 용어

* 데이터 모델 정리
    * Entity Relationship Model (ERM)
        * ERM에서는 로우를 매번 표현해주지 않아도 되고, 선과 선의 끝점들을 통해서 Entity들 사이 관계를 조금 더 자세하게 표현할 수 있다.
    * 객체 관계형 모델
    * 개념 모델
    * 논리 모델
    * 물리 모델

<br>

# 논리적 모델링
* 비즈니스 룰
    *  "특정 조직이 운영되기 위해 따라야 하는 정책, 절차, 원칙에 대한 간단 명료한 설명"
* 비지니스 룰이 있을 때, Entity, Attribute, Relationship을 찾는 가장 기본적인 원칙
    * 1. 모든 명사는 Entity 후보입니다.
    * 2. 모든 동사는 Relationship 후보입니다.
    * 3. 하나의 "값"으로 표현할 수 있는 명사는 attribute의 후보입니다.
* "하나의 값으로 표현할 수 있는 명사는 attribute 후보"의 예외 경우. 하나의 값으로 표현할 수 있더라도, 하나의 entity가 여러 개의 값을 가져야 하는 경우 (예를들어 유저 entity에 adress 컬럼이 3개이상)
    * NULL이 많이 생길 수 있게 된다
    * 컬럼을 몇 개를 만들어야 되는지 애매해진다
    * 조회가 비효율적이게 된다
    * 주소를 컬럼이 아니라, 새로운 테이블(Entity)로 만든다. 이렇게 하면 방금 본 세 가지의 문제점이 생기지 않으며, 깔끔하게 모델링을 할 수 있다.
* ERM을 활용하면 회사의 전반적인 데이터 베이스 구조를 쉽게 파악 할 수 있다. 카디널리티를 사용하여 데이터 테이블간 관계를 쉽게 설정 할 수 있다.

<br>

# 정규화(Normalization)
* 장점
    * 데이터베이스에서 삽입, 업데이트, 삭제이상을 없앤다.
    * 새로운 종류의 데이터를 추가할 때 테이블 구조 수정을 안 해도 된다.
    * 데이터베이스 구조를 단순화해서 사용자가 더 쉽게 이해할 수 있다.
* **1NF**
    * 테이블 안 모든 로우의 모든 컬럼 값들은 나눌 수 없는 단일값 이어야 한다.
    * 한 컬럼에 같은 종류의 값을 여러 개 저장하고 있을 때
        * 이때는 해당 컬럼을 하나의 테이블로 분리해서 모델링합니다.
    * 한 컬럼에 서로 다른 종류의 값을 여러 개 저장하고 있을 때
        * 이때는 한 컬럼을 여러 개로 분리해서 모델링합니다.
* **함수 종속성 (Function Dependency)**
    * y = 2x + 1 --> x의 값에따라 y가 바뀐다. 즉, y는 x에 대한 함수 종속성이 있다. x -> y
    * 상품(x)의 사이즈와 가격은 상품에 따라 바뀐다. 즉, 사이즈와 가격은 상품에 대한 종속성이 있다. 상품 -> {사이즈, 가격}
    * score(y)는 user와 product에 따라 바뀐다. 즉, score는 user와 product에 대한 종석성이 있다. {user, product} -> score
    * 함수 종속성의 이행성: product -> brand -> brand_country brand는 product 에따라 바뀌고, brand country 는 brand 에 따라 바뀐다. 즉, brand는 product에 대한 종속성이 있고, brand country는 brand에 대한 종속성이 있다.
* **Candidate Key**
    * 하나의 row를 특정지을 수 있는 attribute들의 최소 집합
    * ID는 Candidate Key이다. 각각의 로우를 특정지을 수 있기 때문이다. (Prime attribute)
* **2NF**
    * 테이블에 candidate key의 일부분에 대해서만 함수 종속성이 있는 non-prime attribute가 없어야한다. 즉, user id, product id, age, price가 있을 때 age는 user에 대한 종속성이 있고, price는 product에 대한 종속성이 있기 때문에, (user -> age, product -> price) candidate key의 {user id, product id}전체가아닌 일부에만 의존하고 있다고 할 수 있다. 그래서 2NF에 부합하지 않는다.


# 물리적 모델링
* 네이밍의 중요성
* 데이터 타입
    * 데이터 정확성
    * 데이터 함수,연산 사용을 위해서
    * 데이터 용량을 최적화하기 위해서
* 인덱스 정리
    * Clustered
    * Non-Clustered