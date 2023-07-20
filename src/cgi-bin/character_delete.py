import cgi
import sys
import io
import genshin.database.operation as gdo

form = cgi.FieldStorage()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

template = """
<html>
<head>
    <meta charset="utf-8">
    <script type="text/javascript">
        location.replace('/cgi-bin/characters.py?dname={name}');
    </script>
</head>
<body>
    <p>Deleting...</p>
</body>
</html>
"""


def delete_character_data(name):
    gdo.delete_character(name)


def main():
    name = form.getvalue("del")
    delete_character_data(name)

    print("Content-type: text/html\n")
    print(template.format(name=name))


main()
