from np_payments.clients.esewa.esewa import EsewaClient


def main():
    client = EsewaClient(
        base_url="https://rc-epay.esewa.com.np/api/epay/main/v2/form",
        success_url="https://localhost:8000/success",
        failure_url="https://localhost:8000/failure",
        product_code="EPAYTEST",
        secret_key="8gBm/:&EnhH.1/q",
    )

    resposne = client.initiate_payment(
        amount=100,
        success_url="https://example.com/success",
        failure_url="https://example.com/failure",
        product_code="EPAYTEST",
    )
    print(resposne)


main()
# import asyncio

# asyncio.run(main())
