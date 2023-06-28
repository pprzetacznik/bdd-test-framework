from pytest import fixture
from tests.config import Config
from tests.my_app_service import Server, MyAppService


@fixture
def my_app_service(app):
    server = Server(server_url=Config.SERVER_URL)
    return MyAppService(server)
