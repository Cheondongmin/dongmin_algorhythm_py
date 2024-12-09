"""
바뀔 시점에 count를 늘려준다, (첫번째 들어온 숫자가 아닌 숫자일 경우에만..)
"""
input = input()

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    first = ""
    now = ""
    res = 0
    for s in range(len(string)):
        if s == 0:
            first = string[s]
            now = string[s]
            continue
        if now != string[s]:
            now = string[s]
            if first != now:
                res += 1

    return res

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)