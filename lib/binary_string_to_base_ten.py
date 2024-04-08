binary_to_base_10 = int('11001', 2)
print(binary_to_base_10) # => 25

hexadecimal_to_base_10 = int('10', 16)
print(hexadecimal_to_base_10) # => 16

base_10_to_binary = bin(25)
print(base_10_to_binary) # => 0b11001 where 0b denotes binary and 11001 is the binary value

base_10_to_hexadecimal = hex(16)
print(base_10_to_hexadecimal) # => 0x10 where 0x denotes hexadecimal and 10 is the hexadecimal value

base_10_to_base_8 = oct(24)
print(base_10_to_base_8) # => 0o30 where 0o denotes base 8 and 30 is the base 8 value, 3 eights and 0 units

# Other base conversions require a custom function:
def decimal_to_base_n(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
    return result

# e.g. number = 25, base = 2
#remainder = 1, result = 1, number = 12
#remainder = 0, result = 01, number = 6
#remainder = 0, result = 001, number = 3
#remainder = 1, result = 1001, number = 1
#remainder = 1, result = 11001, number = 0
# returns the result 11001

# custom method to convert from binary to base 10
def bin_to_decimal(input_string):
    num = 0
    input_string = input_string[::-1] # reverse the input_stringut string
    for i in range(len(input_string)):
        num += int(input_string[i]) * 2 ** i # adds (current digit * 2) to the power of index
    return num

# e.g. input_string = '11001'
# reversed input_string = '10011'
# i = 0, digit = 1, add = 1 * 2 ** 0 = 1, num = 0 + 1 = 1
# i = 1, digit = 0, add = 0 * 2 ** 1 = 1, num = 1 + 0 = 1
# i = 2, digit = 0, add = 0 * 2 ** 2 = 1, num = 1 + 0 = 1
# i = 3, digit = 1, add = 1 * 2 ** 3 = 8, num = 1 + 8 = 9
# i = 4, digit = 1, add = 1 * 2 ** 4 = 16, num = 9 + 16 = 25




