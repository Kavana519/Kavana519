from cryptography.fernet import Fernet

# Sample device database (for demonstration purposes)
device_db = {
    "device123": "password",  # device_id: credentials
}

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to authenticate the device
def authenticate_device(device_id, credentials):
    if device_id in device_db and device_db[device_id] == credentials:
        print(f"Device {device_id} authenticated successfully.")
        return True
    print(f"Authentication failed for device {device_id}.")
    return False

# Function to encrypt data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    print("Data encrypted successfully.")
    return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    print("Data decrypted successfully.")
    return decrypted_data

# Function to detect threats in data
def detect_threats(data):
    # Placeholder for threat detection logic (this can be expanded)
    if "sensitive" in data.decode():  # Example condition for detection
        raise Exception("Threat detected: Sensitive information compromised!")

# Main function
def main():
    # Sample key generation and usage
    key = generate_key()
    device_id = "device123"
    credentials = "password"
    
    if authenticate_device(device_id, credentials):
        data = "This is some sensitive data"
        
        # Encrypt the data
        encrypted_data = encrypt_data(data, key)
        
        # Simulate threat detection on encrypted data
        try:
            detect_threats(encrypted_data)
        except Exception as e:
            print(e)
        
        # Decrypt the data (optional, for demonstration)
        decrypted_data = decrypt_data(encrypted_data, key)
        print("Decrypted data:", decrypted_data)

if __name__ == "__main__":
    main()
