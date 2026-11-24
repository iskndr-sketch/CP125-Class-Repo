def validate_entry(name, pin):
    if name == "Director" and pin == 1122:
        return True
    elif name == "Security" and pin == 9900:
        return True
    else:
        return False


print(validate_entry("Director", "1122")) # True
print(validate_entry("security", "9900")) # True

