# 복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다.
# 복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.
#
# 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
# 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
# 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
# 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
# 제한사항
# weights의 길이는 2 이상 1,000 이하입니다.
# weights의 모든 값은 45 이상 150 이하의 정수입니다.
# weights[i] 는 i+1번 복서의 몸무게(kg)를 의미합니다.
# head2head의 길이는 weights의 길이와 같습니다.
# head2head의 모든 문자열은 길이가 weights의 길이와 동일하며, 'N', 'W', 'L'로 이루어진 문자열입니다.
# head2head[i] 는 i+1번 복서의 전적을 의미하며, head2head[i][j]는 i+1번 복서와 j+1번 복서의 매치 결과를 의미합니다.
# 'N' (None)은 두 복서가 아직 붙어본 적이 없음을 의미합니다.
# 'W' (Win)는 i+1번 복서가 j+1번 복서를 이겼음을 의미합니다.
# 'L' (Lose)는 i+1번 복사가 j+1번 복서에게 졌음을 의미합니다.
# 임의의 i에 대해서 head2head[i][i] 는 항상 'N'입니다. 자기 자신과 싸울 수는 없기 때문입니다.
# 임의의 i, j에 대해서 head2head[i][j] = 'W' 이면, head2head[j][i] = 'L'입니다.
# 임의의 i, j에 대해서 head2head[i][j] = 'L' 이면, head2head[j][i] = 'W'입니다.
# 임의의 i, j에 대해서 head2head[i][j] = 'N' 이면, head2head[j][i] = 'N'입니다.
#


def solution(weights, head2head):

    # 복서 리스트 만들기
    boxers = [boxer for boxer in range(len(weights))]

    # 자신보다 무거운 복서를 이긴 횟수 구하기
    def get_count_over_weight_wins(head2head, boxers, weights):
        result = {}
        for i in range(len(boxers)):
            count = 0
            for j in range(len(boxers)):
                if head2head[i][j] == 'W' and weights[i] < weights[j]:
                    count += 1
                result[i] = count
        return list(result.values())

    over_weights_points = get_count_over_weight_wins(head2head, boxers, weights)

    # 싸운 횟수 구하기
    def get_count_fights(str):
        if str.count('N') == len(str):
            return 0
        return len(str) - str.count('N')

    # 승률 구하기
    def get_win_rate(win_list, count_fights):
        if not count_fights:
            return 0.0
        return win_list / count_fights

    win_rates = [get_win_rate(games.count('W'), get_count_fights(games)) for games in head2head]
    array = []

    # 승률, 이긴 횟수, 무게, 복서 리스트 하나로 묶기
    for wins, point, weight, boxer in zip(win_rates, over_weights_points, weights, boxers):
        array.append((wins, point, weight, boxer))

    # python 내장 함수 sort의 key를 이용하여 조건별 순서대로 정렬하기
    array.sort(key = lambda x: (-x[0], -x[1], -x[2], x[3]))

    # 정렬된 리스트 인덱스에서 복서 번호 구하기 위해 +1 해주기
    answer = [i[3]+1 for i in array]
    return answer