__author__ = 'Javier'

import unittest
from LaBSKApi.reports import ReportBuilder
from LaBSKApi.MongoDB import MongoDB



class TestCase(unittest.TestCase):
    """ This test acse tries to generate a report from planeta ludico
    using the same report objects than used fro LaBSK.

    """

    def test_planeta_ludico_report(self):
        db = MongoDB(col="blogs")
        madeira = {'name': 'Planeta Ludico demo',
                      'keywords': ["madeira"]}
        rb = ReportBuilder(db)
        result = rb.build_report(madeira)
        print result
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
