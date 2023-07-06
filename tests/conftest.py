from time import sleep
from threading import Thread
from pytest import fixture
from my_app.server import create_app
from my_app.settings import TestConfig


def my_thread(app):
    print("Running server")
    app.run(host="127.0.0.1", port=8003, use_reloader=False)
    print("Stop server")


@fixture(autouse=True, scope="session")
def app():
    app = create_app(TestConfig)
    Thread(target=my_thread, args=(app,), daemon=True).start()

    ctx = app.test_request_context()
    ctx.push()
    sleep(3)

    yield app

    ctx.pop()
