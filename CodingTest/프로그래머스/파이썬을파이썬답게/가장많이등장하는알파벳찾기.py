from collections import Counter
my_str = input().strip()
answer=[]
a = Counter(my_str)

#비교하기위해 가장 많이쓰인 키의 값을 기준으로 삼음.
b=max(a.values())

# 딕셔너리 순회하며 value가 최대와 같으면 key를 answer배열에 추가
for (key, value) in a.items():
    if value == b:
        answer.append(key)
answer = sorted(answer,reverse=False)
print(''.join(answer))

"""
Counter는 딕셔너리 형태로 리턴.


느낀점:
    자바스크립트에 익숙해져 있어서인지.. 파이썬 dictonary 접근 하는방법이 너무 짜증나게한다.
    특히나... 백틱이 없는것이 너무 짜증난다. 
    처음엔 힌트에서 Counter를 쓰는것에서 힌트를 얻었고 , Counter를 통해 빈도수가 높은것들이
    알아서 딕셔너리 형태로 반환해주는것이 편했는데..
    Counter의 most_common()로 해결할까 했는데.. 뭔가 복잡해졌고 ..
    이후 가장 많이쓰인 알파벳의 값을 기준으로 삼고 딕셔너리 순회를 하며 값이 같은것들만 배열에
    추가하려고 했다. 근데 이 과정에서.. dict 값 접근하는 방법이. 어려웠다.
    흔히 보는 값에 대한 접근은 키로 접근하는데 , str형태로만 찾아야하고 .. str은 항상 바뀌기 때문이다.
    values()를 사용하여 그중에 가장 큰값을 기준으로 삼는것으로 문제 해결을 했다.


"""

