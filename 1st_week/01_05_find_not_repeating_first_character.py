def find_not_repeating_first_character(string):
    arr = [0] * 26
    a_ascii = ord("a")
    for char in string:
        index = ord(char) - a_ascii
        if arr[index] > 1:
            continue
        else:
            arr[index] = arr[index] + 1

    for i in string:
        index = ord(i) - a_ascii
        if arr[index] == 1:
            return chr(a_ascii + index)

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
