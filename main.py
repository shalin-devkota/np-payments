from np_payments.clients.esewa.esewa import EsewaClient


def main():
    client = EsewaClient(
        base_url="https://rc-epay.esewa.com.np/api/epay/main/v2/form",
        success_url="https://localhost:8000/success",
        failure_url="https://localhost:8000/failure",
        product_code="EPAYTEST",
        secret_key="8gBm/:&EnhH.1/q",
    )

    # resposne = client.initiate_payment(
    #     amount=100,
    #     success_url="https://example.com/success",
    #     failure_url="https://example.com/failure",
    #     product_code="EPAYTEST",
    # )
    data = "eyJ0cmFuc2FjdGlvbl9jb2RlIjoiMDAwQkNKRCIsInN0YXR1cyI6IkNPTVBMRVRFIiwidG90YWxfYW1vdW50IjoiMTAwLjAiLCJ0cmFuc2FjdGlvbl91dWlkIjoiYzBkZGUyMTQtYTIwOC00YzA1LWFiN2MtNWU5NWE1NzYwMTIwIiwicHJvZHVjdF9jb2RlIjoiRVBBWVRFU1QiLCJzaWduZWRfZmllbGRfbmFtZXMiOiJ0cmFuc2FjdGlvbl9jb2RlLHN0YXR1cyx0b3RhbF9hbW91bnQsdHJhbnNhY3Rpb25fdXVpZCxwcm9kdWN0X2NvZGUsc2lnbmVkX2ZpZWxkX25hbWVzIiwic2lnbmF0dXJlIjoiL0p1QXpEQkxLaFc1ckVJdE1rQ2xsQnI0cGJ4U1IvYlNGSlBXVHlya3U1VT0ifQ=="
    response = client.validate_payment(data=data)


main()


# import asyncio

# asyncio.run(main())
