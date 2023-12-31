from json import dumps
from pytest_bdd import scenario, given, when, then
from tests.config import Config
from tests.fixtures import my_app_service


@scenario("users.feature", "Check log in")
def test_login(app):
    pass


@given("user opens index page")
def given_index_page(my_app_service):
    response = my_app_service.get_index()
    print(response)
    assert dumps(response) == dumps({"msg": "You are not logged in"})


@when("user logs in with credentials")
def when_login(my_app_service):
    response = my_app_service.login(Config.USER_USERNAME, Config.USER_PASSWORD)
    print(response)
    assert dumps(response, indent=4) == dumps(
        {"msg": "Logged successfully"}, indent=4
    )


@then("user successfull message is sent")
def then_login_successfully(my_app_service):
    pass


@scenario("users.feature", "Check nbp currencies")
def test_currencies(app):
    pass


@given("user not logged")
def given_not_logged():
    pass


@when("user opens currency page")
def when_login(my_app_service):
    response = my_app_service.currency()
    print(response)
    assert response.get("msg") == "ok"
    assert response.get("content")


@then("currencies are fetched")
def then_currencies_are_fetched():
    pass
