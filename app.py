
import re
import requests
import streamlit as st

APP_NAME = "TxLens"
NETWORK = "Ethereum Mainnet"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔎",
)

st.title("🔎 TxLens")
st.write("An Ethereum transaction analysis tool.")
st.caption(f"Network: {NETWORK}")

tx_hash = st.text_input(
    "Ethereum transaction hash",
    placeholder="Paste a transaction hash here...",
)

if st.button("Analyze transaction"):
    tx_hash = tx_hash.strip()

    if not re.fullmatch(r"0x[0-9a-fA-F]{64}", tx_hash):
        st.error("Invalid transaction hash format.")

    else:
        api_key = st.secrets["ETHERSCAN_API_KEY"]

        params = {
            "chainid": "1",
            "module": "proxy",
            "action": "eth_getTransactionReceipt",
            "txhash": tx_hash,
            "apikey": api_key,
        }

        try:
            response = requests.get(
                "https://api.etherscan.io/v2/api",
                params=params,
                timeout=15,
            )
            response.raise_for_status()
            data = response.json()

            receipt = data.get("result")

            if "error" in data:
                st.error("Ethereum API returned an error.")
                st.json(data["error"])

            elif receipt is None:
                st.warning(
                    "No transaction receipt found. "
                    "The transaction may be pending or "
                    "the hash may be incorrect."
                )
                st.json(data)

            elif not isinstance(receipt, dict):
                st.error("Unexpected API response.")
                st.json(data)

            else:
                status = receipt.get("status")

                if status == "0x1":
                    st.success("Transaction succeeded.")
                elif status == "0x0":
                    st.error("Transaction reverted.")
                else:
                    st.warning("Transaction status is unavailable.")

                st.write(
                    "Block number:",
                    int(receipt["blockNumber"], 16),
                )
                st.write(
                    "Gas used:",
                    int(receipt["gasUsed"], 16),
                )
                
            # Fetch transaction details
            tx_params = {
                "chainid": "1",
                "module": "proxy",
                "action": "eth_getTransactionByHash",
                "txhash": tx_hash,
                "apikey": api_key,
            }

            tx_response = requests.get(
                "https://api.etherscan.io/v2/api",
                params=tx_params,
                timeout=15,
            )
            tx_response.raise_for_status()
            tx_data = tx_response.json()
            transaction = tx_data.get("result")

            if isinstance(transaction, dict):
                sender = transaction.get("from")
                recipient = transaction.get("to")
                value_wei = int(transaction.get("value", "0x0"), 16)
                value_eth = value_wei / 10**18

                st.subheader("Transfer details")
                st.write("From:", sender)
                st.write("To:", recipient or "Contract creation")
                st.write("ETH transferred:", f"{value_eth:.8f} ETH")
            else:
                st.warning("Could not retrieve transaction details.")


        except requests.RequestException as error:
            st.error(f"API request failed: {error}")

st.divider()

st.info("Version 0.1 — Your transaction analysis tool is taking shape.")

st.caption("Built with Python and Streamlit.")
