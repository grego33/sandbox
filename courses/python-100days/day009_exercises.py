
car_models = {
    "Toyota": "Camry",
    "Honda": "Civic",
    "Ford": "Mustang",
    "Chevrolet": "Malibu",
    "Nissan": "Altima"
}

for make in car_models:
    print(make)

for make in car_models.keys():
    print(make)

for model in car_models.values():
    print(model)


# You can mix key types in a dict
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict[1] = "d"
print(dict)