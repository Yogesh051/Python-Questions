def info(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

info("Yogesh", age=19, place="Uttarakhand", district="champawat")        