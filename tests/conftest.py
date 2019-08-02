from pytest import fixture


@fixture(scope="class")
def token() -> dict:
    yield {'access_token': 'token', 'token_type': 'Bearer', 'expires_in': 3600, 'scope': ''}
