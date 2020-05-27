entry = ""
dic = {}
while entry != "MEOW":
    entry = input()
    if entry != "MEOW":
        dic.update({entry.split()[0]: int(entry.split()[1])})
print(max(dic, key=dic.get))

