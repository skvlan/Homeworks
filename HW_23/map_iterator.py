class CustomMapIterator:
    def __init__(self, dict_obj, func1, func2):
        self.dict_obj = dict_obj
        self.func1 = func1
        self.func2 = func2
        self.keys_iterator = iter(dict_obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            key = next(self.keys_iterator)
            transformed_key = self.func1(key)
            transformed_value = self.func2(self.dict_obj[key])
            return (transformed_key, transformed_value)
        except StopIteration:
            raise StopIteration

first_dict = {'l': 1, 'm': 2, 's': 3}

iterator = CustomMapIterator(first_dict, str.upper, str)

for item in iterator:
    print(item)