import requests
from bs4 import BeautifulSoup
from secrets import username, password

login_basic_url = 'https://mbasic.facebook.com/login'
login_mobile_url = 'https://m.facebook.com/login'
payload = {
            'email': username,
            'pass': password
                    }
with requests.Session() as session:
    post = session.post(login_basic_url, data=payload)
REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit=200&shown_ids=288080967878953%2C194735147324461%2C149087531793003%2C100045728942013%2C100042805714654%2C100042470567936%2C100041984138891%2C100040908255590%2C100040073714826%2C100039997277638&total_count=131&ft_ent_identifier=2729596950408702&ref=page_internal'
r=session.get(REQUEST_URL)
soup = BeautifulSoup(r.content, "html.parser")
names = soup.find_all('h3')
people_who_liked = []
for name in names:
    print(name.text)
