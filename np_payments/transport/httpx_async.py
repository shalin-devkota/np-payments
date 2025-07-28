import httpx


class AsyncHTTPTransport:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url)

        async def post(self, url: str, data: dict) -> dict:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()

        async def close(self):
            await self.client.aclose()
