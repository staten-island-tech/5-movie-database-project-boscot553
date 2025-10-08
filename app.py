import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)


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


genre = input("Search for a movie genre  ")
num = 0
for i in range(14117):
    if genre == data[num]["genres"]:
        print(data[num]["title"])
        num += 1
    else:
        num += 1






