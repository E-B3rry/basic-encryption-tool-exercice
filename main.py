# Tested and works with python 3.9.0

# Integrated modules
import os
from shlex import split

# Project modules
import encoder_decoder as enc
import tests


# Constants
__HELP_MESSAGE__ = """List of commands:
> help: displays help
> encrypt <method> "<message>" [optional: "<key>"|<value>]: encrypts message with given method and optionally a key
> decrypt <method> "<message>" [optional: "<key>"|<value>]: decrypts message with given method and optionally a key
> tests: runs tests and ensure that the program is working
> credits: displays the credits
> exit: exits the program

Encryption/Decryption methods:
> rot: rotates the message by the given shift (by default rot13 is used)
> caesar: Caesar cipher with the given key (rotate with a key)
> vigenere: Vigenere cipher with the given key
> polybius: Polybius cipher with the given key

Last key and result are saved and can be used in the next command with the following flags (you still have to quote around flags if necessary):
> \\\\k: use the last key
> \\\\m: use the last message
> \\\\r: use the last result
"""

__CREDITS_MESSAGE__ = """Author:
    - Jules REIX CHARAT (E-Berry)
    
Contributors:
    - The gargantuan world of the internet (no code pasted)
    
License:
    - GPL v3 (see LICENSE)
"""


# Function to clear the console, both on Linux based os and Windows (source: internet, only thing that was pasted, I'm too lazy after all)
clear_screen = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Main function
if __name__ == '__main__':
    clear_screen()
    print(" <===== Encryption/Decryption Tool =====>")
    print("Welcome to this basic enc/decryption tool!\n\n")

    last_message = ""
    last_result = ""
    last_key = ""

    print(__HELP_MESSAGE__)
    input("Press enter to continue...")

    while True:
        clear_screen()
        print("Please enter your command:")
        command = input()

        if command.lower().startswith("h"):
            clear_screen()
            print(__HELP_MESSAGE__)
            input("Press enter to continue...")
        elif command.lower().startswith("enc") or command.lower().startswith("dec"):
            clear_screen()

            # Allow flags in parameters
            command = command.replace("\\\\k", last_key).replace("\\\\m", last_message).replace("\\\\r", last_result)

            try:
                parameters = split(command)  # From shlex module, split the command into parameters but keep the quotes
            except ValueError:
                print("Invalid command (check your quotes)")
                input("\nPress enter to continue...")
                continue

            # Check if the command has correct number of parameters
            if 3 <= len(parameters) <= 4:
                last_message = parameters[2]  # Save last message as... Well, last message

                # Check if the encryption method exists
                if parameters[1].lower() in enc.__METHODS__:
                    # Switch still doesn't exists in Python 3.9, should have updated my venv x)
                    # Won't comment this code, it's pretty straightforward and boring
                    if parameters[1].lower() == "rot":
                        if len(parameters) < 4:
                            rot_value = 13
                        elif parameters[3].isdigit():
                            rot_value = int(parameters[3])
                        else:
                            print("Last parameter must be a number for a rot shift.")
                            input("\nPress enter to continue...")
                            continue

                        last_key = str(rot_value)

                        if parameters[0].lower().startswith("enc"):
                            last_result = enc.rot_encrypt(parameters[2], rot_value)
                            print(f"Encrypted message: {last_result}")
                        else:
                            last_result = enc.rot_decrypt(parameters[2], rot_value)
                            print(f"Decrypted message: {last_result}")
                    elif parameters[1].lower() == "caesar":
                        if len(parameters) == 4:
                            if parameters[3].isdigit():
                                rot_value = int(parameters[3])
                            else:
                                print("Last parameter must be a number for a Caesar shift.")
                                input("\nPress enter to continue...")
                                continue

                            last_key = str(rot_value)

                            if parameters[0].lower().startswith("enc"):
                                last_result = enc.rot_encrypt(parameters[2], int(parameters[3]))
                                print(f"Encrypted message: {last_result}")
                            else:
                                last_result = enc.rot_decrypt(parameters[2], int(parameters[3]))
                                print(f"Decrypted message: {last_result}")
                        else:
                            print("Please enter the value of the Caesar shift algorithm (any positive or negative real number).")
                    elif parameters[1].lower() == "vigenere":
                        if len(parameters) == 4:
                            last_key = parameters[3]

                            if parameters[0].lower().startswith("enc"):
                                last_result = enc.vigenere_encrypt(parameters[2], parameters[3])
                                print(f"Encrypted message: {last_result}")
                            else:
                                last_result = enc.vigenere_decrypt(parameters[2], parameters[3])
                                print(f"Decrypted message: {last_result}")
                        else:
                            print("Please enter a key for the Vigenere algorithm!")
                    elif parameters[1].lower() == "polybius":
                        if len(parameters) == 4:
                            if len(parameters[3]) == 25:
                                last_key = parameters[3]

                                if parameters[0].lower().startswith("enc"):
                                    last_result = enc.polybius_encrypt(parameters[2], parameters[3])
                                    print(f"Encrypted message: {last_result}")
                                else:
                                    last_result = enc.polybius_decrypt(parameters[2], parameters[3])
                                    print(f"Decrypted message: {last_result}")
                            else:
                                print("The length of the key must be of 25.")
                        else:
                            print("Please enter a key for the Polybius Square algorithm!")

                    input("\nPress enter to continue...")
                else:
                    print("Invalid method!")
                    input("\nPress enter to continue...")
            else:
                print("Wrong number of parameters, please ensure that you quoted your text and your key.")
                input("\nPress enter to continue...")
        elif command.lower().startswith("t"):
            # Runs all tests from the test module
            try:
                tests.run_all()
            except BaseException as e:
                e = str(e)
                print(f"That's bad... An error occurred: \n\"\"\"\n{e if e else 'Cannot fetch error. Please directly run tests.py.'}\n\"\"\"")
                print("The actual program may fail as tests indicates that the encoder_decoder module is not 100% reliable.")

            input("\nPress enter to continue...")
        elif command.lower().startswith("c"):
            # Prints the credits
            clear_screen()
            print(__CREDITS_MESSAGE__)
            input("\nPress enter to continue...")
        elif command.lower().startswith("ex"):
            clear_screen()
            break

    input("\n\nPress enter to exit...")
