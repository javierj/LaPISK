__author__ = 'Javier'


# Untested class
class Text(object):

    def __init__(self, firsttext=None):
        self.text = []
        self.nexttext = []
        if firsttext is not None:
            self.addText(firsttext)

    def get_text(self):
        return self.text

    def addText(self, txt):
        self.text.append(txt)

    def addNextText(self, textObj):
        self.nexttext.append(textObj)

    def insert_br(self, text):
        """ Replaces \n for <br/>
        """
        result = text.replace("\n", "<br/>")
        return result

    def change_newline_in_report(self, keywords, report):
        for keyword in keywords:
            new_threads = list()
            #print keywords
            #print report
            threads = report[keyword]
            for thread in threads:
                new_msgs = list()
                #print thread
                if 'msgs' in thread:
                    for msg in thread['msgs']:
                        new_msg = msg.copy()
                        new_msg['body'] = self.insert_br(msg['body'])
                        new_msgs.append(new_msg)
                    thread['msgs'] = new_msgs
                new_threads.append(thread)
            report[keyword] = new_threads

    def __str__(self):
        return str(self.text)


class Table:
    """ Models an HTML table or grid
    """

    @property
    def title(self):
        return "2014-3-26"

    def cell(self, index):
        return u'0'