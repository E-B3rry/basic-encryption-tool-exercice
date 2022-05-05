# Tested and works with python 3.9.0

# Constants
__METHODS__ = ['rot', 'caesar', 'vigenere', 'polybius']


""" Disclaimer:
  " That's a very basic program which doesn't have anything special, except that it works.
  " Optimization isn't so bad, but I'm pretty sure it's far from being perfect. Hell, we're in Python!
  " Well, I hope it can be useful to you, probably trying to learn some new stuff.
"""


# Rotary encryption function
def rot_encrypt(text, shift=13):
    """
    Encrypts a string using rotate algorithm
    :param text: The string to encrypt
    :type text: str
    :param shift: The shift to use (can be negative)
    :type shift: int
    :return: Encrypted string
    :rtype: str
    """

    rot_text = ""  # Initializes the string

    # Iterates through each character in the text
    for char in text:
        # Only supports alpha and uppercase alpha
        if char.isalpha():
            # Get the char unicode value of the current character
            char_unicode = ord(char)
            # If the character is an uppercase alpha
            # Calculates the new character's unicode according to the case
            if char.isupper():
                # Code is broke down here on purpose, so I can explain what I did there
                relative_alpha_char = char_unicode - ord('A')  # Get the relative (upper)alpha character
                shifted = relative_alpha_char + shift  # Shift the relative alpha character
                # Get the new character, taking the modulo of the shift (so it stays under 26),
                # add the (upper)alpha character value back, and append it to the string (cast as a char)
                rot_text += chr(shifted % 26 + ord('A'))
            else:
                rot_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # If character is not alpha, just append it to the string
            rot_text += char

    return rot_text


# Rotary decryption function (alpha and uppercase alpha only)
def rot_decrypt(text, shift=13):
    """
    Decrypts a string using rotate algorithm
    :param text: The encrypted string
    :type text: str
    :param shift: The shift to use (can be negative)
    :type shift: int
    :return: Decrypted string
    :rtype: str
    """

    rot_text = ""  # Initializes the string

    # Iterates through each character in the text
    for char in text:
        # Only supports alpha and uppercase alpha
        if char.isalpha():
            # Get the char unicode value of the current character
            char_unicode = ord(char)
            # If the character is an uppercase alpha
            # Calculates the new character's unicode according to the case
            if char.isupper():
                # Code is broke down here on purpose, so I can explain what I did there
                relative_alpha_char = char_unicode - ord('A')  # Get the relative (upper)alpha character
                shifted = relative_alpha_char - shift  # Shift the relative alpha character backwards
                # Gets the new character, taking the modulo of the shift (so it stays under 26),
                # add the (upper)alpha character value back, and append it to the string (cast as a char)
                rot_text += chr(shifted % 26 + ord('A'))
            else:
                rot_text += chr((char_unicode - ord('a') - shift) % 26 + ord('a'))
        else:
            # If character is not alpha, just append it to the string
            rot_text += char

    return rot_text


