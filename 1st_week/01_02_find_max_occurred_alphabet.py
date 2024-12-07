def find_max_occurred_alphabet(string):
    arr = [0]*26
    a_ascii = ord('a') # 우리는 이걸 0번째 인덱스 a부터 시작하는 배열로 활용할 것 이다.

    for char in string:
        if char.isalpha():
            index = ord(char) - a_ascii # 해당 알파벳을 a부터 시작한다고 가정했을때의 순서의 index를 취득한다.
            arr[index] += 1

    max_count = 0
    max_index = 0

    index = 0
    for alphabet_count in arr:
        if max_count < alphabet_count:
            max_count = alphabet_count
            max_index = index
        index += 1

    return chr(max_index + a_ascii)

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))





