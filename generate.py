import secrets
import string
import hashlib


def generate_password(n):
    symbol = '-+*#&@%$_?'
    return ''.join([secrets.choice(string.ascii_letters + string.digits + symbol) for i in range(n)])

def create_hash(passwd):
    dk = hashlib.pbkdf2_hmac('sha512', passwd.encode('utf-8'), b'salt', 10000)
    return dk.hex()


if __name__ == "__main__":
    pass_list = []
    for i in range(100):
        pass_str = generate_password(10)
        pass_hash = create_hash(pass_str)
        with open('./passwd_hash.csv', mode='a') as f:
            f.write(pass_str + "," + pass_hash+ '\n')


