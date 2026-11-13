from celery import shared_task
from xrpl.wallet import Wallet
from .xrpl_client import send_test_payment

@shared_task
def autonomous_payment_task(secret: str, destination: str, amount_drops: str):
    """
    Celery task to send payment autonomously on XRPL.
    - secret: Wallet seed string
    - destination: Destination address string
    - amount_drops: Amount to send in drops as string
    """
    wallet = Wallet(seed=secret)
    result = send_test_payment(wallet, destination, amount_drops)
    return result
