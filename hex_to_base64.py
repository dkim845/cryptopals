# Script written to convert hex to base64
# Completed for the cryptopals challenges
# http://cryptopals.com/sets/1/challenges/1
#
# Daniel Kim 2/26/2019
import codecs


# Function that converts the hex key to base64
def encoder(word):
    # The codecs function first decodes the hex key into ASCII data
    # Then it is encoding with base64
    word = codecs.encode(codecs.decode(word, 'hex'), 'base64').decode()
    return word


# Main method
hex_word = input("Enter the hex string to convert: ")
hex_word = encoder(hex_word)
print("The base64 conversion is: " + hex_word)
