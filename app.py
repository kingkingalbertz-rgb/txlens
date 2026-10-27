APP_NAME = "TxLens"
NETWORK = "Ethereum Mainnet"


def get_app_info():
    return {
        "name": APP_NAME,
        "network": NETWORK,
        "version": "0.1.0",
    }


app_info = get_app_info()

print("Application:", app_info["name"])
print("Network:", app_info["network"])
print("Version:", app_info["version"])
