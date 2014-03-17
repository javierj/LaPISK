__author__ = 'Javier'

import unittest
from LaBSKApi.modelobjects import ReportModel, ThreadModel, MsgListModel, MsgModel
from tests.Harness import Reports
from datetime import datetime


class TestReportModel(unittest.TestCase):

    def test_json_is_the_same_that_creation(self):
        rm = ReportModel(Reports.asylum)
        self.assertEqual(Reports.asylum, rm.json())

    def test_get_keyword(self):
        expected = ['Asylum Games', 'Banjooli', 'Mutinies', 'Polis']
        rm = ReportModel(Reports.asylum)
        keywords = rm.getKeywords()
        #print keywords
        self.assertEqual(len(expected), len(keywords))
        self.assertEqual(expected, keywords)

    def test_get_keyword_dont_return_special_keys(self):
        expected = ['Polis', 'Banjooli', 'Mutinies', 'Asylum Games']
        report = {'Asylum Games':[], 'Banjooli':[], 'Mutinies':[], 'Polis':[], 'title':"", 'report_date':""}
        rm = ReportModel(report)
        keywords = rm.getKeywords()
        print keywords
        self.assertEqual(len(expected), len(keywords))
        self.assertEqual(expected, keywords)


class TestMsgListModel(unittest.TestCase):

    def setUp(self):
        self.pre = self.assertTrue
        self.threat = Reports.get_asylum_thread()
        self.msglist = MsgListModel(self.threat['msgs'])

    def test_json(self):
        self.assertEqual(self.threat['msgs'], self.msglist.json())

    def test_append_one_msg(self):
        self.pre(self.msglist.size() == 1)
        self.msglist.append_msg(dict())
        self.assertTrue(self.msglist.size() == 2)

    def test_lastmsg_object(self):
        msg_obj = self.msglist.lastmsg_object()
        self.assertEqual(msg_obj.id(), "msg_1169262")



class TestThreadModel(unittest.TestCase):

    def setUp(self):
        self.empty_thread = ThreadModel({"msgs": [{}], 'answers': '0'})
        self.thread = ThreadModel(Reports.threats_with_newline.copy())

    def test_date(self):
        self.assertIsNone(self.empty_thread.date())
        self.empty_thread.set_date("X")
        self.assertEqual("X",  self.empty_thread.date())

    def test_get_id_last_msg(self):
        _id = self.thread.id_last_msg()
        self.assertEqual(_id, "msg_1169262")

    def test_get_id_last_msg_return_null_if_not_id(self):
        result_id = self.empty_thread.id_last_msg()
        self.assertIsNone(result_id)

    def test_date_last_msg(self):
        self.assertEqual(u' 24 de Octubre de 2013, 08:22:36 am \xbb', self.thread.date_last_msg())

    def test_when_thread_has_no_answers_return_num_of_msg_minus_one(self):
        """ LaBSK doe snot count the first msg
        """
        thread = ThreadModel({'msgs': [{}, {}]})
        self.assertEqual(1, thread.answers())

        thread = ThreadModel({'msgs': []})
        self.assertEqual(-1, thread.answers())

        thread = ThreadModel({'msgs': [{u'date': u' 18 de Septiembre de 2013, 05:19:46 pm \xbb', u'body': u'Dejo por aqu\xed varios enlaces a nuestros \xfaltimos programas.\xa0 Hemos dejado de ser programa de radio de momento (espero que despu\xe9s de las fiestas del Pilar volvamos a serlo) as\xed que el sonido no es muy bueno, pero creo que las entrevistas son muy interesantes porque los invitados lo son\xa0 Proyecto de revista de juegos de mesa en papel y otros temas:Pedro Soto y otros temas:', u'user': u'verarua'}]})
        self.assertEqual(0, thread.answers())

    def test_answers_is_numer(self):
        #print type(self.thread.answers())
        self.assertIsInstance(self.thread.answers(), int)

    def test_num_of_msgs(self):
        t = {u'source': u'LaBSK', u'link': u'http://labsk.net/index.php?topic=127181.0', u'msgs':
             [{u'date': u' 07 de Febrero de 2014, 01:00:21 pm \xbb', u'body': u'', u'user': u'LudoNoticias'},
              {u'date': u' 07 de Febrero de 2014, 05:00:54 pm \xbb', u'body': u'Recuerdo haber jugado hace mucho tiempo con las miniaturas aquellas, de la marca Grenadier si mi memoria no falla... lo cierto es que al ser un juego mas interpretativo y no tan tactico como pudiera ser un D&D las dejamos de usar, asi que para mi, en cuanto a una partida de rol, me parecen mas objeto de coleccionismo que otra cosa, salvo que las quieras usar para un Mansiones o un Arkham\xa0 ', u'user': u'Ech-Pi-El'},
              {u'date': u' 08 de Febrero de 2014, 03:34:44 am \xbb', u'body': u'Sinceramente chicos, si quer\xe9is miniaturas chulas de Cthulhu y sus colegas, huid de estas... cosas e iros a por las de Cthulhu Wars Es que no hay comparaci\xf3n alguna, da hasta verg\xfcenza ajena...Vs', u'user': u'Torke'}], u'title': u'Call of Cthulhu, las miniaturas para sus m\xf3dulos'}

        thread = ThreadModel(t)
        self.assertEqual(3, thread.msg_count())

    def test_when_thread_has_no_msgs_key_then_the_count_of_msgs_is_0(self):
        """ LaBSK doe snot count the first msg
        """
        thread = ThreadModel({})
        self.assertEqual(0, thread.msg_count())

    def test_year_last_msg(self):
        self.assertEqual(self.thread.year_last_msg(), 2013)

    def test_add_creation_and_last_update_dates(self):

        t = {u'source': u'LaBSK', u'link': u'http://labsk.net/index.php?topic=127181.0', u'msgs': [{u'date': u' 07 de Febrero de 2014, 01:00:21 pm \xbb', u'body': u'', u'user': u'LudoNoticias'},
                                                                                                   {u'date': u' 07 de Febrero de 2014, 05:00:54 pm \xbb', u'body': u'Recuerdo haber jugado hace mucho tiempo con las miniaturas aquellas, de la marca Grenadier si mi memoria no falla... lo cierto es que al ser un juego mas interpretativo y no tan tactico como pudiera ser un D&D las dejamos de usar, asi que para mi, en cuanto a una partida de rol, me parecen mas objeto de coleccionismo que otra cosa, salvo que las quieras usar para un Mansiones o un Arkham\xa0 ', u'user': u'Ech-Pi-El'},
                                                                                                   {u'date': u' 08 de Febrero de 2014, 03:34:44 am \xbb', u'body': u'Sinceramente chicos, si quer\xe9is miniaturas chulas de Cthulhu y sus colegas, huid de estas... cosas e iros a por las de Cthulhu Wars Es que no hay comparaci\xf3n alguna, da hasta verg\xfcenza ajena...Vs', u'user': u'Torke'}
                ], u'title': u'Call of Cthulhu, las miniaturas para sus m\xf3dulos'}

        thread = ThreadModel(t)
        thread.add_creation_and_last_update_dates()
        self.assertEqual(t['creation_date'], u' 07 de Febrero de 2014, 01:00:21 pm \xbb')
        self.assertEqual(t['last_msg_date'], u' 08 de Febrero de 2014, 03:34:44 am \xbb')



