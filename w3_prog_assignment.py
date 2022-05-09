import base64
import os
from Crypto.Hash import SHA256

def main():
    block_size = 1024
    target_file = "files/target.mp4"
    target_hash = ""

    verify_file = "files/verify.mp4"
    verify_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

    cal_hash = calculate_hash(verify_file, block_size)
    cal_hash_hex = base64.b16encode(cal_hash).decode('latin-1').lower()
    print("Calculated hash using the method wrote for the check file is: ", cal_hash_hex)
    print("Are the two hashes equal(given and calculated): ", cal_hash_hex == verify_hash)

    cal_target_hash = calculate_hash(target_file, block_size)
    cal_target_hex = base64.b16encode(cal_target_hash).decode('latin-1').lower()
    print("The target hash is: ", cal_target_hex)


def calculate_hash(path, block_size):
    # getting size of file
    file_size = os.path.getsize(path)
    # getting the last block size
    last_block_size = file_size % block_size

    res_hash = ''
    print("reading file at:", path)
    op = open(path, "rb")

    for segment in read_reversed(op, file_size, last_block_size, block_size):
        sha256 = SHA256.new()
        sha256.update(segment)
        
        if(res_hash):
            sha256.update(res_hash)

        res_hash = sha256.digest()
    op.close()
    
    return res_hash


def read_reversed(file_obj, file_size, last_segment_size, segment_size):
    iter = 0
    last_pos = file_size
    while last_pos > 0:
        size = segment_size

        if(iter == 0):
            size = last_segment_size

        # reading the file in reversed order
        file_obj.seek(last_pos - size)
        data = file_obj.read(segment_size)
        if not data:
            break

        iter += 1
        last_pos -= size
        yield data

main()