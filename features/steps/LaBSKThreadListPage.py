from bs4 import UnicodeDammit, BeautifulSoup

class LaBSKThreadListPage:

	def __init__(self, source):
		self.soup = BeautifulSoup(source)
		
	def count(self, word):
		count = 0
		for line in self.soup.find("table", "table_grid").tbody.find_all("tr"):
			field = line.find("td", "subject windowbg2")
			if field <> None:
				ud = UnicodeDammit(field.a.contents[0])
				title = ud.unicode_markup
				#print "LaBSKThreadListPage::count -- ", ud.unicode_markup
				if word in title:
					count = count +1
		return count