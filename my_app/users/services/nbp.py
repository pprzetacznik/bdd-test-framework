from dataclasses import dataclass
import requests


@dataclass
class Server:
    hostname: str

    def get(self, endpoint: str) -> dict:
        response = requests.get(f"https://{self.hostname}/{endpoint}")
        return response.json()


class NBPService:
    def __init__(self, server: Server):
        self.server = server

    def get(self) -> dict:
        return self.server.get("api/exchangerates/tables/A/?format=json")
