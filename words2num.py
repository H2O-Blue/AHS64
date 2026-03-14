import base64

def words2num(text: str) -> int:
    """
    Converts a piece of text into an absurdly huge number.

    Parameters
    ----------
    text : str
        The words you foolishly decided to turn into a number.
        Warning: Please do not input anything outside the ASCII table

    Returns
    -------
    int
        A number so large it makes no practical sense.

    Notes
    -----
    Looks like magic but really it's just base conversion.
    What type of base conversion do you ask? FAFO.
    """
    # Base64 alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Encode text to base64, strip padding
    b64 = base64.b64encode(text.encode()).decode().rstrip("=")
    
    # Convert base64 string into a giant integer
    value = 0
    for ch in b64:
        value = value * 64 + alphabet.index(ch)
    return value

def num2words(value: int) -> str:
    """
    Converts an absurdly huge number back into text.

    Looks impressive, but really it's just undoing the base conversion.
    What kind of base conversion you ask? Same FAFO energy, just reversed.
    WARNING: Do NOT import the actual num2words package from PyPI
    alongside this one. Unless you enjoy watching namespaces fight to the death.
    """
    # Base64 alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Convert integer back into base64 string
    chars = []
    while value > 0:
        value, idx = divmod(value, 64)
        chars.append(alphabet[idx])
    b64 = "".join(reversed(chars))
    
    # Pad with '=' to make length a multiple of 4
    while len(b64) % 4 != 0:
        b64 += "="
    
    # Decode base64 back to text
    return base64.b64decode(b64).decode()

