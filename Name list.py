Names = []
while True:
    Input = int(input("1 - Add name\n2 - Remove name\n3 - Change name\n4 - View names\nInput: "))
    if Input == 1:
        Names.append(str(input("Add what name?\nInput: ")))

    elif Input == 2:
        Names.pop(int(input("Remove which name?\nInput: ")))

    elif Input == 3:
        Names.pop(int(input("Change which name?\nInput: ")))
        Names.append(str(input("Change it to what?\nInput: ")))
    elif Input == 4:
        print(Names)
