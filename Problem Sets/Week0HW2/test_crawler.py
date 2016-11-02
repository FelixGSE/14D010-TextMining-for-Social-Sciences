import re
import unittest
execfile('crawler.py')

class TestCrawlerMethods(unittest.TestCase):
    def test_get_url_list(self):
        url = 'http://www.poemhunter.com/poems/new-poems/?a=0&l=new&order=submitted&p='
        reg = re.compile("\/poem\/.+\/")
        self.assertRegexpMatches(get_url_list(url)[0], reg)

    def test_get_titles(self):
        titles = ["/poem/eggs-and-ham/"]
        self.assertEqual(get_titles(titles), ["eggs and ham"])

    def test_clean(self):
        raw_html = "<p>Wobbling about on a ladder of bricks, <br/>taking a seat to rest momentarily.</p>"
        soup = BeautifulSoup(raw_html,"html.parser")
        self.assertEqual(clean(soup), "\n Wobbling about on a ladder of bricks,\n \n taking a seat to rest momentarily.\n")

    def test_get_poems(self):
        urls = ["/poem/eggs-and-ham"]
        reg = re.compile("[a-zA-Z]+")
        self.assertRegexpMatches(get_poems(urls)[0], reg)

if __name__ == '__main__':
    unittest.main()
