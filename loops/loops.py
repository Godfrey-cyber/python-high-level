fruits = ["apple", "banana", "cherry", "kiwi", "oranges", "lemons"]

for fruit in fruits:
    print("-", fruit)

for i in range(5):
    print("-", i)

# while
count = 0

while count <= 5:
    print(count)
    count += 1

for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

for i in range(4):
    print(i, end=" ")

for i in range(2, 4):
    print(i, end=" ")

print("\n")
for i in range(2, 10, 2):
    print(i, end=" ")
print('\n\n')
for i in range(0, 3):
    print(i, end=" ")
print("------4-------")
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print(a.get('projects')[3])

print("\n")
for i in range(1, 4):
    print(i, end=" ")
print("\n")
for i in [1, 3, 4, 2]:
    print(i, end=" ")

print("\n")
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print(a.get('projects'))


a = { 'id': 89, 'name': "John" }
print(a['id'])
for i in [1, 2, 3, 4]:
     print(i, end=" ")


a = { 'id': 89, 'name': "John" }
print(a.get('age'))


a = { 'id': 89, 'name': "John" }
print(a.get('id'))


for i in range(0, 3):
    print(i, end=" ")
print("\n")
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
print(a.get('projects')[3])

for i in range(1, 4):
    print(i, end=" ")
print("\n")
for i in [1, 3, 4, 2]:
    print(i, end=" ")

for i in ["Hello", "Holberton", "School", 98]:
    print(i, end=" ")

a = { 'id': 89, 'name': "John" }
print(a.get('age', 0))