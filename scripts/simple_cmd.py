import argparse
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes  # Use cryptography's hash algorithms instead of hashlib

# Function to derive a key from the password
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(input_file, password, output_file):
    salt = os.urandom(16)  # Create a random salt
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(input_file, 'rb') as f:
        data = f.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(data)

    # Save the encrypted data and salt
    with open(output_file, 'wb') as f:
        f.write(salt + encrypted_data)  # Prepend the salt to the encrypted file

    print(f"File '{input_file}' has been encrypted and saved to '{output_file}'.")

def decrypt_file(input_file, password, output_file):
    with open(input_file, 'rb') as f:
        salt = f.read(16)  # The first 16 bytes are the salt
        encrypted_data = f.read()

    key = derive_key(password, salt)
    fernet = Fernet(key)

    # Decrypt the data
    try:
        decrypted_data = fernet.decrypt(encrypted_data)

        # Write the decrypted data to the output file
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"File '{input_file}' has been decrypted and saved to '{output_file}'.")
    except Exception as e:
        print(f"Failed to decrypt the file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Simple File Encryptor/Decryptor')
    
    subparsers = parser.add_subparsers(dest='command', help='encrypt or decrypt')

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file')
    encrypt_parser.add_argument('input_file', help='The input file to encrypt')
    encrypt_parser.add_argument('-p', '--password', required=True, help='The password to use for encryption')
    encrypt_parser.add_argument('-o', '--output', required=True, help='The output file path for the encrypted file')

    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a file')
    decrypt_parser.add_argument('input_file', help='The input file to decrypt')
    decrypt_parser.add_argument('-p', '--password', required=True, help='The password to use for decryption')
    decrypt_parser.add_argument('-o', '--output', required=True, help='The output file path for the decrypted file')

    args = parser.parse_args()

    if args.command == 'encrypt':
        encrypt_file(args.input_file, args.password, args.output)
    elif args.command == 'decrypt':
        decrypt_file(args.input_file, args.password, args.output)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()