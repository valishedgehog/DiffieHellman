from src.DiffieHellman import DiffieHellman
import time

NUMBER_BIT_SIZE = 256

def main():
    start_time = time.time()
    FirstUser = DiffieHellman(NUMBER_BIT_SIZE)
    SecondUser = DiffieHellman(NUMBER_BIT_SIZE)
    FirstUser.requestHandshake(SecondUser)

    print("Private FirstUser key:  {}".format(FirstUser.pk))
    print("Private SecondUser key: {}".format(SecondUser.pk))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()