#다음과 같이 import를 사용할 수 있습니다.
import math

def solution(scores):
    _min = 100
    _max = 0
    _sum = 0
    for s in scores:
        _sum += s
        if s < _min :
            _min = s
        if s < _max :
            _max = s

    answer = (_sum - _min - _max) // (len(scores) - 2)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")


# scores가 다음과 같을때 return값을 구하시오
# [1, 0, 99, 100, 43, 2] = 61


