import cgi
import sys
import io
from collections import OrderedDict

import genshin.character as gc
import genshin.database.operation as gdo
import genshin.ascend_calculator as gac
import genshin.talent_calculator as gtc
import genshin.template.header as header

form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

template = """
<html>
<head>
    <meta charset="utf-8">
    <title>原神 -キャラ一覧-</title>
    <style>
        {style}
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript">
        {modal_script}
    </script>
</head>
<body>
    {header}
    <div class="content">
        <h1>- 育成キャラクター 一覧 -</h1>
        {message}
        <div class="all">
            {characters}
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

ul {
    padding: 0;
}

li {
    list-style: none;
}

ul li label {
    margin-right: 5px;
    width: 75px;
    float: left;
}

table {
    width: 100%;
    border-collapse: collapse;
    background-color: #FFF;
}

th {
    background-color: #eee;
}

td, th {
    border: 2px solid #ccc;
    padding: 5px;
}

#modal-wrap {
    background: none;
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
}

.modal-box {
    position: fixed;
    width: 75%;
    max-width: 420px;
    height: 0;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    opacity: 1;
    border-radius: 3px;
    z-index: 1000;
}

.modal-inner {
    padding: 10px;
    text-align: center;
    box-sizing: border-box;
    background: rgba(0, 0, 0, 0.7);
    color: #fff;
}

.accordion-check {
    display: none;
}

.accordion-label {
    display: block;
    cursor: pointer;
    padding: 10px 10px 0 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f0f0f0;
}

.accordion-label:hover {
    background-color: #ddd;
}

.accordion-label::before {
    display: inline-block;
    width: 1.5em;
    text-align: center;
    margin-right: 0.5em;
}


.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-in-out;
    background-color: #eee;
    border: 1px solid #ccc;
    border-radius: 2px;
    width: 99%;
    margin: 0 auto;
}

.accordion-check:checked + .accordion-label + .accordion-content {
    max-height: 75%;
    overflow: auto;
}

.character {
    text-align: center;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    flex-wrap: wrap;
}

.character h2 {
    margin: 5px 0;
}

.costs {
    display: flex;
    justify-content: space-evenly;
    align-items: flex-start;
    flex-wrap: wrap;
    margin-bottom: 10px;
}

.costs h3 {
    margin: 10px 0;
    text-align: center;
}

.buttons {
    margin: 20px 0 10px 0;
}

.btn {
    font-size: 1.0rem;
    font-weight: 250;
    line-height: 1.8;
    width: 100px;
}

.btn-red {
    line-height: 1.4;
    background-color: #FF8F83;
}

.btn-red:hover {
    background-color: #FF8F83;
}

#炎 {
    background-color: #FF6F6340;
}

#水 {
    background-color: #4C92EA40;
}

#風 {
    background-color: #4CD9C840;
}

#雷 {
    background-color: #C773FF40;
}

#草 {
    background-color: #7AD84C40;
}

#氷 {
    background-color: #73CCFF40;
}

#岩 {
    background-color: #E6B32240;
}

#炎elm {
    background-color: #FF6F6360;
}

#水elm {
    background-color: #4C92EA60;
}

#風elm {
    background-color: #4CD9C860;
}

#雷elm {
    background-color: #C773FF60;
}

#草elm {
    background-color: #7AD84C60;
}

#氷elm {
    background-color: #73CCFF60;
}

#岩elm {
    background-color: #E6B32260;
}

#炎elm tr:nth-child(2n) {
    background: #FF6F6320;
}

#炎elm tr:nth-child(2n+1) {
    background: #FF6F6310;
}

#水elm tr:nth-child(2n) {
    background: #4C92EA20;
}

#水elm tr:nth-child(2n+1) {
    background: #4C92EA10;
}

#風elm tr:nth-child(2n) {
    background: #4CD9C820;
}

#風elm tr:nth-child(2n+1) {
    background: #4CD9C810;
}

#雷elm tr:nth-child(2n) {
    background: #C773FF20;
}

#雷elm tr:nth-child(2n+1) {
    background: #C773FF10;
}

#草elm tr:nth-child(2n) {
    background: #7AD84C20;
}

#草elm tr:nth-child(2n+1) {
    background: #7AD84C10;
}

#氷elm tr:nth-child(2n) {
    background: #73CCFF20;
}

#氷elm tr:nth-child(2n+1) {
    background: #73CCFF10;
}

#岩elm tr:nth-child(2n) {
    background: #E6B32220;
}

#岩elm tr:nth-child(2n+1) {
    background: #E6B32210;
}
"""

script = """
<script>
    var btn = document.getElementById('del_btn_{cname}');
    btn.addEventListener('click', function() {{
        if (window.confirm('キャラクター「{cname}」を削除しますか？')) {{
            location.href = 'http://localhost:8000/cgi-bin/character_delete.py?del={cname}';
        }}
    }})
</script>
"""

modal_script = """
    $(function() {
         var count = 2000;//表示までの時間（ミリ秒）
         setTimeout(function(){$("#modal-wrap").fadeOut(500);}, count);
    });
"""


def get_cost_html(key, value):
    """
    :param key:
    :param value:
    :return:
    """
    return f"""
    <tr>
        <td>{key}</td>
        <td>{value}</td>
    </tr>
    """


