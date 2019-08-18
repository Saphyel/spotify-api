import base64
import time
from dataclasses import dataclass, field
from typing import List


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


@dataclass(order=True)
class Image:
    url: str
    height: int
    width: int


@dataclass(order=True)
class Album:
    id: str
    name: str
    external_urls: dict
    href: str
    uri: str
    type: str
    available_markets: List[str]
    images: list
    total_tracks: int
    release_date: str
    release_date_precision: str
    artists: list
    album_type: str
    popularity: int = None
    tracks: list = None
    copyrights: List[dict] = None
    genres: List[str] = None
    label: str = None
    external_ids: dict = None


@dataclass(order=True)
class Artist:
    id: str
    name: str
    external_urls: dict
    href: str
    uri: str
    type: str
    images: list = None
    popularity: int = None
    followers: list = None
    genres: List[str] = None


@dataclass(order=True)
class Track:
    id: str
    name: str
    external_urls: dict
    href: str
    uri: str
    type: str
    duration_ms: int
    preview_url: str
    available_markets: List[str]
    explicit: bool
    track_number: int
    disc_number: int
    artists: list
    is_local: bool
    album: Album = None
    popularity: int = None
    external_ids: dict = None