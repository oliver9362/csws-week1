cities = ['London', 'New York', 'Montreal', 'Paris', 'Berlin', 'Moscow', 'Beijing']
print(cities)
print("There are ", +len(cities), "in the list")
cities.append('Mexico City')
print(cities)
cities.insert(1, 'Quebec')
del cities[4]
cities.remove('Moscow')
X = cities.pop(2)
print(X)
print(cities)