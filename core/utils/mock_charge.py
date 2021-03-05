def mock_charge():
    return {
        "id": "ch_1HtF7bA6fNGd5nTNhZNyOXME",
        "object": "charge",
        "amount": 2000,
        "amount_captured": 120,
        "amount_refunded": 0,
        "application": None,
        "application_fee": None,
        "application_fee_amount": None,
        "balance_transaction": "txn_1HtF7cA6fNGd5nTNxh5Xx2gT",
        "billing_details": {
            "address": {
                "city": None,
                "country": None,
                "line1": None,
                "line2": None,
                "postal_code": None,
                "state": None
            },
            "email": None,
            "name": None,
            "phone": None
        },
        "calculated_statement_descriptor": "Stripe",
        "captured": True,
        "created": 1606753263,
        "currency": "usd",
        "customer": None,
        "description": "My First Test Charge (created for API docs)",
        "disputed": False,
        "failure_code": None,
        "failure_message": None,
        "fraud_details": {},
        "invoice": None,
        "livemode": False,
        "metadata": {},
        "on_behalf_of": None,
        "order": None,
        "outcome": {
            "network_status": "approved_by_network",
            "reason": None,
            "risk_level": "normal",
            "risk_score": 42,
            "seller_message": "Payment complete.",
            "type": "authorized"
        },
        "paid": True,
        "payment_intent": None,
        "payment_method": "card_1HtF7bA6fNGd5nTN6BSYP65R",
        "payment_method_details": {
            "card": {
                "brand": "visa",
                "checks": {
                    "address_line1_check": None,
                    "address_postal_code_check": None,
                    "cvc_check": "pass"
                },
                "country": "US",
                "exp_month": 11,
                "exp_year": 2021,
                "fingerprint": "NREWjQgtjy4vzpvl",
                "funding": "credit",
                "installments": None,
                "last4": "4242",
                "network": "visa",
                "three_d_secure": None,
                "wallet": None
            },
            "type": "card"
        },
        "receipt_email": None,
        "receipt_number": None,
        "receipt_url": "https://pay.stripe.com/receipts/acct_1Ht7ZOA6fNGd5nTN/ch_1HtF7bA6fNGd5nTNhZNyOXME/rcpt_IUDYTsmBx5DNjRdopVJYIwgBOnS5SGU",
        "refunded": False,
        "refunds": {
            "object": "list",
            "data": [],
            "has_more": False,
            "url": "/v1/charges/ch_1HtF7bA6fNGd5nTNhZNyOXME/refunds"
        },
        "status": "succeeded",
        "transfer_data": None,
        "transfer_group": None,
        "source": "tok_mastercard"
    }
