# About Array basic

Contents
> * Array basic
> * Linked List


# Array basic

* 최고의 경우: O(1) 자주일어남 내부 배열에 여유 공간이 있을때
* 최악의 경우: O(n) 가끔일어남 내부 배열이 꽉차있을때

* 분할 상환 분석(Amortized Analysis) 쉽게 말해 할부임
    - 같은 동작을 n번 했을 때 드는 시간이 x일떄: 동작을 한 번 하는 데 걸린 시간 x/n
    - 즉, 시간복잡도의 최악의 경우가 아니라 평균을 내서 말하는 것임. 더 합리적인 시간 복잡도 계산 가능함.

* 삽입 연산(insert operation)
    - 정적 배열에 남는 공간이 있을때: O(n)
    - 정적 배열이 꽉 찼을 때: O(n)
<br>
<br>

# Linked List
* 데이터 순서대로 저장, 요소 추가 가능.
~~~python
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
~~~

