#Multiplication

def main():
    print('Multiplication')
    while True:
        try:
            print('Input multiplicand(integer):')
            Multiplicand = int(input())
            print('Input multiplier(integer):')
            Multiplier = int(input())
            break
        except:
            print("That's not a valid option!")
    
    print('_________________________________________________________________')
    print('Multiplicand = ', Multiplicand)
    print('Multiplier = ', Multiplier)

    Result = multiply(Multiplicand, Multiplier)
    print('_________________________________________________________________')
    print()
    print('Result: ', Result)
    print('Expected result: ', Multiplicand * Multiplier)
    if(Result == Multiplicand * Multiplier):
        print('\033[92m Whoa, it worked!! \033[0m')
    else:
        print('\033[91m Whoa, it not worked!! \033[0m')
    print()


def multiply(multiplicand, multiplier):
    binaryMultiplicand = shiftToNBit(bin(multiplicand).lstrip('0b'), n=32)
    print('Multiplicand: ' + binaryMultiplicand)
    
    binaryMultiplier = shiftToNBit(bin(multiplier).lstrip('0b'), n=32)
    print('Multiplier:   ' + binaryMultiplier)
    
    binaryResult = shiftToNBit(bin(0).lstrip('0b'), n=64)
    print('Initializing register: ' + binaryResult)
    print()
    print('\033[4mShifting multiplicand to left:  ' + '|' + 'Shifting multiplier to right:    \033[0m')
    for i in range(0, 32):
        if binaryMultiplier[len(binaryMultiplier) - 1] == '1':
            print('_________________________________________________________________')
            print()
            print('\033[92m Multiplier LSB=1: adding multiplicand to product')
            binaryResult = binaryAdd(binaryMultiplicand, binaryResult)
            print('Product: ' + binaryResult + '\033[0m')
            print('_________________________________________________________________')
            print()
        # multiplicand left bin-shift
        binaryMultiplicand = shiftLeft(binaryMultiplicand)
        # multiplier right bin-shift
        binaryMultiplier = shiftRight(binaryMultiplier)
        print('\033[4m' + binaryMultiplicand + '|' + binaryMultiplier + '\033[0m')

    return int(binaryResult, 2)


def binaryAdd(a, b, n=64):
    a_i = int(a, 2)
    b_i = int(b, 2)
    return shiftToNBit(bin(a_i+b_i).lstrip('0b'), n)


def shiftToNBit(bin_number, n=32):
    temp_str = ''
    while len(temp_str + bin_number) < n:
        temp_str += '0'
    
    return temp_str + bin_number


def shiftLeft(str):
    return str[1:len(str)] + '0'


def shiftRight(str):
    return '0' + str[:len(str) - 1]


if __name__ == "__main__":
    main()