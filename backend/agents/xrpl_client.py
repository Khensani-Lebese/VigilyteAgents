from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment
from xrpl.transaction.autofill import autofill_transaction
from xrpl.transaction.signed_transaction import safe_sign_transaction
from xrpl.transaction.submit import send_reliable_submission

TESTNET_URL = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(TESTNET_URL)

def generate_wallet():
    return Wallet.create()

def send_test_payment(wallet, destination, amount_drops="1000000"):
    payment = Payment(
        account=wallet.classic_address,
        destination=destination,
        amount=amount_drops,
    )
    tx = autofill_transaction(payment, client)
    signed_tx = safe_sign_transaction(tx, wallet)
    response = send_reliable_submission(signed_tx, client)
    return response
