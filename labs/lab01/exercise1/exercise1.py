def is_budget_sufficient(one_way_km,budget):
    round_trip = one_way_km * 2
    liter = round_trip / 10
    cost = liter * 2.00
    return budget >= cost

print(is_budget_sufficient(100, 40)) # True
print(is_budget_sufficient(100, 39)) # False

