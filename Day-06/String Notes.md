                  Day 5 – Strings in Python 

gbvn krvw rdgq ppyz
amanibathini28@gmail.com
___________________________________________________________________

 What is a String?
 __________________________________

A string is a collection (sequence) of characters enclosed in:

* Single quotes `' '`
* Double quotes `" "`
* Triple quotes `''' '''` or `""" """` (used for multi-line strings)

Examples:
`  name = "Amani"
   city = 'Hyderabad'
   paragraph = """Python
   is easy"""

### Remember

* String = Sequence of characters
* Every character has an index.
* Strings are immutable (cannot be modified after creation). 

 Characteristics of Strings
___________________________________

✔ Ordered

✔ Immutable

✔ Supports Indexing

✔ Supports Slicing

✔ Allows duplicate characters

✔ Can contain letters, numbers, symbols and spaces

Example:
  text = "Python123!"

## String Operations
__________________________________

# A. Concatenation (+)

Used to join two or more strings.

first = "Hello"
second = "World"
print(first + " " + second)
Output:
Hello World

Real-life Example:
Joining First Name + Last Name

# B. Repetition (*)

Repeats the string multiple times.

print("Hi " * 3)
Output:
Hi Hi Hi

Real-life Example

Printing stars in patterns.

## C. Indexing

Used to access one character.

Positive Index
P y t h o n
0 1 2 3 4 5

Negative Index
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1

Example:
text = "Python"
print(text[0])
print(text[-1])

Output
P
n

## D. Slicing

Extracts part of a string.
Syntax:
string[start:stop:step]

Examples:
text = "Python"
print(text[0:3])
print(text[:4])
print(text[2:])

Output:
Pyt
Pyth
thon

## E. Membership Operators

Checks whether a substring exists.

text = "Python"
print("Py" in text)
print("Java" not in text)
Output:
True
True

# Built-in Functions
_____________________________

## len()
Returns total characters.

len("Python")
Output:
6

## max()
Returns character with highest ASCII value.

max("abcXYZ")
Output:
c

## min()
Returns smallest ASCII value.

min("abcXYZ")
Output:
X

## sorted()
Returns characters in sorted order.

sorted("python")
Output:
['h','n','o','p','t','y']

## ord()
Character → ASCII value

ord('A')
Output:
65

## chr()
ASCII → Character

chr(97)
Output`
a

# String Methods
______________________________________

# A. Case Conversion

| Method       | Purpose                              |
| ------------ | ------------------------------------ |
| upper()      | Converts to uppercase                |
| lower()      | Converts to lowercase                |
| capitalize() | First letter uppercase               |
| title()      | First letter of every word uppercase |
| swapcase()   | Upper ↔ Lower                        |
| casefold()   | Strong lowercase conversion          |

# B. Alignment & Formatting

| Method   | Purpose            |
| -------- | ------------------ |
| center() | Centers text       |
| ljust()  | Left align         |
| rjust()  | Right align        |
| zfill()  | Adds leading zeros |

# C. Search Methods

| Method   | Purpose                                       |
| -------- | --------------------------------------------- |
| find()   | Returns index or -1                           |
| rfind()  | Searches from right                           |
| index()  | Like find(), but raises an error if not found |
| rindex() | Right search with error                       |
| count()  | Counts occurrences                            |

**Important Interview Question**

### Difference between `find()` and `index()`

| find()                  | index()                          |
| ----------------------- | -------------------------------- |
| Returns -1 if not found | Raises `ValueError` if not found |

## D. Testing Methods

Used to check string properties. They return **True** or **False**.

Examples:

* `isalpha()`
* `isalnum()`
* `islower()`
* `isupper()`
* `isspace()`
* `istitle()`
* `isidentifier()`
* `isdecimal()`
* `isdigit()`
* `isnumeric()`

**Easy Memory**

All methods starting with **is** return a Boolean value.

**Difference to Remember**

* `isdecimal()` → Only decimal digits
* `isdigit()` → Digits + superscripts
* `isnumeric()` → Digits, fractions, Roman numerals, etc. 

## E. Replace & Modify

| Method      | Purpose                          |
| ----------- | -------------------------------- |
| replace()   | Replaces old text with new       |
| translate() | Replaces using translation table |
| maketrans() | Creates translation table        |

## F. Split & Join

| Method       | Purpose                                |
| ------------ | -------------------------------------- |
| split()      | Splits into a list                     |
| rsplit()     | Splits from the right                  |
| splitlines() | Splits by new lines                    |
| join()       | Joins iterable elements                |
| partition()  | Splits into 3 parts at first separator |
| rpartition() | Splits into 3 parts at last separator  |

**Real-life Example**

CSV data:
"John,25,Hyderabad".split(",")

## G. Strip Methods

| Method   | Purpose                        |
| -------- | ------------------------------ |
| strip()  | Removes spaces from both sides |
| lstrip() | Removes left spaces            |
| rstrip() | Removes right spaces           |

## H. Encoding & Decoding

* `encode()` → String ➜ Bytes
* `decode()` → Bytes ➜ String

Used when working with files, APIs, networking, or data transmission. 
