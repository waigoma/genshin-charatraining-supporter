def get_header_html():
    """
    :return: header Template HTML
    """
    return f"""
    <header>
    <div class="header select-block">
        <h1>
            <a href="/cgi-bin/index.py">原神育成サポーター</a>
        </h1>
        <nav class="pc-nav">
            <ul>
                <li><a href="/cgi-bin/index.py">ホーム</a></li>
                <li><a href="/cgi-bin/register.py">登録</a></li>
                <li><a href="/cgi-bin/characters.py">一覧</a></li>
            </ul>
        </nav>
    </div>
    </header>
    """


def get_style():
    """
    :return: Template CSS
    """
    return """
    header {
        border-bottom: 1px solid #aaa;
        position: sticky;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #fcfcfc;
        z-index: 100;
    }
    
    header h1 {
        font-weight: normal;
        font-size: 1.75rem;
    }
    
    img {
        border-bottom: 1px solid #aaa;
        user-select: none; /* CSS3 */
        -moz-user-select: none; /* Firefox */
        -webkit-user-select: none; /* Safari、Chromeなど */
        -ms-user-select: none; /* IE10かららしい */
        user-drag: none;
        -webkit-user-drag: none;
        -moz-user-select: none;
    }
    
    .select-block {
        user-select: none; /* CSS3 */
        -moz-user-select: none; /* Firefox */
        -webkit-user-select: none; /* Safari、Chromeなど */
        -ms-user-select: none; /* IE10かららしい */
        user-drag: none;
        -webkit-user-drag: none;
        -moz-user-select: none;
    }
    
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0 0 0;
        width: 75%;
        margin: 0 auto;
    }
    
    header h1 {
        margin: 0 0 5px 0;
    }
    
    header h1 a {
        color: #1e1e1e;
        text-decoration: none;
    }
    
    header nav ul {
        display: flex;
        justify-content: space-between;
        align-items: center;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    header nav ul li {
        margin: 0 10px;
    }
    
    header nav ul li a {
        color: #1e1e1e;
        text-decoration: none;
    }
    
    @media screen and (max-width: 768px) {
        header {
            flex-direction: column;
        }
        
        header nav {
            margin-top: 10px;
        }
        
        header nav ul {
            flex-direction: column;
        }
        
        header nav ul li {
            margin: 10px 0;
        }
    }
    
    body {
        margin: 0;
        background-color: #F5F6F4;
        color: #1e1e1e;
        font-family: 'Noto Sans JP', sans-serif;
    }
    
    .content {
        width: 75%;
        margin: 5px auto;
        padding: 5px 0;
        background-color: #fafafa;
        border-radius: 10px;
    }
    
    .content h1, p {
        text-align: center;
    }
    
    .all {
        width: 98%;
        max-width: 1100px;
        margin: 0 auto;
    }
    
    .btn-wrapper {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    
    .btn {
        cursor: pointer;
        vertical-align: middle;
        text-align: center;
        text-decoration: none;
        
        color: #2f2f2f;
        background-color: #AADDDD;
        border-radius: 5vh;
        font-size: 1.4rem;
        font-weight: 500;
        line-height: 1.5;
        
        -webkit-transition: all 0.3s;
        transition: all 0.3s;
        letter-spacing: 0.1em;
        border-radius: 0.5rem;
        border-width: 1px;
    }
    
    .btn:hover {
      color: #fff;
      background: #AADDDD;
    }
    """
