with open("locationid.txt", "r") as f:
    input = f.read()
    f.close()
leftlist, rightlist = [], []
score = 0
similarity = 0

for i in input.splitlines():
    a, b = i.split("   ")
    leftlist.append(int(a))
    rightlist.append(int(b))

leftlist.sort()
rightlist.sort()


def distance(num1, num2):
    if num1 > num2:
        return num1-num2
    return num2-num1

for i in range(len(leftlist)):
    similarity += leftlist[i] * rightlist.count(leftlist[i])
    score += distance(leftlist[i], rightlist[i])

print(score)
print(similarity)