def get_ascend_costs_html(character):
    """
    :type character: gc.CharacterData
    :param character:
    :return:
    """
    temp = """
    <div class="ascend-cost">
        <h3>レベル突破素材</h3>
        {table}
    </div>
    """
    costs = gac.calc_ascend_cost(character.name, character.current_level, character.to_level)
    if costs is None:
        return temp.format(table="必要素材はありません！")

    costs = OrderedDict(sorted(costs.items()))
    if "モラ" in costs:
        costs.move_to_end("モラ", last=False)

    return temp.format(table=f"""
        <table>
        <tbody>
            <tr>
                <th>名前</th>
                <th>必要数</th>
            </tr>
            {"".join([get_cost_html(key, value) for key, value in costs.items()])}
        </tbody>
        </table>
    """)


def get_talent_costs_html(character):
    """
    :type character: gc.CharacterData
    :param character:
    :return:
    """
    temp = """
    <div class="talent-cost">
        <h3>天賦 {i} 素材</h3>
        {table}
    </div>
    """
    tmp = ""
    for i in range(len(character.current_talents)):
        costs = gtc.calc_talent_cost(character.name, character.current_talents[i], character.to_talents[i])

        if costs is None:
            tmp += temp.format(table="必要素材はありません！", i=i + 1)
            continue

        costs = OrderedDict(sorted(costs.items()))
        if "モラ" in costs:
            costs.move_to_end("モラ", last=False)

        tmp += temp.format(table=f"""
        <table>
        <tbody>
            <tr>
                <th>名前</th>
                <th>必要数</th>
            </tr>
            {"".join([get_cost_html(key, value) for key, value in costs.items()])}
        </tbody>
        </table>
        """, i=i + 1)

    return tmp


def get_all_characters_html(characters):
    return "".join([get_character_html(character) for character in characters])


def get_character_html(character):
    """
    :type character: gc.CharacterData
    :param character:
    :return:
    """
    return f"""
    <div class="select-block">
        <form action="/cgi-bin/characters.py" method="post">
            <input type="hidden" name="name" value="{character.name}">
            <input type="hidden" name="region" value="{character.region}">
            <input type="hidden" name="element" value="{character.element}">
            <input type="hidden" name="img" value="{character.img}">
            <input type="checkbox" class="accordion-check" id="{character.name}" name="{character.name}ck">
            <label class="accordion-label" id="{character.element}" for="{character.name}">
            <div class="character">
                <div class="character-view">
                    <h2>{character.name}</h2>
                    <img src="{character.img}" alt="{character.name}">
                </div>
                <div>
                    <h3>現在</h3>
                    <ul>
                        <li>
                            <label for="current_level">レベル:</label>
                            <input type="number" name="current_level" value="{character.current_level}" min="1" max="90">
                        </li>
                        <li>
                            <label for="current_talentA">天賦 1:</label>
                            <input type="number" name="current_talentA" value="{character.current_talents[0]}" min="1" max="10">
                        </li>
                        <li>
                            <label for="current_talentB">天賦 2:</label>
                            <input type="number" name="current_talentB" value="{character.current_talents[1]}" min="1" max="10">
                        </li>
                        <li>
                            <label for="current_talentC">天賦 3:</label>
                            <input type="number" name="current_talentC" value="{character.current_talents[2]}" min="1" max="10">
                        </li>
                    </ul>
                </div>
                <div>
                    <h3>目標</h3>
                    <ul>
                        <li>
                            <label for="to_level">レベル:</label>
                            <input type="number" name="to_level" value="{character.to_level}" min="1" max="90">
                        </li>
                        <li>
                            <label for="to_talentA">天賦 1:</label>
                            <input type="number" name="to_talentA" value="{character.to_talents[0]}" min="1" max="10">
                        </li>
                        <li>
                            <label for="to_talentB">天賦 2:</label>
                            <input type="number" name="to_talentB" value="{character.to_talents[1]}" min="1" max="10">
                        </li>
                        <li>
                            <label for="to_talentC">天賦 3:</label>
                            <input type="number" name="to_talentC" value="{character.to_talents[2]}" min="1" max="10">
                        </li>
                    </ul>
                </div>
                <div>
                    <div class="buttons">
                        <button class="btn" type="submit">更新</button>
                    </div>
                    <div>
                        <button id="del_btn_{character.name}" class="btn btn-red" type="button">削除</button>
                    </div>
                    {script.format(cname=character.name)}
                </div>
            </div>
            </label>
            <div class="accordion-content" id="{character.element}elm">
                <div class="costs">
                    {get_ascend_costs_html(character)}
                    {get_talent_costs_html(character)}
                </div>
            </div>
        </form>
    </div>
    """


def update_character_data():
    name = form.getvalue("name")
    region = form.getvalue("region")
    element = form.getvalue("element")
    current_level = form.getvalue("current_level")
    current_talents = [form.getvalue("current_talentA"), form.getvalue("current_talentB"),
                       form.getvalue("current_talentC")]
    to_level = form.getvalue("to_level")
    to_talents = [form.getvalue("to_talentA"), form.getvalue("to_talentB"), form.getvalue("to_talentC")]
    img = form.getvalue("img")

    gdo.update_character(name, region, element, current_level, current_talents, to_level, to_talents, img)


def main():
    update = form.getvalue("name", None)
    dname = form.getvalue("dname", None)
    is_delete = False

    if update is not None:
        update_character_data()

    if dname is not None:
        dname = f"""
        <div id="modal-wrap" class="modal-wrap">
            <div id="modal-box" class="modal-box">
                <div class="modal-inner">
                    キャラクター「{dname}」を削除しました。
                </div>
            </div>
        </div>
        """
        is_delete = True

    characters = gc.get_character_data_list(gdo.get_all_characters())
    tmp = template.format(characters=get_all_characters_html(characters), style=header.get_style()+style, header=header.get_header_html(),
                          message=dname if is_delete else "", modal_script=modal_script if is_delete else "")

    print("Content-type: text/html\n")
    print(tmp)


main()
