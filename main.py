import random


def gen_pq():
    prime_array = []
    for i in range(99000, 99999):
        if i == 0 or i == 1:
            continue
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            if i % 4 == 3:
                prime_array.append(i)
    return prime_array


def gen_N():
    while True:
        num1 = random.choice(gen_pq())
        num2 = random.choice(gen_pq())
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
    for i in range(15):
        result_x += (bits[i]) ** 2
    result_x = (result_x * (16 / 5000)) - 5000

    print(result_x)
    if 2.16 < result_x < 46.17:
        print("bits : " + str(bits))
        print("Test 4 passed.\n")
        return True
    else:
        print("Test 4 failed.\n")
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
        print("Test 3 failed.\n")
        return False
    else:
        print("\nMax consecutive 1s: " + str(max_len_1))
        print("Max consecutive 0s: " + str(max_len_0))
        print("Test 3 passed.\n")
        return True


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
        print("Consecutive 1s - 1 :" + str(num_len1))
        print("Consecutive 1s - 2 :" + str(num_len2))
        print("Consecutive 1s - 3 :" + str(num_len3))
        print("Consecutive 1s - 4 :" + str(num_len4))
        print("Consecutive 1s - 5 :" + str(num_len5))
        print("Consecutive 1s - 6+ :" + str(num_len_rest))
        print("Test 2 passed.\n")
        return True
    else:
        print("Test 2 failed.\n")
        return False


def test_1(bit_number):
    if 9725 < bit_number.count('1') < 10275:
        print("Number of 1s: " + str(bit_number.count('1')))
        print("Test 1 passed.\n")
        return True
    else:
        print("Test 1 failed.\n")
        return False


def tests():
    if test_4(bit_num):
        if test_1(bit_num) and test_2(bit_num) and test_3(bit_num):
            return True
    return False


if __name__ == '__main__':
    gen_n = gen_N()
    seed = random.randint(1, 1 * 10 ** 10)
    bit_num = gen_bit(seed, gen_n)

    test_1(bit_num)
    test_2(bit_num)
    test_3(bit_num)
    test_4(bit_num)

    # while True:
    #    gen_n = gen_N()
    #    seed = random.randint(1, 1 * 10 ** 10)
    #    bit_num = gen_bit(seed, gen_n)
    #    if tests():
    #        break

    print("generated N: " + str(gen_n))
    print("generated first X: " + str(seed))
    print("generated key: " + bit_num + "\n")
