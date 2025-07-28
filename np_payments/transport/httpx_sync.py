import httpx


class AsyncHTTPTransport:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=base_url)

        def post(self, url: str, data: dict) -> dict:
            response = self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()

        def close(self):
            self.client.close()
