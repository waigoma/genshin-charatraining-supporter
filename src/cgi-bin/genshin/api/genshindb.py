import enum
import json

import requests


API_URL = 'https://genshin-db-api.vercel.app/api/'


class Region(enum.Enum):
    MONDSTADT = 'モンド'
    LIYUE = '璃月'
    INAZUMA = '稲妻'
    SUMERU = 'スメール'


# https://genshin-db-api.vercel.app/api/characters?query=スメール&matchCategories=true&queryLanguages=japanese&resultLanguage=japanese
def get_characters_by_region(region):
    res = requests.get(
        f'{API_URL}characters',
        params={
            'query': region,
            'matchCategories': 'true',
            'queryLanguages': 'japanese',
            'resultLanguage': 'japanese'
        }
    )
    res.encoding = 'utf-8'
    return res.text


# https://genshin-db-api.vercel.app/api/characters?query=ナヒーダ&queryLanguages=japanese&resultLanguage=japanese
def get_cdata_by_cname(name):
    res = requests.get(
        f'{API_URL}characters',
        params={
            'query': name,
            'queryLanguages': 'japanese',
            'resultLanguage': 'japanese'
        }
    )
    res.encoding = 'utf-8'
    return json.loads(res.text)


# https://genshin-db-api.vercel.app/api/talents?query=ナヒーダ&matchCategories=true&queryLanguages=japanese&resultLanguage=japanese
def get_tdata_by_cname(name):
    res = requests.get(
        f'{API_URL}talents',
        params={
            'query': name,
            'matchCategories': 'true',
            'queryLanguages': 'japanese',
            'resultLanguage': 'japanese'
        }
    )
    res.encoding = 'utf-8'
    return json.loads(res.text)
