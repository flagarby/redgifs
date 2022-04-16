"""
The MIT License (MIT)

Copyright (c) 2022-present scrazzz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class URL:
    __slots__ = ('sd', 'hd', 'poster', 'thumbnail', 'vthumbnail')

    sd: str
    hd: str
    poster: str
    thumbnail: str
    vthumbnail: str

@dataclass
class Gif:
    __slots__ = (
        'id', 'create_date', 'has_audio', 'width', 'height',
        'likes', 'tags', 'verified', 'views', 'duration',
        'published', 'urls', 'username', 'type', 'avg_color',
    )

    id: int
    create_date: int
    has_audio: bool
    width: int
    height: int
    likes: int
    tags: List[str]
    verified: bool
    views: int
    duration: int
    published: bool
    urls: URL
    username: str
    type: int
    avg_color: str
    # gallery

@dataclass
class User:
    __slots__ = (
        'creation_time', 'description', 'followers', 'following', 'gifs',
        'name', 'profile_image_url', 'profile_url', 'published_collections', 'published_gifs',
        'status', 'subscription', 'url', 'username', 'verified',
        'views', 'poster', 'preview', 'thumbnail',
    )

    creation_time: int
    description: Optional[str]
    followers: int
    following: int
    gifs: int
    name: str
    profile_image_url: str
    profile_url: str
    published_collections: int
    published_gifs: int
    status: str
    subscription: int
    url: str
    username: str
    verified: bool
    views: int
    poster: Optional[str]
    preview: Optional[str]
    thumbnail: Optional[str]

@dataclass
class SearchResult:
    __slots__ = (
        'searched_for', 'page', 'pages', 'total', 'gifs', 'users', 'tags',
    )

    searched_for: str
    page: int
    pages: int
    total: int
    gifs: List[Gif]
    users: List[User]
    tags: List[str]

@dataclass
class CreatorsResult:
    __slots__ = (
        'items', 'pages', 'page', 'total'
    )

    items: List[User]
    pages: int
    page: int
    total: int
