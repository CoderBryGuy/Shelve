import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet orange citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in fruit:
#     print(f + "-" + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

fruit.close()



