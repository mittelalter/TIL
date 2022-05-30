# About Basic Algorithm

Contents
> * concepts explain
> * Some basic algorithm code

### 탐색과 정렬의 차이점?

선형탐색은 정렬되지 않은 리스트, 정렬된 리스트 모두에서 사용할 수 있는 반면
이진탐색은 정렬된 리스트에서만 우리가 기대하는 효율을 낼 수 있기 때문에,
정렬이라는 것은 이진탐색을 하기 위한 용도라고 볼 수도 있을 것 같습니다.
즉, 정렬을 하는 목적은 결국에는 정렬이라는 행위를 통해 찾으려는 값을 빠르게 찾는 것(탐색)에 있다고 생각합니다.
정렬의 목적: 요소 탐색 시 효율적으로 탐색이 이루어지도록 하게 함(특히 이진 탐색에서 그러하고, 제한적으로는 선형 탐색에서도 그러함)
탐색의 목적: 최대한 빨리 원하는 요소를 찾아내는 것. 이 때, 선형탐색과 이진탐색 중 보통은 이진탐색이 더 효율적임

<br>

### Binary_search

왜 어려웠나?
- 시작값과 종료값이 바뀔 수 도 있다는것을 인지하지 못했음.
- While문 조건에 들어갈 로직을 엉뚱하게 썻음. 즉, 종료 인덱스 값이 0보다 작아지면 더 이상 비교할 대상이 없다는것을 인지하지 못함. 

~~~python
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
~~~


### Selection sort
어려웠던 점?
- for 내부 반복문에서 min_index값이 if문에서 걸렸다는 뜻은, 그 값이 현재까지는 최소값 이기때문에 더 이상 비교할 필요가 없다는 것, 따라서 비교했던 값으로 대체 (min_index = j). 이 부분을 인지하지 못함.

~~~python
# 0번 인덱스 부터 시작하여 리스트를 한번 돌고 제일 작은 값과 위치 교환, 그 다음 1번 인덱스 시작 이렇게 계속 인덱스 end값 까지 반복.
some_list = [4, 2, 7, 1, 9, 3]
o = 1
for i in range(len(some_list) - 1): #마지막 인덱스에서는 남는 값이 하나밖에 없어서 지장이 없다.
    min_index = i
    for j in range(i+1, len(some_list)): #내부 반목문에서 앞에 값들은 작은 값들이니까 고정되어 더이상 비교할 필요가 없기때문에 +1 해준다.
        if some_list[j] < some_list[min_index]:
            min_index = j #여기가 포인트, 한번 비교해서 값이 크면 더 이상 비교할 필요가 없기 때문에, 비교햇던 값과 대체한다.
    print(f"{o}번 돌음")
    o += 1
    some_list[i], some_list[min_index] = some_list[min_index], some_list[i]
    print(some_list)
~~~