

def solution(spell, dic):
    spell = set(spell) 
    
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2
 
# set 함수 : 중복되지 않은 원소를 얻고자 할때.
# x.issubset(y) => x가 y의 서브 set이 맞나?

solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])

"""
첫번째 코드 : 
    중복에 대해 처리하려면...너무코드가 복잡해질듯
def solution(spell, dic):
    answer = 0
    for a in (spell):
        for b in (spell) :
            for c in (spell):
                if a+b+c in dic:
                    answer =1
                else :
                    answer =2
    print(answer)
    return answer


solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
"""

"""
다른사람 코드:
def solution(spell, dic):
    spell = set(spell) 
    print(spell)
    print(spell.issubset(set(dic[3])))
    for i in dic:
        if spell.issubset(set(i)):
            return 1 
    return 2

"""


