__author__ = 'Javier'

from LaBSKApi.web import WebClient
from features.steps.LaBSKThreadListPage import LaBSKThreadListPage

webclient = WebClient("http://labsk.net/index.php?board=18.0;sort=last_post;desc")
noticias = LaBSKThreadListPage(webclient)
word = "Dungeoneer"
print "Referencias a ", word
print noticias.count(word)

print "Ok."
