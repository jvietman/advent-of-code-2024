with open("memory.txt", "r") as f:
    input = f.read()
    f.close()
value = 0

# search strings
search = "mul("
do = "do()"
dont = "don't()"
c, b1, b2 = 0, 0, 0 # iterator

com = False # if comma
num = ["", ""] # two multiply values
enabled = True # if enabled

for i in input:
    # search for do()
    if b1 >= len(do):
        enabled = True
        b1 = 0
    elif i == do[b1]:
        b1 += 1
    else:
        b1 = 0

    # search for don't()
    if b2 >= len(dont):
        enabled = False
        b2 = 0
    elif i == dont[b2]:
        b2 += 1
    else:
        b2 = 0

    # search for mul(
    if c < len(search):
        if i == search[c]:
            c+=1
        else:
            c=0

    # extract values
    elif c >= len(search):
        # stop extraction
        if i == ")":
            # if everything is correct
            if com and num[0] and num[1]:
                if enabled:
                    value += int(num[0]) * int(num[1])
            c, com, num = 0, False, ["", ""]

        # if comma, start extracting second number
        elif i == ",":
            if com or not num[0]:
                c, com, num = 0, False, ["", ""]
            else:
                com = True
                c+=1
            
        # extract number
        elif i.isdigit():
            num[len(search)-c] += i
        
        # if value invalid
        else:
            c, com, num = 0, False, ["", ""]

print(value)