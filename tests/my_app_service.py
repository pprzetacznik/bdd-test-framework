import requests


class Server:
    def __init__(self, server_url: str) -> None:
        self.server_url = server_url

    def get(self, endpoint: str) -> dict:
        url = f"{self.server_url}{endpoint}"
        return requests.get(self._prepare_url(endpoint))

    def post(self, endpoint: str, data: dict = None) -> dict:
        response = requests.post(
            self._prepare_url(endpoint),
            json=data,
            headers=self._prepare_headers(),
        )
        return response

    def _prepare_url(self, endpoint: str) -> str:
        return f"{self.server_url}{endpoint}"

    def _prepare_headers(self) -> dict:
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }
        return headers


class MyAppService:
    def __init__(self, server: Server) -> None:
        self.server = server

    def get_index(self):
        result = self.server.get("/")
        return result.json()


    def login(self, username: str, password: str) -> dict:
        result = self.server.post(
            "/login", data={"username": username, "password": password}
        )
        return result.json()
