from classes_531 import Rational


class Equations:
    def __init__(self, filename):
        assert isinstance(filename, str)
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r") as f:
            equations = []
            for line in f:
                eq = [n for n in line.split()]
                equations.append(eq)
        new_equations = []
        for eq in equations:
            new_eq = []
            for char in eq:
                if char not in "+-*":
                    try:
                        new_eq.append(Rational(char))
                    except ValueError:
                        new_eq.append(int(char))
                else:
                    new_eq.append(char)
            new_equations.append(new_eq)
        return new_equations

    @staticmethod
    def solve_simple(lst):
        tlst = tuple(lst)
        solution = tlst[0]
        try:
            for i in range(1, len(lst)+1):
                if str(lst[i]) == "+":
                    solution = solution + tlst[i+1]
                elif str(lst[i]) == "-":
                    solution = solution - tlst[i+1]
        except IndexError:
            pass
        return solution


    def solve_equations(self):
        solutions = []
        for eq in self.read_file():
            if eq:
                solution = Rational(1, 1)
                multiplicandum = []
                if '*' in str(eq):
                    small_eq = []
                    for el in eq:
                        if str(el) != "*":
                            small_eq.append(el)
                        else:
                            multiplicandum.append(small_eq[:])
                            small_eq.clear()
                    multiplicandum.append(small_eq)
                    for r in multiplicandum:
                        res = self.solve_simple(r)
                        solution *= res
                else:
                    solutions.append(self.solve_simple(eq))
                solutions.append(solution)
        return solutions


if __name__ == "__main__":
    e = Equations('input01.txt')

    # print(e.read_file())
    print(*e.solve_equations())

    # print(equations)
