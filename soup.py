from bs4 import BeautifulSoup

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# find_all(name, attrs, recursive, text, **kwargs)


html_doc = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello World</h4>   
    </div>
    
    <div class="panel-body">
        <ul class="list" id="list-1">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
        
        <ul class="list list-samll" id="list-2">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
    </div>
    </div>
</div>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.select('.panel .panel-heading')) # 获取class为panel-heading的节点
# print(soup.select('ul li')) # 获取ul下的li节点
# print(soup.select('#list-2 li')) # 获取id为list-2下的li节点
# print(soup.select('ul'))    # 获取所有的ul节点
print(type(soup.select('ul')[0]))
