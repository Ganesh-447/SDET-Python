# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check for palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Count vowels/consonants
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

# 4. Remove duplicates from a string
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# 5. First non-repeating character
def first_non_repeating_char(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

# 6. Remove duplicates from a list
def remove_duplicates_list(lst):
    return list(dict.fromkeys(lst))

# 7. Common elements in two lists
def common_elements(l1, l2):
    return list(set(l1) & set(l2))

# 8. Sort list of dictionaries by key
def sort_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

# 9. Merge two dictionaries
def merge_dicts(d1, d2):
    return {**d1, **d2}

# 10. Frequency of elements
def element_frequency(lst):
    from collections import Counter
    return Counter(lst)

# 11. Read file and count lines/words
def file_line_word_count(filename):
    with open(filename) as f:
        lines = f.readlines()
        word_count = sum(len(line.split()) for line in lines)
    return len(lines), word_count

# 12. Longest line in file
def longest_line(filename):
    with open(filename) as f:
        return max(f, key=len)

# 13. Remove blank lines from file
def remove_blank_lines(filename):
    with open(filename) as f:
        lines = [line for line in f if line.strip()]
    with open(filename, 'w') as f:
        f.writelines(lines)

# 14. Class with attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# 15. Inheritance and overriding
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def greet(self):
        return f"Hi, I'm {self.name}, Employee ID: {self.emp_id}"

# 16. FizzBuzz
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# 17. Prime number check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 18. Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# 19. Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 20. Check anagram
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 21. API interaction (GET/POST)
import requests

def get_request(url):
    response = requests.get(url)
    return response.status_code, response.json()

def post_request(url, data):
    response = requests.post(url, json=data)
    return response.status_code, response.json()

# 22. Simple pytest test
# Save in test_sample.py
# def add(a, b):
#     return a + b
#
# def test_add():
#     assert add(2, 3) == 5

# 23. Pytest fixture
# import pytest
#
# @pytest.fixture
# def input_data():
#     return [1, 2, 3]
#
# def test_sum(input_data):
#     assert sum(input_data) == 6

# 24. Parametrize example
# @pytest.mark.parametrize("a,b,result", [(1, 2, 3), (3, 5, 8)])
# def test_add(a, b, result):
#     assert a + b == result
