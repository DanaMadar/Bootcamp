# #ex1
# values = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionary = dict(zip(values, values))
# print(dictionary)

#ex2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# price = 0
# cost = 0

# for name, age in family.items():
#     age = int(age)

#     if age < 3:
#         cost = 0
#         price += 0
#     elif age < 12:
#         cost = 10
#         price += 10
#     else:
#         cost = 15
#         price += 15
#     print(f"each members {name} cost is {cost}")
# print("the familiys total cost is ", price)


#ex3
# brand = {
#     "name": "Zara", 
#     "creation_date": "1975", 
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue", 
#         "Spain": "red", 
#         "US": ["pink", "green"]
#     }
# }

# brand["number_stores"] = 2
# print(brand["number_stores"])
# print("Zaras clients are", brand["type_of_clothes"])
# brand["country_creation"] = "Spain"
# "international_competitors" in brand
# print(True)
# brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# for values in brand.values():
#     print(values)

# more_on_zara = {
#     "creation_date": "1975", 
#     "number_stores": 10000
#     }
# brand.update(more_on_zara)
# print(brand["number_stores"])

#ex4
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
d = {}
d1 = {}
d2 = {}
d3 = {}
d4 = {}

for keys, values in enumerate(users):
    d[values] = keys  

for values, keys in enumerate(users):
    d1[values] = keys  

for keys, values in enumerate(sorted(users)):
    d2[values] = keys  


for values, keys in enumerate(users):
    if "i" in keys:
        d3[values] = keys  


for values, keys in enumerate(d1):
    if keys.startswith("M"):
        d4[values] = keys  
    if keys.startswith("P"):
        d4[values] = keys  
print(d4)