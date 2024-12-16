import numpy as np

with open("reports.txt", "r") as f:
    input = f.read()
    f.close()
safeamount = 0

def check_safety(arr):
    safe = True
    pos = []
    for j in range(len(arr)):
        if j+1 < len(arr):
            # if distance greater than 3
            if arr[j]-arr[j+1] > 3:
                safe = False
                pos.append(j)
            # if increasing
            if arr[j] < arr[j+1]:
                safe = False
                pos.append(j)
            # if number is the same
            if arr[j] == arr[j+1]:
                safe = False
                pos.append(j)
    return [safe, pos]

def is_ascending(arr):
    up, down = 0, 0
    for a in range(len(arr)):
        if a+1 >= len(arr):
            break
        if arr[a] < arr[a+1]:
            up += 1
        else:
            down += 1
    
    if up > down:
        return True
    else:
        return False

reports = input.splitlines()
for i in range(len(reports)):
    reports[i] = (np.array(reports[i].split(" ")).astype(int)).tolist()

    # check wether safe or unsafe
    if len(reports[i]) >= 2:
        # if increasing, reverse
        if is_ascending(reports[i]):
            reports[i].reverse()
        safe, pos = check_safety(reports[i])
        if not safe:
            print("\n"+str(i)+": "+str(reports[i]))
            print(str(len(pos))+" errors found at "+str(pos))
            for j in range(len(reports[i])):
                tmp = reports[i].copy()
                del tmp[j]
                safe = check_safety(tmp)[0]
                print(str(j)+" removed: "+str(tmp))
                if safe:
                    print("now safe")
                    break
                
        if safe:
            safeamount += 1
        else:
            print(str(reports[i])+" is not safe: "+str(len(pos))+" errors")

print(safeamount)