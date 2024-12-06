with open("prints.txt", "r") as f:
    input = f.read()
    f.close()

tmp, prints = input.split("\n\n")
print(tmp)
rules = {}
for i in tmp.splitlines():
    if not i.split("|")[0] in rules:
        rules[i.split("|")[0]] = []
    rules[i.split("|")[0]].append(i.split("|")[1])

prints = [i.split(",") for i in prints.splitlines()]

print(len([j for i in rules.values() for j in i]))
print(len(tmp.splitlines()))
# print(rules)
# print(prints)

# corrected = the right prints
# fixed = the previously false prints that have been fixed
corrected, fixed = [], []
for numbers in prints:
    if 0 == prints.index(numbers) == len(prints)-1:
        continue
    counted = []
    swapped = numbers
    incorrect = False
    for i in numbers:
        try:
            for j in rules[i]:
                if j in counted:
                    incorrect = True
                    swapped[numbers.index(i)], swapped[numbers.index(j)] = swapped[numbers.index(j)], swapped[numbers.index(i)]
        except:
            pass
        counted.append(i)
    if not incorrect:
        corrected.append(numbers)
    else:
        fixed.append(swapped)

val = 0
for i in corrected:
    val += int(i[int((len(i))/2)])
print(val)

fixval = 0
for i in fixed:
    fixval += int(i[int((len(i))/2)])
print(fixval)