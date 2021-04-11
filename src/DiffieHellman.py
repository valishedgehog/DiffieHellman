from random import randint

from src.PrimeNumberGenerator import PrimeNumberGenerator
from src.Utils import Utils

class DiffieHellman:
    def __init__(self, number_length):
        self.png = PrimeNumberGenerator(number_length)
        self.generated_secret_key = self.png.getPrime()

    def requestHandshake(self, user) -> None:
        self.p = self.png.getSophiePrime()
        self.g = self.png.getPrimitiveRootModulo(self.p) # always can use 2
        self.open_key = Utils.fastModuloPow(self.g, self.generated_secret_key, self.p)
        self.user_ok = user.responseHandshake(self.p, self.g, self.open_key)
        self.pk = Utils.fastModuloPow(self.user_ok, self.generated_secret_key, self.p)

    def responseHandshake(self, p: int, g: int, open_key: int) -> int:
        self.p, self.g, self.user_ok = p, g, open_key
        self.pk = Utils.fastModuloPow(open_key, self.generated_secret_key, p)
        self.open_key = Utils.fastModuloPow(self.g, self.generated_secret_key, self.p)
        return self.open_key
