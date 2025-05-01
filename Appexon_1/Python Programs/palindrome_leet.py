# # def palindrome(string):
# #
# #     if string[::-1] == string:
# #         return True
# #     else:
# #         return False
# #
# # print(palindrome('122')
# #
#
# class Reverse:
#
#     def reverse(self,input):
#         n = len(input)
#         a = ""
#         for i in range(-1, -n - 1, -1):
#             a += (input[i])
#         return a
#     def palindrome(self,input):
#         reverse = self.reverse(input)
#         if reverse == input:
#             return True
#         else:
#             return False
# a = Reverse()
# print(a.palindrome('121'))
class Reverse:
    def reverse(self, input_str):
        n = len(input_str)
        reversed_str = ""
        for i in range(-1, -n - 1, -1):
            reversed_str += input_str[i]
        return reversed_str

class Palindrome(Reverse):  # Palindrome class inherits from Reverse
    def is_palindrome(self, input_str):
        reverse_str = self.reverse(input_str)  # Accessing reverse method from Reverse class
        if reverse_str == input_str:
            return True
        else:
            return False
input_str = "anku"

reverse_instance = Reverse()
reversed_str = reverse_instance.reverse(input_str)
print(reversed_str)  # Output: ukna

palindrome_instance = Palindrome()
is_palindrome = palindrome_instance.is_palindrome(input_str)
print(is_palindrome)  # Output: False
