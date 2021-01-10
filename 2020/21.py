from aocd import lines

allergens = {}
ingredients = {}
for line in lines:
    l_s = line.split(" (contains ")
    ing = l_s[0].split(" ")
    alg = l_s[1][:-1].split(", ")
    for a in alg:
        if a in allergens:
            allergens[a] &= set(ing)
        else:
            allergens[a] = set(ing)
    for i in ing:
        if i in ingredients:
            ingredients[i] += 1
        else:
            ingredients[i] = 1

identified = {}
while allergens:
    allergen, ingredient = min(allergens.items(), key=lambda x: len(x[1]))
    identified[allergen] = list(ingredient)[0]
    for other in allergens.values():
        other -= {identified[allergen]}
    del allergens[allergen]

print("Part 1:", sum(v for i, v in ingredients.items() if i not in identified.values()))
print("Part 2:", ",".join([identified[i] for i in sorted(identified)]))
