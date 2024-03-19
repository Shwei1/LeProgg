class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def disc(self):
        return self.b ** 2 - 4 * self.a * self.c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c}")

    def solve(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "R"
                else:
                    return None
            else:
                return -self.c / self.b
        else:
            if QuadraticEquation.disc(self) < 0:
                return "No real solutions"
            elif QuadraticEquation.disc(self) == 0:
                return -self.b / (2 * self.a)
            else:
                return ((-self.b + QuadraticEquation.disc(self)**0.5) / (2 * self.a), (-self.b - QuadraticEquation.disc(self)**0.5) / (2 * self.a))




if __name__ == "__main__":
    a, b, c = (int(x) for x in input().split())
    eq = QuadraticEquation(a, b, c)
    print(eq.solve())
