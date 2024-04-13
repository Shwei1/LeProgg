class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        assert type(key) == int, "key must be an integer"
        assert key not in self, "key is already taken"
        super().__setitem__(key, value)
    pass

if __name__ == '__main__':
    d = ProtectedDictInt()
    # d = {}
    d[23] = "Shalom" # d.__setitem__(23, "Hello")
    # d[23] = 32
    # d["Tel"] = "Hai"
    d.update({"Shalom": "Goyim"}) # We can still utilise other methods which have not been rewritten, crap
    print(d)