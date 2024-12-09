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

reports = input.splitlines()
for i in range(len(reports)):
    reports[i] = (np.array(reports[i].split(" ")).astype(int)).tolist()

    # check wether safe or unsafe
    if len(reports[i]) >= 2:
        # if increasing, reverse
        if reports[i][0] < reports[i][1]:
            reports[i].reverse()
        safe, pos = check_safety(reports[i])
        print(pos)
        if not safe and not len(pos) > 1:
            tmp = reports[i]
            del tmp[pos[0]]
            safe = check_safety(reports[i])[0]

            if not pos[0]+1 >= len(reports[i]):
                tmp = reports[i]
                del tmp[pos[0]+1]
                safe = check_safety(reports[i])[0]

        if safe:
            print(str(reports[i])+" is safe")
            safeamount += 1
        else:
            print(str(reports[i])+" is not safe: "+str(len(pos))+" errors")

print(safeamount)