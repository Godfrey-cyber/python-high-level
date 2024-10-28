a = "Python is cool"
print(a[7:])

a = "Python is cool"
print(a[0:6])

a = "Python is cool"
print(a,a,a); 

print(a[-2])

name = 'Godfrey'

greetings = "Good morning"

print(f"{greetings}, Welcome again, {name}")
school = "Holberton"
print(f"{school} school")

print(f"{98} Battery street")

str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"\nWelcome to {str1}!\n")

str1 = "Holberton"
str2 = "School"
str1 = f"{str1} {str2}"
print(f"Welcome to {str1}!")

print('\n')
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[7:]
middle_word = word[1:8]
print(word_first_3)
print(word_last_2)
print(middle_word)

for i in range(97, 123):
    print('{:c}'.format(i), end='')


#!/usr/bin/python3
print("\n")
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
print("\n")
#!/usr/bin/python3
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i not in ['e', 'q']:
        print(i, end="")
#!/usr/bin/python3
for i in range(0, 99):
    print('{} = 0x{:x}'.format(i, i))

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
#!/usr/bin/python3
def is_lowercase(char):
    if 97 <= char <= 122:
        return True
    return False

#!/usr/bin/python3
def is_lowercase(char):
    if 97 <= char <= 122:
        return True
    return False

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))