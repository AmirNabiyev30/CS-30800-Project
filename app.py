import streamlit as st

# Page config
st.set_page_config(page_title="Vigenère Cipher", page_icon="🔐", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background: #1a1a2e;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #16213e;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        color: #e94560;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0f3460;
        color: #00d9ff;
    }
    .title-container {
        text-align: center;
        padding: 30px;
        background: #16213e;
        border-radius: 20px;
        margin-bottom: 40px;
        border: 2px solid #e94560;
    }
    .result-box {
        background: #16213e;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 2px solid #00d9ff;
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
    }
    .stButton>button {
        width: 100%;
        background: #e94560;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: #ff6b81;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(233, 69, 96, 0.4);
    }
    .stTextArea textarea, .stTextInput input {
        background-color: #0f3460 !important;
        color: white !important;
        border: 2px solid #16213e !important;
        border-radius: 10px !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00d9ff !important;
        box-shadow: 0 0 10px rgba(0, 217, 255, 0.3) !important;
    }
    h1, h2, h3, p, label {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="title-container">
    <h1>🔐 SECRET MESSAGE ENCODER 🔐</h1>
    <p style="font-size: 20px;">Encode your messages with the Vigenère Cipher!</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["🔒 Encrypt", "🔓 Decrypt"])

with tab1:
    st.markdown("### 📝 Your Secret Message")
    plaintext = st.text_area("Type your message here:", height=150, key="plaintext", 
                             placeholder="Enter the message you want to encrypt...")
    
    st.markdown("### 🔑 Secret Key")
    encrypt_key = st.text_input("Enter your key:", key="encrypt_key", 
                                placeholder="e.g., SECRET")
    
    if st.button("✨ ENCRYPT MESSAGE ✨", key="encrypt_button"):
        if plaintext and encrypt_key:
            if encrypt_key.isalpha():

                def encryption(text, secret_key):
                    ciphertext = ""    
                    key_index = 0
                    key_len = len(secret_key)

                    for ch in text:
                        if ch == " ":
                            ciphertext += " "
                            continue

                        key_char = secret_key[key_index % key_len]

                        if ch.isupper():
                            shift = ord(key_char.upper()) - 65
                            new_char = chr((ord(ch) - 65 + shift) % 26 + 65)
                        else:
                            shift = ord(key_char.lower()) - 97
                            new_char = chr((ord(ch) - 97 + shift) % 26 + 97)

                        ciphertext += new_char
                        key_index += 1

                    return ciphertext
                encrypted = "YOUR ENCRYPTED MESSAGE WILL APPEAR HERE"
                
                st.markdown(f"### 🎉 Encrypted Message: {encryption(plaintext,encrypt_key)}") 
                st.success("✅ Message encrypted successfully!")
            else:
                st.error("❌ Key must contain only letters!")
        else:
            st.warning("⚠️ Please enter both message and key!")

with tab2:
    st.markdown("### 🔍 Encrypted Message")
    ciphertext = st.text_area("Paste encrypted message:", height=150, key="ciphertext",
                              placeholder="Enter the encrypted message...")
    
    st.markdown("### 🔑 Secret Key")
    decrypt_key = st.text_input("Enter the key:", key="decrypt_key",
                                placeholder="e.g., SECRET")
    
    if st.button("🔓 DECRYPT MESSAGE 🔓", key="decrypt_button"):
        if ciphertext and decrypt_key:
            if decrypt_key.isalpha():
                def decryption(ciphertext, secretkey):
                    plaintext = ""
                    keyindex = 0
                    keylen = len(secretkey)

                    for ch in ciphertext:
                        if ch == " ":
                            plaintext += " "
                            continue

                        keychar = secretkey[keyindex % keylen]

                        if ch.isupper():
                            shift = ord(keychar.upper()) - 65
                            newchar = chr((ord(ch) - 65 - shift + 26) % 26 + 65)
                        else:
                            shift = ord(keychar.lower()) - 97
                            newchar = chr((ord(ch) - 97 - shift + 26) % 26 + 97)

                        plaintext += newchar
                        keyindex += 1

                    return plaintext
                
                
                st.markdown(f"### 🎊 Decrypted Message: {decryption(ciphertext,decrypt_key)}")
                st.success("✅ Message decrypted successfully!")
            else:
                st.error("❌ Key must contain only letters!")
        else:
            st.warning("⚠️ Please enter both encrypted message and key!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #00d9ff; padding: 20px;">
    <p>Group D</p>
</div>
""", unsafe_allow_html=True)