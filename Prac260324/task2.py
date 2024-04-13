class ProtectedDictInt():
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        assert type(key) == int, "key must be an integer"
        assert key not in self, "key is already taken"
        # super().__setitem__(key, value)
        self.__dict[key] = value

    def __getitem__(self, item):
        return self.__dict[item]

    def __contains__(self, item):
        return item in self.__dict

    def __str__(self):
        return f"Protected Dictionary: {self.__dict}"

    def __len__(self):
        return len(self.__dict)

    def __add__(self, other):
        new_dict = ProtectedDictInt()
        for key, value in self.__dict.items():
            new_dict[key] = value

        if type(other) == tuple or type(other) == list: # kortezh
            assert str(bin(len(other)))[-1] == "1"
            for i in range(0, len(other), 2):
                new_dict[other[i]] = other[i+1]
        if type(other) == ProtectedDictInt or type(other) == dict:
            for key, value in other.__dict.items():
                new_dict[key] = value


        return new_dict







if __name__ == '__main__':
    d = ProtectedDictInt()
    k = ProtectedDictInt()
    k[52] = "KIki"
    d[23] = "Shalom" # d.__setitem__(23, "Hello")
    # d[23] = 32
    # d["Tel"] = "Hai"
    print(f"d[23] = {d[23]}") # d.__getitem__
    print(d)
    print(23 in d)
    print(d + {13: 54})
    print(len(d))