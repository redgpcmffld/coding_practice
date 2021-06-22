# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


import math


def solution(nums):
    answer = 0
    sum_list = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum_list.append(nums[i] + nums[j] + nums[k])
    for s in sum_list:
        count = 0
        for k in range(2, math.ceil(math.sqrt(s)) + 1):
            if s % k == 0:
                count += 1
        if count == 0:
            answer += 1
    return answer
