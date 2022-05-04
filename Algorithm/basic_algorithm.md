# About Basic Algorithm

Contents
> * Some basic algorithm code


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