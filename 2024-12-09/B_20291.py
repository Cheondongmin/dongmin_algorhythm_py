# 첫 줄에서 파일 개수 N을 입력받습니다
n = int(input())

# N개의 파일 이름을 리스트로 저장합니다
files = []
for string in range(n):
    files.append(input().split(".")[1])

files.sort()

cnt = 1
index = 0
res = {}

for i in range(len(files)):
    value = files[i]+ " " + str(cnt)
    if i == 0:
        res[index] = value
        continue
    if res[len(res)-1] != value:
        cnt = 1
        index += 1
        res[index] = (str(files[i]) + str(" 1"))
    else:
        cnt += 1
        res[index] = str(res[index].split(" ")[0]) + " " + str(cnt)

for i in res:
    print(res[i])