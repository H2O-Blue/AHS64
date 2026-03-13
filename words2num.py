import base64

def words2num(text: str) -> int:
    # Base64 alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Encode text to base64, strip padding
    b64 = base64.b64encode(text.encode()).decode().rstrip("=")
    
    # Convert base64 string into a giant integer
    value = 0
    for ch in b64:
        value = value * 64 + alphabet.index(ch)
    return value
