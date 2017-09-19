from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    return texts


type = raw_input("TYPE(E.g: r/w/m): ");

html = urllib.urlopen("http://ukshop4malaysia.com/anonymous/gameMode&type="+type+" ").read()
print(text_from_html(html))

