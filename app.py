# import json
# movies = open("./movies.json", encoding="utf8")
# data = json.load(movies)
# # num = 0
# # for i in range(14117):
# #     x = data[num]["title"]
# #     print(x)
# #     num += 1
# num = 0
# y = data[num]["year"]
# year = input("Movies after this year  ")
# year = str(year)
# y = str(y)
# #for i in range(14117):
    

x = input("Give a sentence in either french or english ")
y = x.count('t')
z = x.count('T')
Ts = y + z
v = x.count('s')
w = x.count('S')
Ss = v + w
if Ts > Ss:
    print("English")
elif Ss > Ts:
    print("French")
