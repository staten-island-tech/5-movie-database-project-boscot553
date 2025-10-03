import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
# num = 0
# for i in range(14117):
#     x = data[num]["title"]
#     print(x)
#     num += 1

num = 0
y = data[num]["year"]
year = input("Movies after this year  ")
year = str(year)
y = str(y)
print(y)
#for i in range(14117):
    
    

