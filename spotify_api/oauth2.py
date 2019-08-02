import base64
import os
import time
from dataclasses import dataclass, field

import requests


class SpotifyOauthError(Exception):
    pass


@dataclass
class Token:
    access_token: str
    token_type: str
    expires_in: int
    scope: str
    expires_at: int = field(init=False)

    def __post_init__(self):
        self.expires_at = int(time.time()) + self.expires_in

    def is_expired(self) -> bool:
        return self.expires_at - int(time.time()) < 60


@dataclass
class Client:
    id: str
    secret: str
    proxies: dict

    def token(self) -> str:
        return base64.b64encode(str(self.id + ':' + self.secret).encode('ascii')).decode('ascii')


class SpotifyOauth:
    OAUTH_URL = 'https://accounts.spotify.com/api/token'

    def post_credentials(self, client: Client) -> Token:
        payload = {'grant_type': 'client_credentials'}
        headers = {'Authorization': 'Basic ' + client.token()}
        response = requests.post(self.OAUTH_URL, data=payload, headers=headers, verify=True, proxies=client.proxies)
        if response.status_code != 200:
            raise SpotifyOauthError(response.reason)
        return Token(**response.json())


class SpotifyClientCredentials:
    def __init__(self, client_id: str = None, client_secret: str = None, proxies: dict = None):
        if not client_id:
            client_id = os.getenv('SPOTIFY_CLIENT_ID')
            if not client_id:
                raise SpotifyOauthError('No client id')

        if not client_secret:
            client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
            if not client_secret:
                raise SpotifyOauthError('No client secret')

        self.client = Client(client_id, client_secret, proxies)
        self.token_info = None

    def get_access_token(self) -> str:
        if self.token_info and not self.token_info.is_expired():
            return self.token_info.access_token

        self.token_info = SpotifyOauth().post_credentials(self.client)
        return self.token_info.access_token
