from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import AgentWallet, Mandate


class DashboardApiTests(APITestCase):
    def test_dashboard_is_served_by_django(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'id="wallet-list"')
        self.assertContains(response, 'fetchCollection("/api/wallets/")')
        self.assertContains(response, 'fetchCollection("/api/mandates/")')

    def test_wallet_api_does_not_expose_seed(self):
        wallet = AgentWallet.objects.create(
            name="Primary",
            xrpl_address="rPrimaryWalletAddress",
            seed="sensitive-wallet-seed",
        )

        response = self.client.get("/api/wallets/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], wallet.id)
        self.assertNotIn("seed", response.data[0])

    def test_wallet_api_accepts_seed_without_returning_it(self):
        response = self.client.post(
            "/api/wallets/",
            {
                "name": "Primary",
                "xrpl_address": "rPrimaryWalletAddress",
                "seed": "sensitive-wallet-seed",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("seed", response.data)

    def test_mandate_api_returns_wallet_relation_and_policy(self):
        wallet = AgentWallet.objects.create(
            name="Primary",
            xrpl_address="rPrimaryWalletAddress",
            seed="sensitive-wallet-seed",
        )
        mandate = Mandate.objects.create(
            agent_wallet=wallet,
            max_spend_amount="25.000000",
            allowed_recipients=["rApprovedRecipient"],
        )

        response = self.client.get("/api/mandates/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], mandate.id)
        self.assertEqual(response.data[0]["agent_wallet"], wallet.id)
        self.assertEqual(response.data[0]["allowed_recipients"], ["rApprovedRecipient"])
