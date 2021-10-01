# write and access your friends' birthdays
import json
birthdays = {}
with open("save.json") as f:
   birthdays = json.load(f)

def enter():
    while True:
        print("enter a name, blank to quit option")
        name = input()
        if name == '':
            break
        print("enter birthday")
        birthday = input()
        birthdays[name]=birthday; #no s
        with open("save.json", "w") as f:
                    json.dump(birthdays, f)

def access():
    while True:
        for k in birthdays.keys():
            print(k)
        print("enter a name, blank to quit option")
        name = input()
        if name == '':
            break
        print("birthday is "+str(birthdays[name]))

while True:
    with open("save.json") as f:
       birthdays = json.load(f)
    print("enter 1 to add birthdays, 2 to access, anything else to quit")
    opt = input()
    if opt == '1':
        enter()
    elif opt == '2':
        access()
    else:
        break
