# genshin-charatraining-supporter
原神のキャラクター育成素材を一覧表示させる CGI アプリケーション。

原神のキャラクターを登録して、レベル突破と天賦の育成レベルを指定すると必要素材一覧を確認できます。  

API を使用しているので、キャラクターが増えても対応可能です。  
DB に保存するので、いつでも登録されたキャラクターを見返すことが可能です。

# 環境
Python 3.10  

requirements.txt にインストールが必要なライブラリが記されています。  
`pip install -r requirements.txt`

# 使い方
このソースをダウンロードして src > server.py を起動します。  
localhost:8000/cgi-bin/index.py をブラウザで開きます。  
以上です。

# 使用 API
[genshin-db-api](https://github.com/theBowja/genshin-db-api)

## commit 少ない。
学校の課題で作ったものを移植してきたので commit 数は少なくなっています。
