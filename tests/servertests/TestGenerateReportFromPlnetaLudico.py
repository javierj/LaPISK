__author__ = 'Javier'

import unittest
from LaBSKApi.reports import ReportBuilder
from LaBSKApi.MongoDB import MongoDB



class TestCase(unittest.TestCase):
    """ This test acse tries to generate a report from planeta ludico
    using the same report objects than used fro LaBSK.

    Expected result is something like this:
    04/02/ambassadors-nueva-expansion-para-madeira/?utm_source=rss&utm_medium=rss&utm_campaign=ambassadors-nueva-expansion-para-madeira', u'title': u'The Ambassadors nueva expansi\xf3n para Madeira'}
{u'date': u'2 abril, 2014', u'source': u'Wulfgar73', u'_id': ObjectId('533beceec6a54a16f0a20141'), u'link': u'http://losamigosdecatan.blogspot.com/2014/04/naufragos-1-4-jugadores.html', u'title': u'NAUFRAGOS (1-4 Jugadores)'}
{u'date': u'2 abril, 2014', u'source': u'CUBO Magazine', u'_id': ObjectId('533beceec6a54a16f0a20142'), u'link': u'http://cubomagazine.com/?p=13146', u'title': u'Embajadores en Madeira'}



    """



    def test_planeta_ludico_report(self):
        db = MongoDB(col="blogs")
        madeira = {'name': 'Planeta Ludico demo',
                      'keywords': ["madeira"]}
        rb = ReportBuilder(db)
        result = rb.build_report(madeira)
        print result
        """
        Este es el resultado:
{'report_date': '2014-04-02, 14:12', 'madeira': [
    {'last_msg_date': 'No messages',
      u'title': u'The Ambassadors nueva expansi\xf3n para Madeira', 'creation_date': 'No messages',
      u'source': u'Daniel Mayoralas',
       u'link': u'http://ludonoticias.com/2014/04/02/ambassadors-nueva-expansion-para-madeira/?utm_source=rss&utm_medium=rss&utm_campaign=ambassadors-nueva-expansion-para-madeira',
       u'date': u'2 abril, 2014', u'_id': ObjectId('533beceec6a54a16f0a20140')},
    {'last_msg_date': 'No messages', u'title': u'Embajadores en Madeira', 'creation_date': 'No messages', u'source': u'CUBO Magazine', u'link': u'http://cubomagazine.com/?p=13146', u'date': u'2 abril, 2014', u'_id': ObjectId('533beceec6a54a16f0a20142')}],
    'title': 'Result for report Planeta Ludico demo'}

    Creo que s epuede utilizar
"""
        self.assertTrue(False)





if __name__ == '__main__':
    unittest.main()
