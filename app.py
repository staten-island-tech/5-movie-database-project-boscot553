# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)
# num = 0

# for i in range(14117):
#     x = data[num]["title"]
#     print(x)
#     num += 1
# num = 0

# year = input("Movies after this year  ")
# year = int(year)
# num = 0
# y = data[num]["year"]
# y = int(y)

# for i in range(14117):
#     if year < y:
#         print(data[num]["title"])
#         num += 1
#         num = int(num)
#         if num < int("14117"):
#             y = data[num]["year"]
#             y = int(y)
#     elif year > y or year == y:
#         num += 1
#         y = data[num]["year"]
#         y = int(y)

# year = input("Movies before this year  ")
# year = int(year)
# num = 14116
# y = data[num]["year"]
# y = int(y)

# for i in range(14117):
#     if year > y:
#         print(data[num]["title"])
#         num -= 1
#         num = int(num)
#         if num > int("-1"):
#             y = data[num]["year"]
#             y = int(y)
#     elif year < y or year == y:
#         num -= 1
#         y = data[num]["year"]
#         y = int(y)
        
# year = input("Movies during this year  ")
# year = int(year)
# num = 0
# y = data[num]["year"]
# y = int(y)


        
# num = 0
# x = input("Genre  ")
# for i in range(14116):
#     num += 1
#     y = data[num]["genres"]
#     if x in y:
#         print(data[num]["title"])


def slots(q, x, y, z):
    plays = 0
    while q > 0:
        if x < 35 and q > 0:
            x += 1
            plays += 1
            q -= 1
        else:
            q += 30
            x -= 35
        if y < 100 and q > 0:
            y += 1
            plays += 1
            q -= 1
        else:
            q += 60
            y -= 100
        if z < 10 and q > 0:
            z += 1
            plays += 1
            q -= 1
        else:
            q += 9
            z -= 10
    print(f"Martha plays {plays} times before going broke")

slots(77, 4, 9, 3)