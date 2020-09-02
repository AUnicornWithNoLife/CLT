import fire
import os
import hashlib

def hash(target = ""):
    tar = os.getcwd() + target
    fi = open(tar, "rb")

    hashlib.md5(fi.read)
    out = open(tar + ".hash", "xb")
    out.write(hash_object.hexdigest())
    out.close()
    fi.close()

if __name__ == "__main__":
    fire.Fire(hash)