class TestMsgModel(unittest.TestCase):

    def setUp(self):
        self.empty_thread = ThreadModel({"msgs": [{}], 'answers': '0'})
        self.thread = ThreadModel(Reports.threats_with_newline.copy())

    def test_when_msg_has_no_datetime_return_none(self):
        msg = {}
        msg_obj = MsgModel(msg)
        self.assertIsNone(msg_obj.datetime())

    def test_year(self):
        msg = {u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb'}
        msg_obj = MsgModel(msg)
        self.assertEquals(msg_obj.year(), 2013)

    def test_year_asylum_msg(self):
        msg = {u'id':'msg_1169262',
               u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb',
               u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}
        msg_obj = MsgModel(msg)
        self.assertEquals(msg_obj.year(), 2013)

    def test_datetime_asylum_msg(self):
        msg = {u'id':'msg_1169262',
               u'date': u' 24 de Octubre de 2013, 08:22:36 am \xbb',
               u'body': u"Programaci\xf3n de la emisi\xf3n para hoy jueves 24.\nEn el aire desde:10:00 - Grublin Games Publishing - Cornish Smuggler10:20 - Lautapelit.fi - Nations10:40 - Blackrock Editions - Armad\xf6ra11:00 - Ares Games - Sails of Glory, Galaxy Defenders11:30 - Placentia Games - Florenza: The Card Game12:00 - Schmidt Spiele/Drei Magier Spiele - Stories!, Dog Deluxe, Der geheimnisvolle Spiegel12:30 - Czech Board Games - Dr. Hrubec13:00 - Deinko Games - Patchistory13:30 - Asylum Games - Banjooli Xeet, 21 Mutinies Arrr! Edition14:00 - eggertspiele - Rokoko, Coal Baron14:30 - Portal Games - Legacy: The Testament of Duke de Crecy, Theseus: The Dark Orbit15:00 - Hans im Gl\xfcck - Russian Railroads, Carcassonne: South Seas15:30 - Hurrican - Sheeepzz15:45 - LudiCreations - Byzantio16:00 - Backspindle Games - Luchador! Mexican Wrestling Dice16:30 - IELLO - C'est pas faux!, Guardians' Chronicles, Heroes of Normandie17:00 - IELLO - Continued17:30 - Spielworxx - Agora, Kohle & Kolonie18:00 - Queen Games - Dark Darker Darkest, Amerigo, Speculation, Templar: The Secret Treasures18:30 - Queen Games - Continued", u'user': u'winston smith'}
        msg_obj = MsgModel(msg)
        self.assertEquals(msg_obj.datetime(), datetime(2013, 10, 24, 8, 22, 36))
        self.assertEquals(msg_obj.datetime().year, 2013)


if __name__ == '__main__':
    unittest.main()
