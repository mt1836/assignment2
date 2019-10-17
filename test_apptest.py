import bs4, unittest, requests
from app import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url_register = 'http://localhost:5000/register'
my_url_login = 'http://localhost:5000/login'
my_url_spell_check = 'http://localhost:5000/spell_check'

class TestSpellFunctions(unittest.TestCase):
    
    def test_pagesxist(self):
        res_my_url_register = requests.get(my_url_register)
        res_my_url_login = requests.get(my_url_login)
        res_my_url_spell_check = requests.get(my_url_spell_check)
        
        assert(((requests.get('http://localhost:5000/register')).status_code) == 200)
       # assert(res_my_url_login.status_code == '200')
        #assert(res_my_url_spell_check.status_code == '200')
       # assert(res_my_url_register.status_code == '200')
        #assert(res_my_url_login.status_code == '200')
        #assert(res_my_url_spell_check.status_code == '200')
    
    
    def test_regfail(self):
        uClient = urlopen(my_url_register)
        register_html = uClient.read()
        uClient.close()
        register_soup = BeautifulSoup(register_html, "html.parser")
        assert(register_soup.p.text == 'Failure to register.  Please complete the required fields appropriately')

if __name__ == '__main__':
    unittest.main()