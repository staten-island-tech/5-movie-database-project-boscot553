import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
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

# for i in range(14117):
#     if year == y:
#         print(data[num]["title"])
#         num += 1
#         num = int(num)
#         y = data[num]["year"]
#         y = int(y)
#     elif year < y or year > y:
#         num += 1
#         if num < int("14117"):
#             y = data[num]["year"]
#             y = int(y)


# pro = input("Search for a movie  ")
# num = 0
# for i in range(14117):
#     if pro == data[num]["title"]:
#         print(data[num])
#         break
#     else:
#         num += 1


# x = input("Genre  ")
# num = 0
# for i in range(14117):
#     y = data[num]["genres"]
#     z = len(y)
#     if z == 1:
#         if x == y[0]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
#     if z == 2:
#         if x == y[0] or x == y[1]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
#     if z == 3:
#         if x == y[0] or x == y[1] or x == y[2]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
#     if z == 4:
#         if x == y[0] or x == y[1] or x == y[2] or x == y[3]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
#     if z == 5:
#         if x == y[0] or x == y[1] or x == y[2] or x == y[3] or x == y[4]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
#     if z == 6:
#         if x == y[0] or x == y[1] or x == y[2] or x == y[3] or x == y[4] or x == y[5]:
#             print(data[num]["title"])
#             num += 1
#         else:
#             num += 1
        
num = 0
x = input("Genre  ")
for i in range(14116):
    z = 0
    num += 1
    y = data[num]["genres"]
    for str in y:
        if x == y[z]:
            print(data[num]["title"])
            break
        else:
            z += 1
        
