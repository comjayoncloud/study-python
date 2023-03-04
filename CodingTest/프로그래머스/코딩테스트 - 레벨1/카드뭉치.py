

def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1_idx ,cards2_idx = 0,0
    
    for word in goal:
        if len(cards1) > cards1_idx and word == cards1[cards1_idx]:
            cards1_idx +=1
        elif len(cards2) > cards2_idx and word == cards2[cards2_idx]:
            cards2_idx +=1
        else:
            answer ="No"
            break
    print(cards1_idx,cards2_idx)
        

    return answer

solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"])



"""

걸린시간 : 8시 3분 ~ 

초기 생각한 해결방안 :
    원하는 카드 뭉치에서 카드를 순서대로 한장씩 사용한다
    한번 사용한 카드는 다시 사용할수 없음
    카드를 사용하지않고 다음 카드로 넘어갈 수없다
    단어 순서를 바꿀수 없다
    a[0]->b[0]->b[1]->a[1]->a[2]
    card1에서 시작하는경우 순서가 맞아야함.. 인덱스가 맞는지 확인
    card2에서 시작하는경우 순서가 맞아야함..
    
틀린점 및 해결방안 :
    투포인터..!


다른사람코드 및 리뷰 :
    def solution(cards1, cards2, goal):
        for g in goal:
            if len(cards1) > 0 and g == cards1[0]:
                cards1.pop(0)       
            elif len(cards2) >0 and g == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
        return "Yes"


"""