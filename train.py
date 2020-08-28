import pandas as pd

df = pd.read_excel("C:/Users/path/Downloads/train map out.xlsx")
i = 0
print("WELCOME TO RAILWAYS.")
print("1. Kanpur")
print("2. Delhi")
print("3. Banglore city")
a = input("Please enter the station you want to book from:")
if a == '1':
    print("WELCOME TO KANPUR RAILWAYS")
    b = input("Please enter the destination:")
    new = df.loc[df['Station 1'] == 'Kanpur']
    new1 = df.loc[df['Station 2'] == 'Kanpur']
    new2 = df.loc[df['Station 3'] == 'Kanpur']
    new3 = df.loc[df['Station 4'] == 'Kanpur']
    f = [new, new1, new2]
    new = pd.concat(f)
    if not new.empty:
        for index, row in new.iterrows():
            if new['Station 1'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 2'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 3'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 4'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
    if i == 0:
        print("No direct train for that destination")
        old = df.loc[df['Station 1'] == b]
        old1 = df.loc[df['Station 2'] == b]
        old2 = df.loc[df['Station 3'] == b]
        old3 = df.loc[df['Station 4'] == b]
        g = [old, old1, old2, old3]
        old = pd.concat(g)
        for index, row in new.iterrows():
            for index1, row1 in old.iterrows():
                if new['Station 1'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
if a == '2':
    print("WELCOME TO DELHI RAILWAYS")
    b = input("Please enter the destination:")
    new = df.loc[df['Station 1'] == 'Delhi']
    new1 = df.loc[df['Station 2'] == 'Delhi']
    new2 = df.loc[df['Station 3'] == 'Delhi']
    f = [new, new1, new2]
    new = pd.concat(f)
    if not new.empty:
        for index, row in new.iterrows():
            if new['Station 1'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 2'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 3'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 4'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
    if i == 0:
        print("No direct train for that destination")
        old = df.loc[df['Station 1'] == b]
        old1 = df.loc[df['Station 2'] == b]
        old2 = df.loc[df['Station 3'] == b]
        old3 = df.loc[df['Station 4'] == b]
        g = [old, old1, old2, old3]
        old = pd.concat(g)
        for index, row in new.iterrows():
            for index1, row1 in old.iterrows():
                if new['Station 1'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 1'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 2'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 3'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 1'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 2'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 3'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 4'][index1]:
                    print("You can first travel through ", new['Train name'][index],
                          ' and then you can change the train at ')
                    print(new['Station 4'][index], " to ", old['Train name'][index1])
                    i = 1
                    break
if a == '3':
    print("WELCOME TO BANGLORE CITY RAILWAYS")
    b = input("Please enter the destination:")
    new = df.loc[df['Station 1'] == 'Banglore City']
    new1 = df.loc[df['Station 2'] == 'Banglore City']
    new2 = df.loc[df['Station 3'] == 'Banglore City']
    f = [new, new1, new2]
    new = pd.concat(f)
    if not new.empty:
        for index, row in new.iterrows():
            if new['Station 1'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 2'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 3'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
            elif new['Station 4'][index] == b:
                print("you can travel through ", new['Train name'][index])
                i = 1
                break
    if i == 0:
        print("No direct train for that destination")
        old = df.loc[df['Station 1'] == b]
        old1 = df.loc[df['Station 2'] == b]
        old2 = df.loc[df['Station 3'] == b]
        old3 = df.loc[df['Station 4'] == b]
        g = [old, old1, old2, old3]
        old = pd.concat(g)
        for index, row in new.iterrows():
            for index1, row1 in old.iterrows():
                if new['Station 1'][index] == old['Station 1'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 1'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 2'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 1'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 3'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 1'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 1'][index] == old['Station 4'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 1'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 1'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 2'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 2'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 2'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 3'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 2'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 2'][index] == old['Station 4'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 2'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 1'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 3'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 2'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 3'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 3'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 3'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 3'][index] == old['Station 4'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 3'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 1'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 4'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 2'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 4'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 3'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 4'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
                if new['Station 4'][index] == old['Station 4'][index1]:
                    print("You can first travel through ",new['Train name'][index],' and then you can change the train at ')
                    print(new['Station 4'][index]," to ",old['Train name'][index1])
                    i = 1
                    break
if i == 0:
    print("No direct or connecting train for that destination")

