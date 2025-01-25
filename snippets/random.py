data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "San Francisco"},
    {"name": "Eve", "age": 22, "city": "Boston"}
]

alice = next((person for person in data if person["name"] == "Alice"), None)
print(alice)

print(data[1])
print(data["alice"])