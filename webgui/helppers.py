__author__ = 'Javier'


class GenerateHTMLFromText(object):
    """ This class generaes HTML frm a WebGUI.Text object
    """

    def html_from(self, text, lines = 1):
        result = "<p>" + text.text[0]
        for i in range (1, lines):
            result += " / " + text.text[i]
        return  result + "</p>"

