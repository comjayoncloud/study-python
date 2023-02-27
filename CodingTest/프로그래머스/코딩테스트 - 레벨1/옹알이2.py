
def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]     #가능한 4가지 발음 리스트
    for i in babbling:                  #babbling 문자열 배열만큼 반복
        for v in speak:                 #4가지 발음으로 반복
            if v*2 not in i:            #연속된 같은발음이 없다면
                i=i.replace(v,' ')      #' '으로 발음을 치환
                print(i)
        if i.strip()=='':               #치환 완료된 문자열의 공백을 제거하고 ''와 같다면
            answer+=1                   #발음가능한 단어로 카운팅
    return answer

# solution(["aya", "yee", "u", "maa"]	)
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])

"""
해결방안
A. 
    말할수 있는 조합 1,2,3,4를 다 구해서 있는지 없는지 확인하려면 너무많은 for문이라서 시간초과가 일어날거같다.
    그렇다면 받은 배열이 몇개의 조합인지 파악하면 되지않을까?
    조합이 몇개인지 파악하려면.. 기준이 필요하다. 기준은 기존에 있는걸로 파악하자 u로 정하자 가장 짧으니까.
    => u로 계산하니.. 잘 보아하니 예제엔 2개 조합,3개조합 다나왔다.
"""