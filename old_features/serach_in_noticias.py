from old_features import LaBSKThreadListPage

__author__ = 'Javier'

from LaBSKApi.web import WebClient

webclient = WebClient("http://labsk.net/index.php?board=18.0;sort=last_post;desc")
noticias = LaBSKThreadListPage(webclient)
word = "Dungeoneer"
print "Referencias a ", word
print noticias.count(word)

print "Ok."
