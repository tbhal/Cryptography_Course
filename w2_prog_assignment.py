import base64
from Crypto.Cipher import AES
from Crypto.Util import Counter

def main():
    blockSize = 16 # 16 byte encryption

    q1 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14",
    "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81",
    blockSize)

    q2 = cbcDecrypt("140b41b22a29beb4061bda66b6747e14",
    "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253",
    blockSize)

    q3 = ctrDecrypt("36f18357be4dbd77f050515c73fcf9f2",
    "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329",
    blockSize)

    q4 = ctrDecrypt("36f18357be4dbd77f050515c73fcf9f2",
    "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451",
    blockSize)

    print("\n\nResults:")
    print("Q1. ", q1)
    print("Q2. ", q2)
    print("Q3. ", q3)
    print("Q4. ", q4)

def ctrDecrypt(key, cypherText, blockSize):
    k = base64.b16decode(key,True)
    ct = base64.b16decode(cypherText,True)
    iv = ct[:blockSize]
    main_ct = ct[blockSize:]
    ctr = Counter.new(128, initial_value=base64.b16encode(iv))
    aes_obj = AES.new(k, AES.MODE_CTR, counter=ctr)
    paddedStr = aes_obj.decrypt(main_ct)
    return paddedStr



def cbcDecrypt(key, cypherText, blockSize):
    k = base64.b16decode(key,True)
    ct = base64.b16decode(cypherText,True)
    iv = ct[:blockSize]
    main_ct = ct[blockSize:]
    aes_obj = AES.new(k, AES.MODE_CBC,iv)
    paddedStr = aes_obj.decrypt(main_ct)
    #print(paddedStr)
    paddingAmt = ord(paddedStr[len(paddedStr)-1:])
    return paddedStr[:-paddingAmt]

main()


# I was gettig an error NameError: name 'long' is not defined
# for resolving this go the Counter.py and change long with int(n, 16)
# as for python 3.x log has been swithced with int