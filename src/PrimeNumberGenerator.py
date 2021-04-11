from random import randrange, getrandbits, randint
from math import ceil, sqrt
from .Utils import Utils


class PrimeNumberGenerator:
    def __init__(self, length=None, tests_count=None):
        self.tests_count = 100 if tests_count is None else tests_count
        self.length = 1024 if length is None else length

    def millerRobinTest(self, number: int, tests_count: int) -> bool:
        if number == 2 or number == 3:
            return True
        if number <= 1 or number % 2 == 0:
            return False

        s = 0
        r = number - 1
        while r & 1 == 0:
            s += 1
            r //= 2

        for _ in range(tests_count):
            a = randint(2, number - 1)
            x = pow(a, r, number)
            if x != 1 and x != number - 1:
                j = 1
                while j < s and x != number - 1:
                    x = pow(x, 2, number)
                    if x == 1:
                        return False
                    j += 1
                if x != number - 1:
                    return False

        return True

    def isPrime(self, number: int) -> bool:
        return self.millerRobinTest(number, self.tests_count)

    def generatePrimeCandidate(self):
        number = getrandbits(self.length)
        number |= (1 << self.length - 1) | 1
        return number

    def getPrime(self):
        prime = None
        while prime is None or not self.isPrime(prime):
            prime = self.generatePrimeCandidate()
        return prime

    def getSophiePrime(self) -> int:
        n = self.getPrime()
        while not self.isPrime(2 * n + 1):
            n = self.getPrime()
        return 2 * n + 1

    def primeFactorization(self, p: int) -> list:
        factor = []
        while p % 2 == 0:
            if not (2 in factor):
                factor.append(2)
            p = p / 2
        
        if self.isPrime(int(p)):
            factor.append(int(p))
            return factor

        for i in range(3, ceil(sqrt(p)), 2):
            needCheck = False
            while p % i == 0:
                if not (i in factor):
                    factor.append(i)
                    needCheck = True
                p = p / i

            if needCheck and self.isPrime(int(p)):
                factor.append(int(p))
                return factor

        return factor

    def getPrimitiveRootModulo(self, p: int) -> int:
        s = p - 1
        factor = self.primeFactorization(s)
        powers = map(lambda i: s / i, factor)

        for g in range(3, ceil(sqrt(p))):
            isRoot = True
            for power in powers:
                if Utils.fastModuloPow(g, power, p) == 1:
                    isRoot = False
            
            if isRoot:
                return g
