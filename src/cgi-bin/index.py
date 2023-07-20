import sys
import io
import genshin.template.header as header

# index ページを表示するだけの CGI スクリプト
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

template = """
<html>
<head>
    <meta charset="utf-8">
    <title>原神 -キャラ育成計画書-</title>
    <style>
        {style}
    </style>
</head>
<body>
    {header}
    <div class="content">
        <h1>原神 - キャラクター育成サポート -</h1>
        <p>この CGI スクリプトは、原神のキャラクター育成をサポートするものです。</p>
        <p>育てたいキャラクターを DB に保存することができるため、後から見るのが容易です。</p>
        <div class="all">
            <div>
                <h2>- キャラ登録編 -</h2>
                <ul>
                    <li>登録ページへ行く。</li>
                    <li>登録したいキャラクターを選択。</li>
                    <li>登録ボタンを押す。</li>
                    <li>登録が完了したキャラが表示される。</li>
                </ul>
                <div class="btn-wrapper">
                    <button class="btn" onclick="location.href='/cgi-bin/register.py'">登録ページへ行く</button>
                </div>
            </div>
            <div>
                <h2>- 育成キャラ一覧閲覧編 -</h2>
                <ul>
                    <li>育成キャラ一覧ページへ行く。</li>
                    <li>登録されているキャラクターが一覧表示される。</li>
                    <li>キャラクターに現在と目標のレベルが設定できる。</li>
                    <li>キャラクターを選択すれば必要アイテムが表示できる。</li>
                </ul>
                <div class="btn-wrapper">
                    <button class="btn" onclick="location.href='/cgi-bin/characters.py'">育成キャラ一覧ページへ行く</button>
                </div>
            </div>
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
    width: 100%;
}

.all {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    margin: 0 auto 20px auto;
}

.all h2 {
    text-align: center;
}

.character {
    width: 200px;
    text-align: center;
}

.character h2 {
    margin: 5px 0;
}

"""

print("Content-type: text/html\n")
print(template.format(style=header.get_style()+style, header=header.get_header_html()))
