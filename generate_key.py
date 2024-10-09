import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth


names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["XXX", "XXX"]

# Create an instance of the Hasher class
hasher = stauth.Hasher(passwords)

# Generate hashed passwords
hashed_passwords = [hasher.hash(password) for password in passwords]

print(hashed_passwords)

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)