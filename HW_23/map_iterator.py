
def my_map(dict, func1, func2):
    return {func1(key): func2(value) for key, value in dict.items()}

first_dict = {'l': 1, 'm': 2, 's': 3}

second_dict = my_map(first_dict, str.upper, str)

print(second_dict)