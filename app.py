
import streamlit as st

APP_NAME = "TxLens"
NETWORK = "Ethereum Mainnet"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔎",
)


tx_hash = st.text_input(
    "Ethereum transaction hash",
    placeholder="Paste a transaction hash here...",
)

if st.button("Analyze transaction"):
    tx_hash = tx_hash.strip()

    if len(tx_hash) != 66 or not tx_hash.startswith("0x"):
        st.error("Invalid transaction hash format.")
    else:
        st.success("Transaction hash format looks correct.")
        st.code(tx_hash)


st.divider()

st.info("Version 0.1 — Your transaction analysis tool is taking shape.")

st.text_input(
    "Ethereum transaction hash",
    placeholder="Paste a transaction hash here...",
)

st.button("Analyze transaction")

st.caption("Built with Python and Streamlit.")

