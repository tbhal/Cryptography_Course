

def main():
    text1 = "attack at dawn"
    encoded_str = bytes.fromhex('6c73d5240a948c86981bc294814d').decode('latin-1')
    key = xor_strings(text1, encoded_str)

    text2 = "attack at dusk"
    text2_encoded = xor_strings(text2, key)
    print(text2_encoded.encode('latin-1').hex())


def xor_strings(strA, strB):
    return ''.join(chr(ord(chrA) ^ ord(chrB)) for (chrA, chrB) in zip(strA, strB))

main()

# result is 6c73d5240a948c86981bc2808548