import random
from math import sqrt


def gen_pq():
    prime_array = []
    for i in range(10000, 99999):
        for x in range(2, int(sqrt(i)) + 1):
            if i % x == 0:
                break
        else:
            if i % 4 == 3:
                prime_array.append(i)
    return prime_array


def gen_N():
    while True:
        primes = gen_pq()
        num1 = random.choice(primes)
        num2 = random.choice(primes)
        if num1 != num2:
            return num1 * num2


def gen_bit(x, N):
    bit_output = ""
    for i in range(20000):
        x = x * x % N
        b = x % 2
        bit_output += str(b)
    return bit_output


def test_4(bit_number):
    bits = [0] * 16
    for i in range(5000):
        if bit_number[i * 4:i * 4 + 4] == '0000':
            bits[0] += 1
        if bit_number[i * 4:i * 4 + 4] == '0001':
            bits[1] += 1
        if bit_number[i * 4:i * 4 + 4] == '0010':
            bits[2] += 1
        if bit_number[i * 4:i * 4 + 4] == '0011':
            bits[3] += 1
        if bit_number[i * 4:i * 4 + 4] == '0100':
            bits[4] += 1
        if bit_number[i * 4:i * 4 + 4] == '0101':
            bits[5] += 1
        if bit_number[i * 4:i * 4 + 4] == '0110':
            bits[6] += 1
        if bit_number[i * 4:i * 4 + 4] == '0111':
            bits[7] += 1
        if bit_number[i * 4:i * 4 + 4] == '1000':
            bits[8] += 1
        if bit_number[i * 4:i * 4 + 4] == '1001':
            bits[9] += 1
        if bit_number[i * 4:i * 4 + 4] == '1010':
            bits[10] += 1
        if bit_number[i * 4:i * 4 + 4] == '1011':
            bits[11] += 1
        if bit_number[i * 4:i * 4 + 4] == '1100':
            bits[12] += 1
        if bit_number[i * 4:i * 4 + 4] == '1101':
            bits[13] += 1
        if bit_number[i * 4:i * 4 + 4] == '1110':
            bits[14] += 1
        if bit_number[i * 4:i * 4 + 4] == '1111':
            bits[15] += 1

    result_x = 0
    for i in range(16):
        result_x += (bits[i]) ** 2
    result_x = (result_x * (16 / 5000)) - 5000

    if 2.16 < result_x < 46.17:
        return True, result_x, bits
    else:
        return False


def test_3(bit_number):
    num_len = 0
    max_len_1 = 0

    for i in range(len(bit_number)):
        if bit_number[i] == '1':
            num_len += 1
        else:
            if num_len > max_len_1:
                max_len_1 = num_len
            num_len = 0

    num_len = 0
    max_len_0 = 0

    for i in range(len(bit_number)):
        if bit_number[i] == '0':
            num_len += 1
        else:
            if num_len > max_len_0:
                max_len_0 = num_len
            num_len = 0

    if max_len_1 > 25 or max_len_0 > 25:
        return False
    else:
        return True, max_len_0, max_len_1


def test_2(bit_number):
    num_len = 0
    str_len = ""
    test = False
    for i in range(len(bit_number)):
        if bit_number[i] == '1':
            num_len += 1
        else:
            str_len += str(num_len)
            num_len = 0
    str_len = str_len.replace("0", "")

    num_len1 = str_len.count('1')
    num_len2 = str_len.count('2')
    num_len3 = str_len.count('3')
    num_len4 = str_len.count('4')
    num_len5 = str_len.count('5')
    num_len_rest = len(str_len) - num_len1 - num_len2 - num_len3 - num_len4 - num_len5

    if 2315 < num_len1 < 2685:
        if 1114 < num_len2 < 1386:
            if 527 < num_len3 < 723:
                if 240 < num_len4 < 384:
                    if 103 < num_len5 < 209:
                        if 103 < num_len_rest < 209:
                            test = True
    if test:
        return True, num_len1, num_len2, num_len3, num_len4, num_len5, num_len_rest
    else:
        return False


def test_1(bit_number):
    if 9725 < bit_number.count('1') < 10275:
        return True, bit_number.count('1')
    else:
        return False


if __name__ == '__main__':

    counter = 0
    while True:
        counter += 1
        print(counter)
        gen_n = gen_N()
        seed = random.randint(1, 1 * 10 ** 10)
        bit_num = gen_bit(seed, gen_n)

        passed4 = test_4(bit_num)
        if not passed4:
            continue
        passed3 = test_3(bit_num)
        if not passed3:
            continue
        passed2 = test_2(bit_num)
        if not passed2:
            continue
        passed1 = test_1(bit_num)

        if passed1 and passed2 and passed3 and passed4:
            print("\nTest 1 passed.")
            print("Number of 1s: " + str(passed1[1]) + "\n")

            print("Test 2 passed.")
            print("Consecutive 1s - 1: " + str(passed2[1]))
            print("Consecutive 1s - 2: " + str(passed2[2]))
            print("Consecutive 1s - 3: " + str(passed2[3]))
            print("Consecutive 1s - 4: " + str(passed2[4]))
            print("Consecutive 1s - 5: " + str(passed2[5]))
            print("Consecutive 1s - 6+: " + str(passed2[6]) + "\n")

            print("Test 3 passed.")
            print("Max consecutive 1s: " + str(passed3[1]))
            print("Max consecutive 0s: " + str(passed3[2]) + "\n")

            print("Test 4 passed.")
            print("X : " + str(passed4[1]))
            print("bits (0:15) : " + str(passed4[2]) + "\n")

            print("counter: " + str(counter))
            print("generated N: " + str(gen_n))
            print("generated first X: " + str(seed))
            print("generated key: " + bit_num)
            break





