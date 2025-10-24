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


# def slots(q, x, y, z):
#     slot1 = x
#     slot2 = y
#     slot3 = z
#     quarters = q
#     plays = 0
#     while quarters > 0:
#         if slot1 < 35 and quarters > 0:
#             slot1 += 1
#             plays += 1
#             quarters -= 1
#         elif slot1 == 35:
#             quarters += 30
#             slot1 = 0
#         if slot2 < 100 and quarters > 0:
#             slot2 += 1
#             plays += 1
#             quarters -= 1
#         elif slot2 == 100:
#             quarters += 60
#             slot2 = 0
#         if slot3 < 10 and quarters > 0:
#             slot3 += 1
#             plays += 1
#             quarters -= 1
#         elif slot3 == 10:
#             quarters += 9
#             slot3 = 0
#     print(f"Martha plays {plays} times before going broke")

# slots(77, 4, 9, 3)

plays = 0
def slots(q, x, y, z):
    plays = 0
    while q > 0:
        if x < 34:
            q -= 1
            x += 1
            plays += 1
        elif x == 34:
            q += 29
            x = 0
            
