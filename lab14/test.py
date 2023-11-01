import random as rd 
ErrorCorrection = []

n = 127
data = rd.randrange(1,n+1)
def num_Tobi(data):
    binary = bin(data)[2:]
    binary = binary.zfill(7)
    return binary

binary_number = num_Tobi(data)

def insert_arr(binary_number):
    for bit in (binary_number):
        ErrorCorrection.append(int(bit))
    return ErrorCorrection

arr_bit = insert_arr(binary_number)
def ham(arr_bit):
    arr_bit.extend([0, 0])
    arr_bit.insert(3,0)
    arr_bit.insert(7,0)
    R1 = (arr_bit[8] +arr_bit[6] +arr_bit[4] + arr_bit[2] + arr_bit[0]) % 2
    arr_bit[10] = R1
    R2 = (arr_bit[8] + arr_bit[5] + arr_bit[4] + arr_bit[1] + arr_bit[0]) % 2
    arr_bit[9] = R2
    R3 = (arr_bit[6] + arr_bit[5] +arr_bit[4]) % 2
    arr_bit[7] = R3
    R4 = (arr_bit[2] + arr_bit[1] + arr_bit[0]) % 2
    arr_bit[3] = R4
    return arr_bit

# hamming = ham(arr_bit)
# print(hamming)
def check_error(arr_bit):
    c1 = ( arr_bit[10] + arr_bit[8] + arr_bit[6] + arr_bit[4] + arr_bit[2] + arr_bit[0]) % 2
    c2 = ( arr_bit[9] +  arr_bit[8] +  arr_bit[5] +  arr_bit[4] +  arr_bit[1] +  arr_bit[0]) % 2
    c3 = ( arr_bit[7] +  arr_bit[6] +  arr_bit[5] +  arr_bit[4]) % 2
    c4 = ( arr_bit[3] +  arr_bit[2] +  arr_bit[1] + arr_bit[0]) % 2
    # sum_c = c1+c2+c3+c4
    check_bit = [c4,c3,c2,c1]
    print(check_bit)

    LenCheck = len(check_bit) - 1
    a = 0
    position_error = 0
    while  LenCheck >= 0 :
        position_error += check_bit[LenCheck] * pow(2, a)
        LenCheck -= 1
        a += 1
    print("error point", position_error  )
    arr_bit[len(arr_bit) - position_error] = 1 if arr_bit[len(arr_bit) - position_error] % 2 == 0 else 0
    return arr_bit


def main():
     hamming = ham(arr_bit) #original
     print(hamming)
     corrupted_arr = hamming
     corrupted = rd.randrange(0,len(corrupted_arr))
     corrupted_arr[corrupted] = 1 if corrupted_arr[corrupted] % 2 == 0 else 0
     print(corrupted_arr)
     print(check_error(corrupted_arr))
     print("check")


main()