# ZAD 1
int_1 = 14
int_2 = 0x1A 
print('Pierwsza liczba:',int_1)
print('Druga liczba:',int_2)

float_1 = 3.14
float_2 = (-0b10011)
print('Pierwszy float:',float_1)
print('Drugi float:',float_2)

# ZAD 2
liczba = 19
num_set_bits2 = int.bit_count(liczba)
print(f"Ilość bitów w liczbie {liczba} wynosi: {num_set_bits2}")

is_integer1 = 3.0
is_integer2 = 3.14
print(f"{is_integer1} is an integer: {is_integer1.is_integer()}")
print(f"{is_integer2} is an integer: {is_integer2.is_integer()}") 

# ZAD 3 
bit_1 = 0b1111000
bit_2 = 0b1111
print('Bit pierwszy',bit_1)
print('Bit drugi',bit_2)
print(bit_1 & bit_2)
print(bit_1 | bit_2)
print(bit_1 ^ bit_2)
print(bit_1, bit_1 << 3)
