with open("prints.txt", "r") as f:
    input = f.read()
    f.close()

tmp, numbers = input.split(" ")
rules = {}
for i in tmp.splitlines():
    rules[i.split("|")[0]] = i.split("|")[1]

numbers = [i.split(",") for i in numbers.splitlines()][1:]

print(rules)
print(numbers)

counted, corrected = [], []
for i in numbers:
    incorrect = False
    for j in i:
        try:
            if rules[j] in counted:
                incorrect = True
        except:
            pass
        counted.append(i)
    if not incorrect:
        corrected.append(i)

val = 0
for i in corrected:
    print(i)
    val += int(i[int((len(i))/2)])
print(val)