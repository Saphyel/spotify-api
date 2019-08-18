from spotify_api.model import Track, Artist, Album, Client
from spotify_api.repository import SpotifyRepository, OauthRepository
from spotify_api.transformer import Transformer


class TokenService:
    def __init__(self, client: Client, transformer: Transformer, repository: OauthRepository):
        self.client = client
        self.transformer = transformer
        self.repository = repository
        self.token = None

    def get_access_token(self) -> str:
        if self.token and not self.token.is_expired():
            return self.token.access_token

        self.token = self.transformer.transform(self.repository.post_credentials(self.client))

        return self.token.access_token


class AlbumService:
    def __init__(self, repository: SpotifyRepository, transformer: Transformer):
        self.repository = repository
        self.transformer = transformer

    def get_one(self, uri: str, token: str) -> Album:
        return self.transformer.transform(self.repository.get_response('albums/' + uri, token))


class ArtistService:
    def __init__(self, repository: SpotifyRepository, transformer: Transformer):
        self.repository = repository
        self.transformer = transformer

    def get_one(self, uri: str, token: str) -> Artist:
        return self.transformer.transform(self.repository.get_response('artists/' + uri, token))


class TrackService:
    def __init__(self, repository: SpotifyRepository, transformer: Transformer):
        self.repository = repository
        self.transformer = transformer

    def get_one(self, uri: str, token: str) -> Track:
        return self.transformer.transform(self.repository.get_response('tracks/' + uri, token))
