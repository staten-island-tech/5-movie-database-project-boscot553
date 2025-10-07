import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)


# for i in range(14117):
#     x = data[num]["title"]
#     print(x)
#     num += 1
# num = 0

year = input("Movies after this year  ")
year = int(year)
num = 0
y = data[num]["year"]
y = int(y)

for i in range(14116.5):
    if year < y:
        print(data[num]["title"])
        num += 1
        if num == "14117":
            break
        y = data[num]["year"]
        y = int(y)
    elif year > y or year == y:
        num += 1
        if num == "14117":
            break
        y = data[num]["year"]
        y = int(y)
        




