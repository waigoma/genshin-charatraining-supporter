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
    <title>原神 -キャラ登録-</title>
    <style>
        {style}
    </style>
</head>
<body>
    {header}
    <div class="content">
        <h1>- キャラクター 登録 -</h1>
        <div class="all">
            <form action="/cgi-bin/register_post.py" method="post" class="select-block">
            {characters}
            <div class="btn-wrapper">
                <button type="submit" class="btn">登録</button>
            </div>
            </form>
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

form {
    margin: 0;
}

.btn {
    width: 50%;
}

.reg-div {
    width: auto;
    height: auto;
    margin: 10px 0;
}

.accordion-check {
    display: none;
}

.accordion-label {
    display: block;
    cursor: pointer;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #eee;
}

.accordion-label:hover {
}

.accordion-label::before {
    content: "+";
    display: inline-block;
    width: 1.5em;
    text-align: center;
    margin-right: 0.5em;
}

.accordion-check:checked + .accordion-label::before {
    content: "-";
}

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-in-out;
}

.accordion-check:checked + .accordion-label + .accordion-content {
    max-height: 75%;
    overflow: auto;
}

.region {
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

.character-box {
    width: auto;
    height: auto;
    margin: 0;
}

.character-check {
    display: none;
}

.character-label {
    display: block;
    cursor: pointer;
    margin: 5px;
    border: 2px solid #ccc;
    border-radius: 5px;
}

.character-check:checked + .character-label {
    border: 2px solid #5AFF19;
    border-radius: 5px;
}

.モンド {
    background-color: #4CD9C830;
}

.璃月 {
    background-color: #E6B32230;
}

.稲妻 {
    background-color: #C773FF30;
}

.スメール {
    background-color: #7AD84C30;
}

.モンドreg {
    background: #4CD9C810;
}

.璃月reg {
    background: #E6B32210;
}

.稲妻reg {
    background: #C773FF10;
}

.スメールreg {
    background: #7AD84C10;
}
"""


def get_chara_html(chara):
    """
    キャラクターの情報を HTML に変換する。
    :type chara: gc.Character
    :param chara: キャラクターの情報
    :return: キャラクター部分の HTML
    """
    return f"""
    <div class="character-box">
    <input type="checkbox" name="characters" id="{chara.jp_name}" value="{chara.jp_name}" class="character-check">
    <label for="{chara.jp_name}" class="character-label">
        <div class="character">
            <h2>{chara.jp_name}</h2>
            <img src="{chara.chara_img}" alt="{chara.jp_name}">
        </div>
    </label>
    </div>
    """


def get_region_html(region, characters):
    """
    地域ごとにまとまった HTML を返す。
    :param region: 地域
    :param characters: キャラクターのリスト
    :return: 地域ごとにまとまった HTML
    """
    return f"""
    <div class="reg-div">
        <input type="checkbox" id="{region}" class="accordion-check">
        <label class="accordion-label {region}" for="{region}">{region}</label>
        <div class="region accordion-content {region}reg">
            {"".join([get_chara_html(chara) for chara in characters])}
        </div>
    </div>
    """


def get_all_characters_html(characters):
    """
    全てのキャラクターの HTML を返す。
    :param characters: キャラクターのリスト
    :return: 全てのキャラクターの HTML
    """
    return "".join([get_region_html(region, characters[region]) for region in characters])


def main():
    characters = gc.get_all_characters(gdo.get_all_characters_name())
    tmp = template.format(characters=get_all_characters_html(characters), style=header.get_style()+style, header=header.get_header_html())

    print("Content-type: text/html\n")
    print(tmp)


main()
