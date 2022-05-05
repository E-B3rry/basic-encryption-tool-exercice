# Project modules
import encoder_decoder as enc


# Tests rotary encoder/decoder
def test_rotary():
    print("> Testing rotary encryption/decryption...")

    # Default 13 rotation
    assert(enc.rot_encrypt("Hello World! 135&[)%") == "Uryyb Jbeyq! 135&[)%")
    assert(enc.rot_decrypt("Uryyb Jbeyq! 135&[)%") == "Hello World! 135&[)%")

    # Custom rotations
    assert(enc.rot_encrypt("Hello World! 135&[)%", 10) == "Rovvy Gybvn! 135&[)%")
    assert(enc.rot_decrypt("Rovvy Gybvn! 135&[)%", 10) == "Hello World! 135&[)%")

    # Negative numbers must work too
    assert(enc.rot_encrypt("Hello World! 135&[)%", -13) == "Uryyb Jbeyq! 135&[)%")
    assert(enc.rot_decrypt("Uryyb Jbeyq! 135&[)%", -13) == "Hello World! 135&[)%")

    print("  Test successful!\n")


# Tests Vigenere cypher encryption/decryption
def test_vigenere():
    print("> Testing Vigenere cypher encryption/decryption...")

    # Empty key
    assert(enc.vigenere_encrypt("Hello World! 135&[)%", "") == "Hello World! 135&[)%")
    assert(enc.vigenere_decrypt("Hello World! 135&[)%", "") == "Hello World! 135&[)%")

    # Key smaller than string
    assert(enc.vigenere_encrypt("Hello World! 135&[)%", "blobby") == "Opzmp Dzfme! 135&[)%")
    assert(enc.vigenere_decrypt("Opzmp Dzfme! 135&[)%", "blobby") == "Hello World! 135&[)%")

    # Key larger than string
    assert(enc.vigenere_encrypt("Hello World! 135&[)%", "blobbyisthebestcreature666") == "Opzmp Kgksh! 135&[)%")
    assert(enc.vigenere_decrypt("Opzmp Kgksh! 135&[)%", "blobbyisthebestcreature666") == "Hello World! 135&[)%")

    # Key with same length as string

    print("  Test successful!\n")


# Tests Polybius square cipher encryption/decryption
def test_polybius_square():
    print("> Testing Polybius square cipher encryption/decryption...")

    # Default case
    assert(enc.polybius_encrypt("HELLO WORLD MY BOI", "abcdefghijklmnopqrstuvwy ") == "120421212444422432210344224344012413")
    assert(enc.polybius_decrypt("120421212444422432210344224344012413", "abcdefghijklmnopqrstuvwy ") == "HELLO WORLD MY BOI")

    print("  Test successful!\n")


# Runs tests
def run_all():
    print("\nRunning all the tests...\n")
    test_rotary()
    test_vigenere()
    test_polybius_square()

    print("All tests passed!\n")


if __name__ == '__main__':
    run_all()
    exit(0)
