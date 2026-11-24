import math
def calculate_tent_cost(participants,tent_capacity,tent_price):
    num_tents = participants / tent_capacity
    num_tents = math.ceil(num_tents)
    cost = num_tents * tent_price
    return cost

print(calculate_tent_cost(12, 4, 100)) # 300
print(calculate_tent_cost(13, 4, 100)) # 400
