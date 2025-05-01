products = [{"name" :"HP", "laptop":"123", "price": 2000},
            {"name":"apple", "laptop": "222","price":3000},
            {"name":'Headphone',"price":102},
            {"name":'USB',"price":134}]

print(type(products))
print(type(products[1]))

def is_affordable(item):
    return item["price"] < 500

def is_affordable_name(items):
    return len(items["name"]) > 3


a= list(filter(is_affordable,products))
print(a)
print(a[0]["price"])

c = list(filter(is_affordable_name,products))
for i in c:
    print(i)

b= list(map(is_affordable,products))
print(b)