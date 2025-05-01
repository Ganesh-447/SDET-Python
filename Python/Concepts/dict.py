# a={1:'a',2:'b',3:'c',4:'d'}
# b= {3:'x',5:'g',6:'f'}
#
#
# print(a|b) #union ,if same key's are having then the values with the last operand
# #key will be replaced, as here like b is the last, and variables won't change.
# print(a)
# a|=b   #updating.  the value of a to b. which means here. b dictinoary is added to a
# # and a value also changes.
# print(b)
# print(a)
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}

print(sorted(my_dict.values()))