import bs4, unittest, requests
from app import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url_register = 'http://localhost:5000/register'
my_url_login = 'http://localhost:5000/login'
my_url_spell_check = 'http://localhost:5000/spell_check'

class TestSpellFunctions(unittest.TestCase):
    
    def test_loginsuccess(self):
        client = requests.Session()
        regget = client.get('http://localhost:5000/register')
        reggetsoup = BeautifulSoup(regget.text, 'html.parser')
       # print(regget.text)
        getreginput = reggetsoup.find_all('input')
        regcsrf_token = getreginput[0]['value']
        regpayload = {'username': 'batt', 'phone_number': '123123123', 'password': 'cry', 'csrf_token': regcsrf_token}
        regpost = client.post('http://localhost:5000/register', data=regpayload)
        regpostsoup = BeautifulSoup(regpost.text, 'html.parser')
        regpostinput = regpostsoup.find_all('input')
        regpost_csrf_token = regpostinput[0]['value']
        print('hello1')
        print(regpayload['csrf_token'])
        print(regpost_csrf_token)
        #loginclient = requests.Session()
        loginget = client.get('http://localhost:5000/login')
        logingetsoup = BeautifulSoup(loginget.text, 'html.parser')
       # print(regpost.text)
        getlogininput = logingetsoup.find_all('input')
        logincsrf_token = getlogininput[0]['value']
        loginpayload = {'username': 'batt', 'phone_number': '123123123', 'password': 'cry', 'csrf_token': logincsrf_token}
       # print(loginpayload)
        loginpost = client.post('http://localhost:5000/login', data=loginpayload)
       # print(loginpost.text)
        loginpostsoup = BeautifulSoup(loginpost.text, 'html.parser')
        loginpostinput = loginpostsoup.find_all('input')
        loginpost_csrf_token = loginpostinput[0]['value']
        print(loginpayload['csrf_token'])
        print(loginpost_csrf_token)
        print('hello2')
        loginpostoutput = loginpostsoup.find_all('p')
        reg_message = loginpostoutput[0].text
       # print(loginpostoutput)
        assert(reg_message == 'success')
        
        
    def test_invalidauth(self):
        userinfo = res_my_url_register = requests.get(my_url_register)
        res_my_url_login = requests.get(my_url_login)
        res_my_url_spell_check = requests.get(my_url_spell_check)
        
        assert(res_my_url_login.status_code == 200)
        assert(res_my_url_spell_check.status_code == 200)
        assert(res_my_url_register.status_code == 200)


    def test_regfail(self):
        regfailclient = requests.Session()
        initget = regfailclient.get('http://localhost:5000/register')
        soupg = BeautifulSoup(initget.text, 'html.parser')
        #print(initget.text)
        getinput = soupg.find_all('input')
        csrf_token = getinput[0]['value']
        payload = {'username': '', 'phone_number': '', 'password': '', 'csrf_token': csrf_token}
        print(payload)
        p = regfailclient.post('http://localhost:5000/register', data=payload)
        #print(p.text)
        soupp = BeautifulSoup(p.text, 'html.parser')
        postinput = soupp.find_all('input')
        post_csrf_token = postinput[0]['value']
        print(payload['csrf_token'])
        print(post_csrf_token)
        postoutput = soupp.find_all('p')
        reg_message = postoutput[0].text
        print(postoutput)
        assert(reg_message == 'Failure to register.  Please complete the required fields appropriately')

    def test_regsuccess(self):
        regclient = requests.Session()
        initget = regclient.get('http://localhost:5000/register')
        soupg = BeautifulSoup(initget.text, 'html.parser')
        #print(initget.text)
        getinput = soupg.find_all('input')
        csrf_token = getinput[0]['value']
        payload = {'username': 'batt', 'phone_number': '123123123', 'password': 'cry', 'csrf_token': csrf_token}
        print(payload)
        p = regclient.post('http://localhost:5000/register', data=payload)
        #print(p.text)
        soupp = BeautifulSoup(p.text, 'html.parser')
        postinput = soupp.find_all('input')
        post_csrf_token = postinput[0]['value']
        print(payload['csrf_token'])
        print(post_csrf_token)
        postoutput = soupp.find_all('p')
        reg_message = postoutput[0].text
        print(postoutput)
        assert(reg_message == 'Success you have been successfully registered!')


    def test_pagesxist(self):
        res_my_url_register = requests.get(my_url_register)
        res_my_url_login = requests.get(my_url_login)
        res_my_url_spell_check = requests.get(my_url_spell_check)
        
        assert(res_my_url_login.status_code == 200)
        assert(res_my_url_spell_check.status_code == 200)
        assert(res_my_url_register.status_code == 200)
    


if __name__ == '__main__':
    unittest.main()