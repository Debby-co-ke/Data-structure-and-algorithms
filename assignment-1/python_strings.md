
# STRINGS
## Definition of a String

A **string** in Python is a sequence of characters enclosed in:

* Single quotes → `'hello'`
* Double quotes → `"hello"`
* Triple quotes → `'''hello'''` or `"""hello"""`

A string can contain:

* Letters (`a-z`, `A-Z`)
* Numbers (`0-9`)
* Symbols (`@, #, $, %`)
* Spaces

Example:

```python
name = "Deborah"
```
Strings are one of the most commonly used data types in programming because they allow us to store and work with **textual data** such as names, messages, passwords, and user input.

Strings are a **fundamental data type in Python** used to handle text data.
Understanding strings allows you to:

* Manipulate text easily
* Build applications
* Work with user input
* Implement algorithms like pattern matching

## Key Characteristics of Strings

### 1. Immutable (Cannot be Changed)

Once a string is created, it **cannot be modified directly**.

```python
s = "hello"
s[0] = "H"   # Error
```

Instead of modifying a string, Python creates a **new string** when changes are needed.


### 2. Indexed (Position-Based Access)

Each character has a position (index).

```python
s = "python"
print(s[0])   # p
```

Explanation:

* Indexing starts at **0**
* Negative indexing starts from the **end**


### 3. Ordered (Maintains Sequence)

Characters remain in the order they were entered.

```python
"abc" ≠ "cba"
```

Order matters when comparing strings or processing them.


### 4. Iterable (Can be Looped Through)

You can loop through each character.

```python
for char in "hello":
    print(char)
```

This allows operations like counting characters or searching.

## Indexing

Used to access individual characters.

```python
language = "python"

print(language[0])   # p
print(language[-1])  # n
```

---

## Slicing

Used to extract part of a string.

```python
language = "javascript"

print(language[0:4])   # java
print(language[::-1])  # reverse
```

Format:

```
[start : end : step]
```

---

## Length of a String

Returns number of characters.

```python
print(len("python"))  # 6
```

# String Operations (with Explanation)

### 1. Concatenation

Joins two or more strings together.

```python
a = "Deborah"
b = "Wangui"

print(a + " " + b)  # Deborah Wangui
```

### 2. Repetition

Repeats a string multiple times.

```python
print("hi" * 3)  # hihihi
```


### 3. Membership

Checks if a substring exists inside another string.

```python
print("H" in "Hello")  # True
```

---

### 4. Comparison

Compares strings alphabetically.

```python
print("abc" == "abc")  # True
print("abc" < "bcd")   # True
```

Comparison is based on **ASCII/Unicode values**.


# String Methods

### 1. upper(), lower(), capitalize()

Change the case of characters.

```python
s = "Hello"

print(s.upper())       # HELLO
print(s.lower())       # hello
print(s.capitalize())  # Hello
```


### 2. strip()

Removes spaces from the beginning and end.

```python
s = "   Hello   "

print(s.strip())  # Hello
```


### 3. replace()

Replaces part of a string with another value.

```python
s = "hello"

print(s.replace("l", "x"))  # hexxo
```

### 4. split()

Breaks a string into a list.

```python
s = "a,b,c"
print(s.split(","))  # ['a', 'b', 'c']
```


### 5. join()

Combines a list into a string.

```python
letters = ['a', 'b', 'c']
print("-".join(letters))  # a-b-c
```


### 6. String Formatting

Used to insert variables into strings.

#### f-string

```python
name = "Deborah"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

#### format()

```python
print("My name is {} and I am {}".format(name, age))
```


# Built-in Functions

```python
s = "hello"

len(s)        # length
max(s)        # highest character
min(s)        # lowest character
sorted(s)     # sorted list
```

#Operators

| Operator | Description   |
| -------- | ------------- |
| `+`      | Concatenation |
| `*`      | Repetition    |
| `in`     | Membership    |
| `==`     | Equality      |


# STRING PATTERN MATCHING

## 1. What is String Pattern Matching?

String pattern matching is the process of **searching for a specific pattern (substring)** inside a larger string.

Example:

* Text: `"hello world"`
* Pattern: `"world"`

The goal is to find **where the pattern appears** in the text.

Used in:

* Search engines
* Text editors
* Data validation
* Cybersecurity


## Types of Pattern Matching Algorithms


### 1. Naive Pattern Matching

Definition:
This is the **simplest method**. It checks every possible position in the string.

How it works:

* Move one character at a time
* Compare substring with pattern

```python
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            print("Pattern found at index", i)
```

Advantage:

* Easy to understand

Disadvantage:

* Slow for large data


### 2. KMP Algorithm (Knuth-Morris-Pratt)

An **efficient algorithm** that avoids repeating comparisons.

How it works:

* Uses a helper array called **LPS (Longest Prefix Suffix)**
* Skips unnecessary comparisons

Advantage:

* Faster than naive

Used in:

* Text editors
* Search systems


### 3. Rabin-Karp Algorithm

Description:
Uses **hashing** to find patterns.

 How it works:

* Converts strings into numbers (hash values)
* Compares hash instead of characters

 Advantage:

* Fast for multiple pattern searches

 Disadvantage:

* Possible hash collisio

### 4. Regular Expressions (Regex)

Description:
A powerful way to search patterns using special symbols.

```python
import re

text = "My number is 12345"
pattern = r"\d+"

match = re.search(pattern, text)
print(match.group())  # 12345
```


* `\d+` → finds numbers
* `re.search()` → searches the text


### Common Regex Patterns

| Pattern | Meaning       |
| ------- | ------------- |
| `\d`    | digit         |
| `\w`    | word          |
| `.`     | any character |
| `^`     | start         |
| `$`     | end           |
