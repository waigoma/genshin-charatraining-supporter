import sqlite3


def init():
    # connect to database
    connection = sqlite3.connect("genshin_user.sqlite3")
    cur = connection.cursor()

    # initialize table
    cur.execute("drop table if exists user")
    cur.execute("create table user ("
                "character_name text primary key ,"  # キャラクター名
                "region text ,"  # 地域
                "element text ,"  # 元素
                "current_level integer ,"  # 現在のレベル
                "current_talentA integer ,"  # 現在の天賦Aレベル
                "current_talentB integer ,"  # 現在の天賦Bレベル
                "current_talentC integer ,"  # 現在の天賦Cレベル
                "to_level integer ,"  # 目標レベル
                "to_talentA integer ,"  # 目標天賦Aレベル
                "to_talentB integer ,"  # 目標天賦Bレベル
                "to_talentC integer ,"  # 目標天賦Cレベル
                "img text"  # キャラクター画像
                ")")

    connection.commit()
    connection.close()
    print("Database Initialized.")


init()
