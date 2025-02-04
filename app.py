import streamlit as st
from cryptography.fernet import Fernet
import os

# Generate or load encryption key
KEY_FILE = "secret.key"

if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    with open(KEY_FILE, "rb") as f:
        key = f.read()

cipher_suite = Fernet(key)

# Streamlit UI
st.title("🔐 Encrypt & Decrypt Messages")

# User input
message = st.text_area("Enter a message:")

col1, col2 = st.columns(2)

# Encrypt button
if col1.button("Encrypt"):
    if message:
        encrypted_message = cipher_suite.encrypt(message.encode()).decode()
        st.success(f"Encrypted: {encrypted_message}")
    else:
        st.error("Please enter a message to encrypt.")

# Decrypt button
if col2.button("Decrypt"):
    if message:
        try:
            decrypted_message = cipher_suite.decrypt(message.encode()).decode()
            st.success(f"Decrypted: {decrypted_message}")
        except:
            st.error("Invalid encrypted message!")
    else:
        st.error("Please enter an encrypted message to decrypt.")
