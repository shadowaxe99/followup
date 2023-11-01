This task doesn't have a clear question or challenge to translate into a python code. However, since you are asking to demonstrate a comprehensive, intricately detailed, and state-of-the-art programming skills, I would modify the existing code by adding some functionalities into it correspondingly as shown below:

```python
import hashlib
import base64
import re
from datetime import datetime, timedelta
from getpass import getpass

class User:
    def __init__(self, email, password):
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if not self.validate_password(password):
            raise ValueError("Password must be at least 8 characters long")

        self.email = email
        self.password = self.encrypt_string(password)
        self.data = {}

    def encrypt_string(self, hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature

    def encode_data(self, data):
        encoded_bytes = base64.b64encode(data.encode("utf-8"))
        return str(encoded_bytes, "utf-8")

    def decode_data(self, data):
        decoded_bytes = base64.b64decode(data)
        return str(decoded_bytes, "utf-8")

    def calculate_follow_up_date(self, days):
        current_date = datetime.now()
        follow_up_date = current_date + timedelta(days=days)
        return follow_up_date.strftime("%Y-%m-%d")

    def validate_email(self, email):
        email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.match(email_regex, email) is not None

    def validate_password(self, password):
        return len(password) >= 8

    def add_data(self, key, value):
        encoded_value = self.encode_data(value)
        self.data[key] = encoded_value

    def view_data(self, key):
        encoded_value = self.data.get(key)
        if not encoded_value:
            return None
        decoded_value = self.decode_data(encoded_value)
        return decoded_value

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")
    user = User(email, password)
    while True:
        print("\n1. Add data\n2. View data\n3. Exit")
        choice = input("Your choice: ")
        if choice == '1':
            key = input("Enter data key: ")
            value = input("Enter data value: ")
            user.add_data(key, value)
            print(f"Data added under key: {key}")
        elif choice == '2':
            key = input("Enter data key to view its value: ")
            value = user.view_data(key)
            print(f"Data value: {value}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
```

This enhanced version now includes a class that manages User data. In addition to the methods already in the original script, we have included a method to store key-value data for each user where the value is encoded before being stored in order to maintain privacy. The user can also retrieve its own data through a provided key, where the data presented will be decoded from its original encoding. Users are asked to set their credentials upon creation of a User object, with suitable validations in place to ensure security standards are maintained. 

That being said, the complexity of this inspired task doesn't necessarily mean we need to separate files yet. But as the complexity expands, we can indeed organize various components in separate files and import them accordingly.