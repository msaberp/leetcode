def farey(n):
    list_of_fractions = get_farey_fractions(n)
    list_of_fractions.sort()
    return [str(fraction) for fraction in list_of_fractions]


def get_farey_fractions(n):
    fractions = []
    for denom in range(1, n + 1):
        for nom in range(denom + 1):
            fraction = Fraction(nom, denom)
            if not fraction in fractions:
                fractions.append(fraction)
    return fractions


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return abs(x)


class Fraction:
    nominator: int
    denominator: int

    def __init__(self, nom, denom):
        self.nominator = nom
        self.denominator = denom
        self.simplify()

    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)

    def simplify(self):
        common_factor = gcd(self.nominator, self.denominator)
        self.nominator //= common_factor
        self.denominator //= common_factor

    def __eq__(self, other):
        if self.denominator == other.denominator:
            return self.nominator == other.nominator
        return self.nominator * other.denominator == other.nominator * self.denominator

    def __lt__(self, other):
        if self.denominator == other.denominator:
            return self.nominator < other.nominator
        return self.nominator * other.denominator < other.nominator * self.denominator

    def __gt__(self, other):
        if self.denominator == other.denominator:
            return self.nominator > other.nominator
        return self.nominator * other.denominator > other.nominator * self.denominator


farey_fractions = farey(5)
print(farey_fractions)