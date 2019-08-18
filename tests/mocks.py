class MockResponse:
    def __init__(self, code: int, result: dict):
        self.status_code = code
        self._content = result

    @property
    def ok(self) -> bool:
        return True

    @property
    def text(self) -> str:
        return 'error'

    def json(self):
        return self._content
