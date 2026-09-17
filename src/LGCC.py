#!/usr/bin/env python3

import base64
import getpass


# ============================================================
# LOGIC GATE CAESAR CIPHER (LGCC)
# ============================================================
#
# Educational implementation of the LGCC algorithm described
# in the accompanying academic documentation.
#
# LGCC combines:
#   - Caesar-style modular addition
#   - XOR logic-gate mixing
#   - Ciphertext feedback/chaining
#   - 8-bit left/right rotation
#   - Key-derived per-byte transformation values
#
# NOTE:
# LGCC is an experimental educational cipher and has not been
# formally cryptanalysed or validated for production security.
# ============================================================


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def rotate_left_8(value, amount):
    """
    Rotate an 8-bit value to the left.

    ROTL8(x, r) = ((x << r) | (x >> (8-r))) & 0xFF
    """

    value &= 0xFF
    amount &= 7

    if amount == 0:
        return value

    return ((value << amount) | (value >> (8 - amount))) & 0xFF


def rotate_right_8(value, amount):
    """
    Rotate an 8-bit value to the right.
    """

    value &= 0xFF
    amount &= 7

    if amount == 0:
        return value

    return ((value >> amount) | (value << (8 - amount))) & 0xFF


def key_to_bytes(key):
    """
    Convert the passphrase into UTF-8 key bytes.
    """

    if not key:
        raise ValueError("Key cannot be empty.")

    return key.encode("utf-8")


# ------------------------------------------------------------
# Encryption
# ------------------------------------------------------------

def encrypt(plaintext, key):
    """
    Encrypt a UTF-8 plaintext string using LGCC.

    Returns:
        Base64 encoded ciphertext
    """

    plaintext_bytes = plaintext.encode("utf-8")
    key_bytes = key_to_bytes(key)

    m = len(key_bytes)

    ciphertext = bytearray()

    # LGCC specifies Kbyte[0] as the initial feedback value.
    prev = key_bytes[0]

    for i, plaintext_byte in enumerate(plaintext_bytes):

        # ----------------------------------------------------
        # Step 1:
        # s_i = (K[i mod m] + i) mod 256
        # ----------------------------------------------------
        shift = (key_bytes[i % m] + i) % 256

        # ----------------------------------------------------
        # Step 2:
        # g_i = K[(i + 1) mod m]
        # ----------------------------------------------------
        gate_byte = key_bytes[(i + 1) % m]

        # ----------------------------------------------------
        # Step 3:
        # r_i = K[(i + 2) mod m] AND 7
        #
        # This guarantees a rotation amount between 0 and 7.
        # ----------------------------------------------------
        rotation = key_bytes[(i + 2) % m] & 7

        # ----------------------------------------------------
        # Step 4:
        # t_i = (P_i + s_i) mod 256
        # ----------------------------------------------------
        shifted = (plaintext_byte + shift) % 256

        # ----------------------------------------------------
        # Step 5:
        # u_i = t_i XOR g_i
        # ----------------------------------------------------
        mixed = shifted ^ gate_byte

        # ----------------------------------------------------
        # Step 6:
        # v_i = u_i XOR prev
        # ----------------------------------------------------
        feedback = mixed ^ prev

        # ----------------------------------------------------
        # Step 7:
        # C_i = ROTL8(v_i, r_i)
        # ----------------------------------------------------
        cipher_byte = rotate_left_8(feedback, rotation)

        ciphertext.append(cipher_byte)

        # ----------------------------------------------------
        # Step 8:
        # Update feedback for the next byte.
        # ----------------------------------------------------
        prev = cipher_byte

    # Ciphertext bytes cannot safely be displayed as normal text,
    # so encode them using Base64.
    return base64.b64encode(ciphertext).decode("ascii")


# ------------------------------------------------------------
# Decryption
# ------------------------------------------------------------

def decrypt(ciphertext_base64, key):
    """
    Decrypt a Base64 encoded LGCC ciphertext.

    Returns:
        Original UTF-8 plaintext string
    """

    try:
        ciphertext = base64.b64decode(ciphertext_base64, validate=True)
    except Exception:
        raise ValueError("Invalid Base64 ciphertext.")

    key_bytes = key_to_bytes(key)

    m = len(key_bytes)

    plaintext = bytearray()

    # Same initial feedback value used during encryption.
    prev = key_bytes[0]

    for i, cipher_byte in enumerate(ciphertext):

        # ----------------------------------------------------
        # Recalculate the same key-derived values.
        # ----------------------------------------------------
        shift = (key_bytes[i % m] + i) % 256

        gate_byte = key_bytes[(i + 1) % m]

        rotation = key_bytes[(i + 2) % m] & 7

        # ----------------------------------------------------
        # Step 1:
        # Undo rotation
        #
        # v_i = ROTR8(C_i, r_i)
        # ----------------------------------------------------
        feedback = rotate_right_8(cipher_byte, rotation)

        # ----------------------------------------------------
        # Step 2:
        # Undo chaining
        #
        # u_i = v_i XOR prev
        # ----------------------------------------------------
        mixed = feedback ^ prev

        # ----------------------------------------------------
        # Step 3:
        # Undo XOR mixing
        #
        # t_i = u_i XOR g_i
        # ----------------------------------------------------
        shifted = mixed ^ gate_byte

        # ----------------------------------------------------
        # Step 4:
        # Undo modular shift
        #
        # P_i = (t_i - s_i) mod 256
        # ----------------------------------------------------
        plaintext_byte = (shifted - shift) % 256

        plaintext.append(plaintext_byte)

        # ----------------------------------------------------
        # Update feedback using the CURRENT ciphertext byte.
        # ----------------------------------------------------
        prev = cipher_byte

    try:
        return plaintext.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(
            "Decryption failed: incorrect key or invalid UTF-8 plaintext."
        )


# ------------------------------------------------------------
# Interactive Interface
# ------------------------------------------------------------

def main():

    print("=" * 60)
    print("       LOGIC GATE CAESAR CIPHER (LGCC)")
    print("=" * 60)
    print()
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print()

    choice = input("Select an option: ").strip()

    if choice == "1":

        plaintext = input("\nEnter message: ")
        key = getpass.getpass("Enter key: ")

        try:
            ciphertext = encrypt(plaintext, key)

            print("\n" + "-" * 60)
            print("ENCRYPTED MESSAGE")
            print("-" * 60)
            print(ciphertext)
            print("-" * 60)

        except ValueError as error:
            print(f"\nError: {error}")

    elif choice == "2":

        ciphertext = input("\nEnter Base64 ciphertext: ")
        key = getpass.getpass("Enter key: ")

        try:
            plaintext = decrypt(ciphertext, key)

            print("\n" + "-" * 60)
            print("DECRYPTED MESSAGE")
            print("-" * 60)
            print(plaintext)
            print("-" * 60)

        except ValueError as error:
            print(f"\nError: {error}")

    elif choice == "3":
        print("\nExiting LGCC.")

    else:
        print("\nInvalid option.")


if __name__ == "__main__":
    main()