import streamlit as st

st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url("https://media.kasperskydaily.com/wp-content/uploads/sites/92/2015/06/06024742/ciphers-featured.png");
         background-size: cover;
         background-position: center;
         background-repeat: no-repeat;
         background-attachment: fixed;
     }}
     .custom-title {{
            color: white;
        }}
     </style>
     """,
     unsafe_allow_html=True
 )

def encrypt_message(message):
    enmsg = []
    for char in message:
        if 'a' <= char <= 'z':
            en = (ord(char) - ord('a') + 3) % 26 + ord('a')
        elif 'A' <= char <= 'Z':
            en = (ord(char) - ord('A') + 3) % 26 + ord('A')
        else:
            en = ord(char)
        enmsg.append(chr(en))
    return ''.join(enmsg)

def decrypt_message(encrypted_message):
    demsg = []
    for char in encrypted_message:
        if 'a' <= char <= 'z':
            de = (ord(char) - ord('a') - 3) % 26 + ord('a')
        elif 'A' <= char <= 'Z':
            de = (ord(char) - ord('A') - 3) % 26 + ord('A')
        else:
            de = ord(char)
        demsg.append(chr(de))
    return ''.join(demsg)

# Streamlit web app
#st.title("Message Encryption and Decryption")
st.markdown("<h1 class='custom-title'>Message Encryption and Decryption</h1>", unsafe_allow_html=True)

st.markdown("<h1 class='custom-title'>Encrypt</h1>", unsafe_allow_html=True)
message_to_encrypt = st.text_input("Enter message to encrypt:")
if st.button("Encrypt"):
    encrypted_message = encrypt_message(message_to_encrypt)
    st.text_area("Encrypted message:", encrypted_message, height=100)

st.markdown("<h1 class='custom-title'>Decrypt</h1>", unsafe_allow_html=True)
message_to_decrypt = st.text_input("Enter message to decrypt:")
if st.button("Decrypt"):
    decrypted_message = decrypt_message(message_to_decrypt)
    st.text_area("Decrypted message:", decrypted_message, height=100)
