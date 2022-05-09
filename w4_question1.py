import base64
from tkinter.tix import Tree


def main():
    cypherText = "20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d".split(' ')
    
    # first part is IV
    # cypherTextIV = base64.b16decode(cypherText[0], True)
    # cypherTextmain = base64.b16decode(cypherText[1], True)

    cypherTextIV = bytes.fromhex(cypherText[0]).decode('latin-1')
    cypherTextmain = bytes.fromhex(cypherText[0]).decode('latin-1')

    plainText = "Pay Bob 100$"
    plainTextTarget = "Pay Bob 500$"

    # define padding
    paddingNum1 = str(len(cypherTextmain) - len(plainText))
    padding1 = "".join([paddingNum1] * int(paddingNum1))

    paddingNum2 = str(len(cypherTextmain) - len(plainTextTarget))
    padding2 = "".join([paddingNum2] * int(paddingNum2))

    # appending padding to plaintext
    plainText += padding1
    plainTextTarget += padding2

    # xor plain text
    xorPlainText = strxor(plainText, plainTextTarget)

    # the IV is xored with the first block in cbc, so to get the desired result
    # we have to xor the IV with the mutated plaintext
    newIV = strxor(xorPlainText, cypherTextIV)

    print("New CBC: ", newIV.encode('latin-1').hex(), cypherText[1])


def strxor(a,b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x,y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x,y) in zip(a, b[:len(a)])])

main()