# Vigenere cipher encryption function
def vigenere_encrypt(text, key):
    """
    Encrypts a string using the Vigenere cypher
    :param text: The string to encrypt
    :type text: str
    :param key: The key to use
    :type key: str
    :return: Encrypted string
    :rtype: str
    """

    # If key is empty, just return the text
    if not len(key):
        return text

    output_string = ""  # Initializes the string

    # Iterates through each character in the text (and enumerates it in an index variable)
    for i, char in enumerate(text):
        # Only supports alpha and uppercase alpha
        if char.isalpha():
            char_unicode = ord(char)  # Get the unicode value of the current character
            # If the character is an uppercase alpha
            if char.isupper():
                # Code is broke down here on purpose, so I can explain what I did there
                relative_alpha_char = char_unicode - ord('A')  # Gets the relative (upper)alpha character
                # (For the key, we will be using a modulo of the key length, so it doesn't go out of bounds)
                relative_key_char = ord(key[i % len(key)]) - ord('A')  # Gets the relative corresponding key character
                shifted = relative_alpha_char + relative_key_char  # Shifts the relative alpha character
                # Gets the new character, taking the modulo of the shift (so it stays under 26),
                # add the (upper)alpha character value back, and append it to the string (cast as a char)
                output_string += chr(shifted % 26 + ord('A'))
            else:
                # This is the optimized version of the code above, but I left it here for reference.
                # As the relative_alpha_char = chr - unicode(a) and the relative_keychar = keychr - unicode(a),
                # and for the encryption we just add them, we can just do keychr + chr - 2 * unicode(a)
                output_string += chr((char_unicode + ord(key[i % len(key)]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            output_string += char

    return output_string


# Vigenere cypher decryption function
def vigenere_decrypt(text, key):
    """
    Decrypts a string using the Vigenere cypher
    :param text: The string to decrypt
    :type text: str
    :param key: The key to use
    :type key: str
    :return: Decrypted string
    :rtype: str
    """

    # If key is empty, just return the text
    if not len(key):
        return text

    output_string = ""  # Initializes the string

    # Iterates through each character in the text (and enumerates it in an index variable)
    for i, char in enumerate(text):
        # Only supports alpha and uppercase alpha
        if char.isalpha():
            char_unicode = ord(char)  # Get the unicode value of the current character
            # If the character is an uppercase alpha
            if char.isupper():
                # Code is broke down here on purpose, so I can explain what I did there
                relative_alpha_char = char_unicode - ord('A')  # Gets the relative (upper)alpha character
                relative_key_char = ord(key[i % len(key)]) - ord('A')  # Gets the relative corresponding key character
                shifted = relative_alpha_char - relative_key_char  # Shifts the relative alpha character backwards
                # Gets the new character, taking the modulo of the shift (so it stays under 26),
                # add the (upper)alpha character value back, and append it to the string (cast as a char)
                output_string += chr(shifted % 26 + ord('A'))
            else:
                # This is the optimized version of the code above, but I left it here for reference.
                # As the relative_alpha_char = chr - unicode(a) and the relative_keychar = keychr - unicode(a),
                # and for the decryption you want to shift the relative_alpha_char backwards, so it's a subtraction
                # in the form of (a - b) - (c - b) <=> a - c as we eliminate the (-b + b). Therefore, we can
                # just subtract the keychr from chr and do a 26 modulo.
                output_string += chr((char_unicode - ord(key[i % len(key)])) % 26 + ord('a'))
        else:
            output_string += char

    return output_string


# Polybius square cipher encryption function
def polybius_encrypt(text, key):
    """
    Encrypts a string using the Polybius square cypher
    :param text: The string to encrypt
    :type text: str
    :param key: The key to use
    :type key: str
    :return: Encrypted string
    :rtype: str
    """

    # If the key isn't 25 characters long, raise an error
    if len(key) != 25:
        raise ValueError("Key must be 25 characters long for the normalized Polybius square encryption")

    polybius_string = ""  # Initializes the string

    # Normalize both parameters to upper case
    text = text.upper()
    key = key.upper()

    # Iterates through each character in the text
    for i in range(0, len(text)):
        try:
            """
            " In the normalized polybius square cypher, it's using a 5*5 table for the 26 alphabet letters.
            " Therefore, two letters are merged into one position. Usually, i and j are mixed, but here,
            " we don't take it into account here, the letter that is ignored is going to be the last of the key,
            " leaving the user to place the "unknown letter" of its choice at the end. 
            " This encryption/decryption method is not lossless, and is probably useless in a real world application, 
            " unless encrypting an array of base 25 values, which is not common at all in the computer field.
            """

            # Add the corresponding row and the column of the character in the encrypted string
            # // being the floor division operator (so we can fetch the row)
            # % being the modulo operator (remainder of the position of the row division (5), giving the column position)
            polybius_string += str(key.index(text[i]) // 5) + str(key.index(text[i]) % 5)
        except ValueError:
            # In case the character is not contained in the key, we set it to the last position of the key
            polybius_string += "55"

    return polybius_string


# Polybius square cipher decryption function
def polybius_decrypt(text, key):
    """
    Decrypts a string using the Polybius square cypher
    :param text: The string to decrypt
    :type text: str
    :param key: The key to use
    :type key: str
    :return: Decrypted string
    :rtype: str
    """

    # If the key isn't 25 characters long, raise an error
    if len(key) != 25:
        raise ValueError("Key must be 25 characters long for the normalized Polybius square encryption")

    decrypted_string = ""   # Initializes the string

    # Normalize both parameters to upper case
    text = text.upper()
    key = key.upper()

    # Iterates through each character in the text
    for i in range(0, len(text), 2):
        # Add the corresponding character in the key index (row * 5 + column) from the key, and limit the value to 25
        decrypted_string += key[min(int(text[i]) * 5 + int(text[i + 1]), len(key) - 1)]

    return decrypted_string
