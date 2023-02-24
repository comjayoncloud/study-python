def solution(strings, n):
    # 1. 왜 처음에 sort()한번 해줄까? 이유는 분석 및 느낀점확인
    strings.sort()
    # 2. n 인덱스만 추출한 배열
    answer = list(i[n] for i in strings)

    # 3. strings와 n인덱스만 추출한것을 zip으로 합침. 
    a = list(zip(answer,strings))

    # 4. n 인덱스 기준으로 sort 해줌
    a.sort(key=lambda a:a[0])

    # 5. sort 되있는것들중 기존 strings에 있는 문자들만 뽑아서 리스트
    b = [i[1] for i in a]
    return b



# def solution(strings, n):
#     strings.sort()
#     print(strings) 
#     return sorted(strings, key=lambda x:x[n])

# solution(["sun", "bed", "car"],1)
solution(["abce", "abcd", "cdx"],2)

"""
분석 및 느낀점
    sort를 사용할 때, 람다 함수를 쓰면 . 정확히 그 지점만을 가지고 정렬한다. 하지만 여기서 문제가 생긴다.
    만약 그 지점에 같은 문자열이 있을경우 , 사전순으로 앞선 문자열이 앞쪽에 위치한다.
    예를 들어 , abce , abcd 에선 . abc까지 동일하다. e와 d를 정렬 했을때 d가 나와야한다. 하지만 
    배열 선언시 abce가 abcd보다 앞서게 선언이 되었기에. 그 순서를 따라간다. 
"""