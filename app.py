
import streamlit as st

APP_NAME = "TxLens"
NETWORK = "Ethereum Mainnet"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔎",
)

st.title("🔎 TxLens")
st.subheader("Understand what happened on-chain.")

st.write(
    "TxLens helps you understand Ethereum transactions "
    "through readable, verifiable data."
)

st.divider()

st.info("Version 0.1 — Your transaction analysis tool is taking shape.")

st.text_input(
    "Ethereum transaction hash",
    placeholder="Paste a transaction hash here...",
)

st.button("Analyze transaction")

st.caption("Built with Python and Streamlit.")

