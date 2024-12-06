with open("prints.txt", "r") as f:
    input = f.read()
    f.close()

tmp, prints = input.split(" ")
rules = {}
for i in tmp.splitlines():
    if not i.split("|")[0] in rules:
        rules[i.split("|")[0]] = []
    rules[i.split("|")[0]].append(i.split("|")[1])

prints = [i.split(",") for i in prints.splitlines()][1:]

print(rules)
print(prints)

corrected = []
for numbers in prints:
    if 0 == prints.index(numbers) == len(prints)-1:
        continue
    counted = []
    incorrect = False
    for i in numbers:
        try:
            for j in rules[i]:
                if j in counted:
                    incorrect = True
        except:
            pass
        counted.append(i)
    if not incorrect:
        corrected.append(numbers)

val = 0
for i in corrected:
    print(i)
    val += int(i[int((len(i))/2)])
print(val)