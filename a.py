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

#                                                 Python - Slicing Strings *******
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

# Output: llo


#                                                Slice From the Start *****
# By leaving out the start index, the range will start at the first character:

# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Output: Hello

#                                                           Slice To the End
# By leaving out the end index, the range will go to the end:

Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#Output: llo, World!


#                                                   Negative Indexing ********
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])
#Output: orl

 
#                                                   Upper Case **********
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# Output: HELLO, WORLD!

#                                                      Lower Case *******
# Example
# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
# Output: hello, world!


#                                                Remove Whitespace *****
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) 

# returns Hello, World!


#                                                      Replace String
# Example
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#  Jello, World!



#                                                Split String *****
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) 

# returns ['Hello', ' World!']


#                                           String Concatenation ***********


# To concatenate, or combine, two strings you can use the + operator.

# ExampleGet your own Python Server
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)



# Example
# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)