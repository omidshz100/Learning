my_vehicle = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red",
    "engine": {
        "type": "V8",
        "horsepower": 300,
        "torque": 400
    },
    "features": ["air conditioning", "power windows", "navigation system"],
    "owner": {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
    },
    "mileage": 15000,
}
# Accessing values

my_vehivle2 = my_vehicle.copy()


my_vehivle2.pop("mileage")

print(my_vehivle2.keys(), "\n ---------------------")

for i, j  in my_vehivle2.items():
    print(i, ":", j)
