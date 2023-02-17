import numpy as np

def solution(id_pw, db):
    for i in db:
        # 1. 아이디 비번 일치했을경우 
        if np.array_equal(id_pw,i)==True:
            return "login"
        # 2-1 id만 일치했을경우
        elif id_pw[0] == i[0]:
            return "wrong pw"
        else:
            continue
        
    # 2-2 id, 비밀번호 둘다 일치하지 않았을경우
    return "fail"

# solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])
solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])


"""
1. 아이디와 비밀번호 모두 일치하는 회원 정보가 잇으면 'login
2. 아이디가 일치하는 회원이 없으면 fail , 아이디는 일치하지만 비밀번호가 일치하지 않으면 wrong pw

    1. 아이디 비밀번호 일치 찾기
        - 비교 연산자 ==
        - set 함수
        - np.array_equal()

    2. 
        2-1 아이디만 일치하는 경우 - wrong pw
        2-2 아이디 일치 하지 않는사람 - fail
"""

"""
다른사람코드1
    def solution(id_pw, db):
        if db_pw := dict(db).get(id_pw[0]):
            return "login" if db_pw == id_pw[1] else "wrong pw"
        return "fail"
"""