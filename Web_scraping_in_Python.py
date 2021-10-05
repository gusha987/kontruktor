#importēnepieciešamās bibliotēkas
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import logging
import logging.config

#define logger konfiguraciju.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Actor.log')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)


#definē mainīgos.
i = 1

aktieri = list()
lomas = list()
url = "https://www.imdb.com/title/tt0251127/?ref_=fn_al_tt_1"

#ar try  tiek mēģināts savienoties ar ievadīto url, ja neizdodas tad tiek izvadītss kļūdas paziņojums
try:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    logger.info('The connection to the url was succesful')
except:
    logger.error('Could not reach the url.')
    quit()

#iet cauri mājas lapas kodam meklējot aktierus un lomas
actors = soup.findAll('a', {'data-testid': 'title-cast-item__actor'})
roles = soup.findAll('span', {'class': 'StyledComponents__CharacterNameWithoutAs-y9ygcu-5 iaZZDn'})
 

#pievieno aktierus un lomas iepriekš definētajiem sarakstiem.
for a in actors:
    aktieri.append(a.text)
for a in roles:
    lomas.append(a.text)

#ejot cauri sarakstiem izvada aktieri un viņa attiecīgo lomu.

try:
    for a in range(len(aktieri)):
        if a in range(len(lomas)):
            print(str(i) +'.Actor ' +aktieri[a] + ' played ' + lomas[a])
            i = i+1
        else:
            print(str(i) + '.Actor '+aktieri[a])
            i = i+1
    logger.info('Succesfully printed all the actors listed on the page.')
except:
    logger.info("The given page didn't have any list of actors. Make sure you are using the imdb.com website url.")
    quit()
