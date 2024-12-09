input = 20


def find_prime_list_under_number(number):
    arr = []

    # 2 부터 20까지 반복문 실행
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)

    return arr
result = find_prime_list_under_number(input)
print(result)