import hashlib

CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def generate_base62_identifier(url):
    # Use a hash function to generate a unique numeric ID for the URL
    # Here, we use SHA-256 for simplicity
    hashed = hashlib.sha256(url.encode()).hexdigest()

    # Convert the hexadecimal hash to a decimal number
    decimal_id = int(hashed, 16)

    # Convert the decimal number to Base62
    base62_id = decimal_to_base62(decimal_id)

    return base62_id

def decimal_to_base62(decimal):
    if decimal == 0:
        return CHARSET[0]

    result = ""
    while decimal:
        decimal, remainder = divmod(decimal, 62)
        result = CHARSET[remainder] + result

    return result

# Example: Generate Base62 identifier for the provided URL
url = "https://chat.openai.com/c/0ce02237-6984-49bd-a1d3-808965fd368e"
base62_identifier = generate_base62_identifier(url)

print(f"URL: {url}")
print(f"Base62 Identifier: {base62_identifier}")