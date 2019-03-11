# Fixed XOR Cipher
# Daniel Kim 03/11/2019
# Will take in two equal sized hex buffers and return the XOR equivalent
# Set 1 Challenge 2


# Function to convert hex array to int array
def create_hex_to_ints(word):
    arr = []
    for a in word:
        x = int(a, 16)
        arr.append(x)
    return arr


# Creates xor hex list from two buffers
def create_xor(w1, w2):
    arr = []
    arr1 = create_hex_to_ints(w1)
    arr2 = create_hex_to_ints(w2)
    for a, b in zip(arr1, arr2):
        x = a ^ b
        x = hex(x)[2:]
        arr.append(x)
    return arr


# Main method
word1 = input("Enter the first buffer: ")
word2 = input("Enter the second buffer: ")
if len(word1) != len(word2):
    exit("Invalid input. Requires two equal length buffers.")
result = create_xor(word1, word2)
result = ''.join(result)
print(result)
