__author__ = 'Javier'

import unittest
from LaBSKApi.web import URL
from tests.Harness import MockKimonoPlanetaLudicoAPI
from LaBSKApi.PlanetaLudico import PlanetaLudicoScrap, Entry
from mockito import mock, when, any, verify

class TestPlanetaLudicoScrap(unittest.TestCase):

    def setUp(self):
        self.mock_collection = mock()
        self.scrap = PlanetaLudicoScrap(self.mock_collection)

    def _read_entries(self, _):
        return MockKimonoPlanetaLudicoAPI.json

    def test_when_scrapping_saves_one_element_per_entry_in_db(self):
        #mock_scrap = mock(self.scrap)
        #when(mock_scrap)._read_entries(any()).thenReturn(MockKimonoPlanetaLudicoAPI.json)
        self.scrap._read_entries = self._read_entries
        result = self.scrap.scrapListOfURL([URL("http://www.kimonolabs.com/api/6j0yuuni?apikey=4bac761d58acc84da9ccadf9e1ff2d8f", "Planeta Ludico")])
        verify(self.mock_collection, 2).save(any())
        #self.assertEqual(len(result), 2)

    def test_when_read_an_entry_title_is_title_of_emtry(self):
        result = self.scrap._build_entry(MockKimonoPlanetaLudicoAPI.entry_json)
        self.assertEqual(result.title,
                         MockKimonoPlanetaLudicoAPI.entry_json['title']['text'])

    def test_when_read_an_entry_date_is_date_of_emtry(self):
        result = self.scrap._build_entry(MockKimonoPlanetaLudicoAPI.entry_json)
        self.assertEqual(result.date,
                         MockKimonoPlanetaLudicoAPI.entry_json['date'])

    def test_when_read_an_entry_link_is_link_of_emtry(self):
        result = self.scrap._build_entry(MockKimonoPlanetaLudicoAPI.entry_json)
        self.assertEqual(result.link,
                         MockKimonoPlanetaLudicoAPI.entry_json['title']['href'])

    def test_when_read_an_entry_source_is_the_blog(self):
        result = self.scrap._build_entry(MockKimonoPlanetaLudicoAPI.entry_json)
        self.assertEqual(result.json()['location'],
                         MockKimonoPlanetaLudicoAPI.entry_json['source']['text'])


class TestEntry(unittest.TestCase):

    def test_json(self):
        entry = Entry('title', 'date', 'link', 'source')
        result = entry.json()
        self.assertEqual(entry.json(),
                         {'title':'title', 'creation_date':'date', 'link':'link', 'location':'source'})

if __name__ == '__main__':
    unittest.main()
