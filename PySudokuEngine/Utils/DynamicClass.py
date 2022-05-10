class DynamicClass:
    def __init__(self, dict = {}):
        for key, value in dict.items():
            if type(value)==type({}):
                dict[key] = DynamicClass(value)

        self.__dict__.update(dict)