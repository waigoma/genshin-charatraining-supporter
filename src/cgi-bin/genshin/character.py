from dataclasses import dataclass
from .api import genshindb as gdb


@dataclass
class Character:
    jp_name: str
    region: str
    element: str
    chara_img: str


@dataclass
class CharacterData:
    name: str
    region: str
    element: str
    current_level: int
    current_talents: list
    to_level: int
    to_talents: list
    img: str


def create_character_by_json(json_data):
    """
    Create character by json data.
    :param json_data: json data from genshin database api
    :return: character
    """
    jp_name = json_data['name']
    region = json_data['region']
    element = json_data['element']
    try:
        chara_img = json_data['images']['icon']
    except KeyError:
        chara_img = json_data['images']['hoyolab-avatar']

    return Character(jp_name, region, element, chara_img)


def get_character(name):
    """
    Get character by name.
    :param name: character name
    :return: character
    """
    json_data = gdb.get_cdata_by_cname(name)
    return create_character_by_json(json_data)


def get_characters(names):
    """
    Get characters by names.
    :param names: character names
    :return: characters
    """
    return [get_character(name) for name in names]


def get_all_characters(ignores=None):
    """
    Get all characters.
    :param ignores: ignore character names
    :return: characters
    """
    characters = {}
    for region in gdb.Region:
        characters[region.value] = []
        for cname in eval(gdb.get_characters_by_region(region.value)):
            if ignores is not None and cname in ignores:
                continue
            json_data = gdb.get_cdata_by_cname(cname)
            characters[region.value].append(create_character_by_json(json_data))
    return characters


def create_character_data(character_data):
    """
    Create character data.
    :param character_data: character data
    :return: character data
    """
    return CharacterData(character_data[0], character_data[1], character_data[2], character_data[3],
                         [character_data[4], character_data[5], character_data[6]], character_data[7],
                         [character_data[8], character_data[9], character_data[10]], character_data[11])


def get_character_data(character_data):
    """
    Get character data.
    :param character_data: character data
    :return: character data
    """
    return create_character_data(character_data)


def get_character_data_list(character_datas):
    """
    Get character data list by name.
    :param character_datas: character data list
    :return: character datas
    """
    return [get_character_data(character_data) for character_data in character_datas]
