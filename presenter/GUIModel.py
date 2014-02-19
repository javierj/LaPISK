__author__ = 'Javier'

# Untested class
class Text(object):
    def __init__(self, firsttext = None):
        self.text = []
        self.nexttext = []
        if firsttext is not None:
            self.addText(firsttext)

    def addText(self, txt):
        self.text.append(txt)

    def addNextText(self, textObj):
        self.nexttext.append(textObj)

    def __str__(self):
        return self.text.str()