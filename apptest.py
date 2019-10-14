import bs4, unittest
from app import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url_register = 'http://localhost:5000/register'
my_url_login = 'http://localhost:5000/login'
my_url_spell_check = 'http://localhost:5000/spell_check'

class TestSpellFunctions(unittest.TestCase):
    def test_regfail(self):
        uClient = urlopen(my_url_register)
        register_html = uClient.read()
        uClient.close()
        register_soup = BeautifulSoup(register_html, "html.parser")
        assert(register_soup.p.text == 'Failure to register.  Please coplete the required fields appropriately')

if __name__ == '__main__':
    unittest.main()