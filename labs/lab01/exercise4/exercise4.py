def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
         price = 2.00
    elif vehicle_type == "Hybrid":
        if hour >= 0 and hour <= 6 or hour >= 22 and hour <= 23:
            price = 2.00
        else:
            price = 5.00
    else:
        price = 5.00

    return price

print(get_hourly_rate("Electric", 5)) # 2.00
print(get_hourly_rate("Electric", 7)) # 5.00
