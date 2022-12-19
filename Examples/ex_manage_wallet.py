# Import the necessary libraries
import hashlib
import ecdsa

# Generate a private key
private_key = hashlib.sha256(b'your-secret-phrase').hexdigest()

# Generate a public key
sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
public_key = sk.verifying_key.to_string().hex()

# Generate a Bitcoin address
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(bytes.fromhex(public_key)).digest())
wallet_address = '1' + ripemd160.hexdigest()

# Print the wallet details
print("Private key:", private_key)
print("Public key:", public_key)
print("Wallet address:", wallet_address)
