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

# def genre()
# num = 0
# for i in range(14117):
#     if genre == data[num]["genres"]:
#         print(data[num]["title"])
#         num += 1
#     else:
#         num += 1


def honi(x):
    num = 0
    HONIS = 0
    for char in x:
        for char in x:
            if x[num] == "H":
                break
            else:
                num += 1
        for char in x:
            if x[num] == "O":
                break
            else:
                num += 1   
        for char in x:
             if x[num] == "N":
                break
             else:
                num += 1           
        for char in x:
            if x[num] == "I":
                HONIS += 1
                break
            else:
                num += 1           
    print(HONIS)
    
honi("HONIS")



        




# def honi(x):
#     num = 0
#     y = x[0]
#     for char in x:
#         y = x[num]
#         num += 1
#         if y == "H":
#             for char in len(x) - num:
#                 y = x[num]
#                 num += 1
#                 if y == "O":
#                     for char in x - num:
#                         y = x[num]
#                         num += 1
#                         if y =="N":
#                             for char in x - num:
#                                 y = x[num]
#                                 num += 1
#                                 if y =="I":
#                                     for char in x - num:
#                                         y = x[num]
#                                         num += 1
#                                         HONIS += 1
