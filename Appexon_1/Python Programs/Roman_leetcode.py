# def romantoint(str):
#     roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     prev_val = 0
#     total = 0
#     for i in str:
#         value = roman_values[i]
#         if value > prev_val:
#             total += value - 2*prev_val
#         else:
#             total += value
#         prev_val = value
#
#     print(total)
#
# romantoint('MCM')



# def romantoint(str):
#      roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#      prev_val = 0
#      result = 0
#      for i in str:
#          value = roman_values[i]
#          if value > prev_val:
#              result += value - 2*prev_val
#          else:
#              result += value
#
#          prev_val = value
#      print(result)
# romantoint('XX')

# def romantoint(str):
#     roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     pre_val = 0
#     result = 0
#     for i in str:
#         value = roman_values[i]
#
#         if value > pre_val:
#             result += value - 2*pre_val
#         else:
#             result += value
#         pre_val = value
#     print(result)
#
# romantoint('XIX')


def roman(str):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    pre_value = 0
    result = 0
    for i in str:
        value = roman_values[i]

        if value > pre_value:
            result += value - 2*pre_value
        else:
            result += value
        pre_value = value
    print(result)

roman("XXX")
































