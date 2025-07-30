print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Python - Slicing Strings *******
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

# Output: llo


# Slice From the Start *****
# By leaving out the start index, the range will start at the first character:

# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Output: Hello