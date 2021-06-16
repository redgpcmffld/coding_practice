def solution(left, right):
    answer = 0
    for integer in range(left, right+1):
        divisor = len([integer / int for int in range(1, integer+1) if integer % int == 0])
        if divisor % 2 == 0:
            answer += integer
        else:
            answer -= integer
    return answer