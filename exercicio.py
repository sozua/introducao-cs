def nomeMaisCurto(namesArray):
    maisCurto = ""
    for rawName in namesArray:
        name = rawName.strip().capitalize()
        if(len(name) < len(maisCurto) or len(maisCurto) == 0):
            maisCurto = name
    return maisCurto


names = ["Juliana",    "Pedro", "   jó    "]
shortestName = nomeMaisCurto(names)
print(shortestName)
