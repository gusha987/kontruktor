#importēnepieciešamās bibliotēkas
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

#definē mainīgos.
i = 1
aktieri = list()
lomas = list()
url = "https://www.imdb.com/title/tt10155932/?ref_=hm_stp_pvs_piv_tt_i_1"

#ar try  tiek mēģināts savienoties ar ievadīto url, ja neizdodas tad tiek izvadītss kļūdas paziņojums
try:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
except:
    print('ivalid url')
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
for a in range(len(aktieri)):
    if a in range(len(lomas)):
        print(str(i) +'.Actor ' +aktieri[a] + ' played ' + lomas[a])
        i = i+1
    else:
        print(str(i) + '.Actor '+aktieri[a])
        i = i+1
