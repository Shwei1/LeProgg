

class Rational:
    def __init__(self, n, d=1):
        assert d != 0
        if isinstance(n, int) and isinstance(d, int):
            self.d = d
            self.n = n
        if isinstance(n, str):
            if "/" in n:
                for i in range(len(n)):
                    if n[i] == '/':
                        try:
                            self.d = int(n[i + 1:])
                            self.n = int(n[0:i])
                        except ValueError:
                            raise ValueError("Abnormal input: use a single slash between the"
                                             " nominator and the denominator.")
            else:
                try:
                    self.n = int(n)
                    self.d = d
                except ValueError:
                    raise ValueError("Abnormal input")

    @staticmethod
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        gcd = Rational.gcd(a, b)
        lcm = (a*b)//gcd
        return lcm

    def reduce(self):
        gcd = self.gcd(self.n, self.d)
        self.n = self.n // gcd
        self.d = self.d // gcd
        return Rational(self.n, self.d)

    def __eq__(self, other):
        if isinstance(other, Rational):
            self.reduce()
            other.reduce()
            if self.d == other.d and self.n == other.n:
                return True
            return False
        else:
            raise ValueError("Abnormal input: the other number not of class Rational")

    def __add__(self, other):
        try:
            if isinstance(other, Rational):
                self.n = self.n * other.d + other.n * self.d
                self.d = self.d * other.d
                return Rational(self.n, self.d) .reduce()

            elif isinstance(other, int):
                self.n = self.n + other * self.d
                self.d = self.d
                return Rational(self.n, self.d).reduce()
        except TypeError:
            raise ValueError("Abnormal input: no operation for the operation for such object to class Rational")

    def __sub__(self, other):
        try:
            if isinstance(other, Rational):
                self.n = self.n * other.d - other.n * self.d
                self.d = self.d * other.d
                return Rational(self.n, self.d).reduce()
            elif isinstance(other, int):
                self.n = self.n + other * self.d
                self.d = self.d
                return Rational(self.n, self.d).reduce()
        except TypeError:
            raise ValueError("Abnormal input: no operation for the operation for such object to class Rational")

    def __mul__(self, other):
        self.n = self.n * other.n
        self.d = self.d * other.d
        return Rational(self.n, self.d).reduce()

    def __str__(self):
        return f"{self.n}/{self.d}"


# if __name__ == "__main__":
#     r1 = Rational(1, 3)
#     r2 = Rational(1, 2)
#     r3 = r2 - r1
#     print(r3)
#     print(r1 < r2)