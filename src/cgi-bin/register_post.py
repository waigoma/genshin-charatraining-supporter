import cgi
import sys
import io
import genshin.character as gc
import genshin.database.operation as gdo
import genshin.template.header as header

form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

template = """
<html>
<head>
    <meta charset="utf-8">
    <title>原神 -キャラ登録完了-</title>
    <style>
        {style}
    </style>
</head>
<body>
    {header}
    <div class="content">
        <h1>- キャラクター登録完了 -</h1>
        <div class="all select-block">
            {characters}
        </div>
        <div class="btn-wrapper">
            <button class="btn" onclick="location.href='/cgi-bin/index.py'">ホームへ戻る</button>
        </div>
    </div>
</body>
</html>
"""

style = """
img {
    width: 128px;
    height: auto;
    user-drag: none;
}

.btn {
    width: 50%;
}

.all {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}

.character {
    width: 200px;
    text-align: center;
}

.character h2 {
    margin: 5px 0;
}

"""


def registered_character_html(character):
    """
    :type character: gc.Character
    :param character: キャラクター情報
    :return: html
    """
    return f"""
    <div class="character">
        <h2>{character.jp_name}</h2>
        <img src="{character.chara_img}">
    </div>
    """


def registered_characters_html(characters):
    """
    :type characters: list[gc.Character]
    :param characters: キャラクター情報
    :return: html
    """
    return "".join([registered_character_html(character) for character in characters])


def register_database(character):
    """
    :type character: gc.Character
    :param character: キャラクター情報
    """
    gdo.add_character(character.jp_name, character.region, character.element, character.chara_img)


def main():
    characters = gc.get_characters(form.getlist('characters'))

    for character in characters:
        register_database(character)

    tmp = template.format(characters=registered_characters_html(characters), style=header.get_style()+style, header=header.get_header_html())
    print("Content-type: text/html\n")
    print(tmp)


main()
