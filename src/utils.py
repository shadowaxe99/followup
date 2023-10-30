```python
import hashlib
import base64
from datetime import datetime, timedelta

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def encode_data(data):
    encoded_bytes = base64.b64encode(data.encode("utf-8"))
    return str(encoded_bytes, "utf-8")

def decode_data(data):
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, "utf-8")

def calculate_follow_up_date(days):
    current_date = datetime.now()
    follow_up_date = current_date + timedelta(days=days)
    return follow_up_date.strftime("%Y-%m-%d")

def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False

def validate_password(password):
    if len(password) >= 8:
        return True
    return False
```