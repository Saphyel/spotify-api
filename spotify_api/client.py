from spotify_api.model import Track, Album, Artist, Client
from spotify_api.repository import SpotifyRepository, OauthRepository
from spotify_api.service import TokenService, TrackService, AlbumService, ArtistService
from spotify_api.transformer import TrackTransformer, ArtistTransformer, AlbumTransformer, ClientTransformer, \
    TokenTransformer


class Spotify:
    def __init__(self, auth: TokenService):
        self.auth = auth

    def get_token(self):
        return self.auth.get_access_token()

    def get_track(self, track_id: str) -> Track:
        return TrackService(SpotifyRepository(), TrackTransformer).get_one(track_id, self.auth.get_access_token())

    def get_album(self, album_id: str) -> Album:
        return AlbumService(SpotifyRepository(), AlbumTransformer).get_one(album_id, self.auth.get_access_token())

    def get_artist(self, artist_id: str) -> Artist:
        return ArtistService(SpotifyRepository(), ArtistTransformer).get_one(artist_id, self.auth.get_access_token())


class SpotifyClientCredentials:
    def __init__(self, client_id: str, client_secret: str, proxies=None):
        self.id = client_id
        self.secret = client_secret
        self.proxies = proxies

    def get_client(self) -> Client:
        return ClientTransformer.transform({'id': self.id, 'secret': self.secret, 'proxies': self.proxies})


def spotify_builder(client_id: str, client_secret: str) -> Spotify:
    client = SpotifyClientCredentials(client_id, client_secret)
    token_info = TokenService(client.get_client(), TokenTransformer, OauthRepository())
    return Spotify(token_info)
