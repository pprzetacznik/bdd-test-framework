from json import dumps
from my_app.users.services.nbp import NBPService


def test_currency():
    class Server:
        def get(self, endpoint):
            return {"status": "ok"}

    nbp_service = NBPService(Server())
    print(dumps(nbp_service.get()))
