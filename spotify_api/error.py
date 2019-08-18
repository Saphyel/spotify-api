class SpotifyOauthError(Exception):
    pass


class SpotifyRepositoryError(Exception):
    def __init__(self, http_status: int, body: str):
        self.http_status = http_status
        self.body = body

    def __str__(self):
        return 'http status: {0}, code:{1}'.format(str(self.http_status), self.body)
