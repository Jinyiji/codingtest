def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer


def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score2 - score1)   # 수정
    return answer


# 1. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최댓값을 구합니다.
# 2. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최솟값을 구합니다.
# 3. 1번과 2번 과정에서 구한 점수를 리스트에 담아 return 합니다.

def solution(mid_scores, final_scores):
    # 1. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최댓값을 구합니다.
    up = func_a(mid_scores, final_scores)
    # 2. 각 학생에 대하여 기말고사 점수에서 중간고사 점수를 뺀 값의 최솟값을 구합니다.
    down = func_b(mid_scores, final_scores)
    # 3. 1번과 2번 과정에서 구한 점수를 리스트에 담아 return 합니다.
    answer = [up, down]
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


# mid_scores와  final_scores가 다음과 같을때의 return값을 구하시오
# [10, 100, 70] | [30, 60, 20]
# [20, -50]

