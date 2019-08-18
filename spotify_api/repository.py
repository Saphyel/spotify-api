import requests

from spotify_api.error import SpotifyOauthError, SpotifyRepositoryError
from spotify_api.model import Client


class OauthRepository:
    OAUTH_URL = 'https://accounts.spotify.com/api/token'

    def post_credentials(self, client: Client) -> dict:
        payload = {'grant_type': 'client_credentials'}
        headers = {'Authorization': 'Basic ' + client.token()}
        response = requests.post(self.OAUTH_URL, data=payload, headers=headers, verify=True, proxies=client.proxies)
        if not response.ok:
            raise SpotifyOauthError(response.reason)
        return response.json()


class SpotifyRepository:
    BASE_URL = 'https://api.spotify.com/v1/'

    @staticmethod
    def _build_header(token) -> dict:
        return {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

    def get_response(self, uri: str, token: str) -> dict:
        response = requests.get(self.BASE_URL + uri, headers=self._build_header(token))
        if not response.ok:
            raise SpotifyRepositoryError(response.status_code, response.json())
        return response.json()
