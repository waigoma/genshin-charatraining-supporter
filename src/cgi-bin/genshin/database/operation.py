import sqlite3


def connect_db():
    """
    Connect to database.
    :return: connection, cur
    """
    connection = sqlite3.connect("./cgi-bin/genshin/database/genshin_user.sqlite3")
    cur = connection.cursor()
    return connection, cur


def close_db(connection):
    """
    Close database.
    :param connection: database connection
    """
    connection.close()


def add_character_full(character_name, region, element, current_level, current_talents, to_level, to_talents, img):
    """
    Add user to database by full information.
    :param element:
    :param character_name: キャラクター名
    :param region: 地域名
    :param current_level: 現在のレベル
    :param current_talents: 現在の天賦 1,2,3 のレベル
    :param to_level: 目標レベル
    :param to_talents: 天賦 1,2,3 の目標レベル
    :param img: キャラクター画像
    """
    connection, cur = connect_db()
    try:
        cur.execute("insert into user values (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (character_name, region, element, current_level, current_talents[0], current_talents[1], current_talents[2], to_level, to_talents[0], to_talents[1], to_talents[2], img))
        connection.commit()
        print("Character Added.")
    except sqlite3.IntegrityError:
        print("Character already exists.")

    close_db(connection)


def add_character(character_name, region, element, img):
    """
    Add user to database by minimum information.
    :param element: 元素
    :param character_name: キャラクター名
    :param region: 地域名
    :param img: キャラクター画像
    """
    add_character_full(character_name, region, element, 1, [1, 1, 1], 1, [1, 1, 1], img)


def get_character(character_name):
    """
    Get character from database by character name.
    :param character_name: キャラクター名
    :return: character
    """
    connection, cur = connect_db()
    cur.execute("select * from user where character_name=?", (character_name,))
    character = cur.fetchone()
    close_db(connection)
    return character


def get_all_characters():
    """
    Get all characters from database.
    :return: characters
    """
    connection, cur = connect_db()
    cur.execute("select * from user")
    characters = cur.fetchall()
    close_db(connection)
    return characters


def get_all_characters_name():
    """
    Get all characters' name from database.
    :return: characters_name
    """
    connection, cur = connect_db()
    cur.execute("select character_name from user")
    characters = cur.fetchall()
    character_names = [character_name[0] for character_name in characters]
    close_db(connection)
    return character_names


def update_character(character_name, region, element, current_level, current_talents, to_level, to_talents, img):
    """
    Update character information.
    :param element: 元素
    :param character_name: キャラクター名
    :param region: 地域名
    :param current_level: 現在のレベル
    :param current_talents: 現在の天賦 1,2,3 のレベル
    :param to_level: 目標レベル
    :param to_talents: 天賦 1,2,3 の目標レベル
    :param img: キャラクター画像
    """
    connection, cur = connect_db()
    cur.execute("update user set region=?, element=?, current_level=?, current_talentA=?, current_talentB=?, current_talentC=?, to_level=?, to_talentA=?, to_talentB=?, to_talentC=?, img=? where character_name=?",
                (region, element, current_level, current_talents[0], current_talents[1], current_talents[2], to_level, to_talents[0], to_talents[1], to_talents[2], img, character_name))
    connection.commit()
    print("Character Updated.")
    close_db(connection)


def delete_character(character_name):
    """
    Delete user from database by character name.
    :param character_name: キャラクター名
    """
    connection, cur = connect_db()
    cur.execute("delete from user where character_name=?", (character_name,))
    connection.commit()
    print("Character Deleted.")
    close_db(connection)
