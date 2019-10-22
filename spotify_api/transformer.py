__strict__ = True

from dataclasses import dataclass

from spotify_api.model import Track, Image, Album, Artist, Token, Client, Playlist, AudioFeatures


class Transformer:
    @staticmethod
    def transform(json: dict) -> dataclass:
        raise NotImplementedError


class ClientTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Client:
        return Client(**json)


class TokenTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Token:
        return Token(**json)


class ImageTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Image:
        return Image(**json)


class AlbumTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Album:
        json['images'] = [ImageTransformer.transform(pic) for pic in json['images']]
        json['artists'] = [ArtistTransformer.transform(artist) for artist in json['artists']]
        if 'tracks' in json:
            json['tracks'] = [TrackTransformer.transform(track) for track in json['tracks']['items']]

        return Album(**json)


class ArtistTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Artist:
        if 'images' in json:
            json['images'] = [ImageTransformer.transform(pic) for pic in json['images']]
        return Artist(**json)


class TrackTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Track:
        if 'album' in json:
            json['album'] = AlbumTransformer.transform(json['album'])
        json['artists'] = [ArtistTransformer.transform(artist) for artist in json['artists']]

        return Track(**json)


class AudioFeaturesTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> AudioFeatures:
        return AudioFeatures(**json)


class PlaylistTransformer(Transformer):
    @staticmethod
    def transform(json: dict) -> Playlist:
        return Playlist(**json)
