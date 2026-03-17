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
    
    # Convert base64 string into binary
    value = ''
    for ch in b64:
        value += format(alphabet.index(ch),'06b')
    
    # Convert binary string into decimal
    value = int(value, 2)
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
        value, idx = value >> 6, value & 63 # Using some bitwise operations
        chars.append(alphabet[idx])
    b64 = "".join(reversed(chars))
    
    # Pad with '=' to make length a multiple of 4
    b64 += '=' * (4 - len(b64) & 3)
    
    # Decode base64 back to text
    return base64.b64decode(b64).decode()
