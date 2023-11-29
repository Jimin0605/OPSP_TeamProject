import json

with open('data/movies_ko.json', 'r', encoding='UTF-8') as file:
        movies_ko_data = json.load(file)

for movie_data in movies_ko_data:
    print(movie_data)
    print()


print("test")