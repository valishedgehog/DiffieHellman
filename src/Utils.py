class Utils:
    @staticmethod
    def fastModuloPow(num: int, pow: int, modulo: int) -> int:
        result = 1
        while pow:
            if pow % 2 == 0:
                num = (num ** 2) % modulo
                pow = pow // 2
            else:
                result = (num * result) % modulo
                pow -= 1
        return result
