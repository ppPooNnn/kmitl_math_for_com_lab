import random

numdeci = random.randrange(0, 127)
numbi = bin(numdeci)
code = [0] * 7
def create_hamming_code(num : str, code : list) :
    print(num)
    lenNum = len(num) - 1
    lenCode = len(code) - 1
    while lenNum >= 2 :
        code[lenCode] = int(num[lenNum])
        lenCode -= 1
        lenNum -= 1
    code.extend([0, 0])
    code.insert(3, 0)
    code.insert(7, 0)
    R1 = (code[8] + code[6] + code[4] + code[2] + code[0]) % 2
    code[10] = R1
    R2 = (code[8] + code[5] + code[4] + code[1] + code[0]) % 2
    code[9] = R2
    R3 = (code[6] + code[5] + code[4]) % 2
    code[7] = R3
    R4 = (code[2] + code[1] + code[0]) % 2
    code[3] = R4
    return code

def error_detec_and_correct(code : list) :
    check1 = (code[10] + code[8] + code[6] + code[4] + code[2] + code[0]) % 2
    check2 = (code[9] + code[8] + code[5] + code[4] + code[1] + code[0]) % 2
    check3 = (code[7] + code[6] + code[5] + code[4]) % 2
    check4 = (code[3] + code[2] + code[1] + code[0]) % 2
    sum_check = check1 + check2 + check3 + check4
    check = [check4,check3,check2,check1]
    print(check)
    if sum_check != 0 :
        len_check = len(check) - 1
        i = 0
        error_point = 0
        while len_check >= 0 :
            error_point += check[len_check] * pow(2, i)
            len_check -= 1
            i += 1
        print("error at point ",error_point)
        code[len(code) - error_point] = 1 if code[len(code) - error_point] % 2 == 0 else 0
    else :
        print("no error")
    return code

def main() :
    print(numdeci)
    hamming_code = create_hamming_code(numbi, code)
    print(hamming_code, "original data")
    corrupt_code = hamming_code
    corrupt_index = random.randrange(0, len(corrupt_code))
    corrupt_code[corrupt_index] = 1 if corrupt_code[corrupt_index] % 2 == 0 else 0 # 1
    print(corrupt_code, "corrupt data")
    fixed_code = error_detec_and_correct(corrupt_code)
    print(fixed_code, "after_fixed")

if __name__ == "__main__" :
    main()