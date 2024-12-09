"""
주어진 범위 내의 모든 소수를 찾는 프로그램

Parameters:
    start (int): 시작 범위
    end (int): 끝 범위

Returns:
    None, 각 소수를 출력함

알고리즘:
    1. start부터 end까지의 모든 숫자를 소수라고 가정
    2. 2부터 시작해서 해당 숫자의 배수들을 모두 지움
    3. 남은 숫자들이 소수
"""

import sys
from math import sqrt  # sqrt 함수 임포트


def find_primes(start, end):
    # 모든 숫자를 일단 소수라고 표시
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    # 2부터 end의 제곱근까지만 확인하면 됨
    # 예: end가 100이면 10까지만 확인하면 됨
    sqrt_end = int(sqrt(end))

    # 2부터 숫자를 키워가며 확인
    for i in range(2, sqrt_end + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들은 모두 소수가 아님
            for j in range(i * 2, end + 1, i):
                is_prime[j] = False

    # start부터 end까지 중에서 소수만 출력
    for i in range(start, end + 1):
        if is_prime[i]:
            print(i)


# 입력 받기
start, end = map(int, input().split())
find_primes(start, end)