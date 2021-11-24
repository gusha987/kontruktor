#importēnepieciešamās bibliotēkas
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import logging
import logging.config
import tkinter as tk
from tkinter.constants import W
from configparser import ConfigParser
import mysql.connector
from mysql.connector import Error
import logging

#define logger konfiguraciju.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Actor.log')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)

logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Database.log')
file_handler.setFormatter(formater)
logger1.addHandler(file_handler)

#definē mainīgos, interfeisu un metodi ko tas izmanto.
root = tk.Tk()
connection =  None
connected = False
try:
	config = ConfigParser()
	config.read('config.ini')
	mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
	mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
	mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
	mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
except:
	logger.exception('')
logger.info('DONE')
#tiek inicializēta datu bāze
logger1.info('Initializing database')
def init_db():
	global connection
	connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
init_db()
logger.info("DONE")
def get_cursor():
	global connection
	try:
		connection.ping(reconnect=True, attempts=1, delay=0)
		connection.commit()
	except mysql.connector.Error as err:
		logger1.error("No connection to db " + str(err))
		connection = init_db()
		connection.commit()
	return connection.cursor()

# Opening connection to mysql DB
logger1.info('Connecting to MySQL DB')
try:
	# connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
	cursor = get_cursor()
	if connection.is_connected():
		db_Info = connection.get_server_info()
		logger1.info('Connected to MySQL database. MySQL Server version on ' + str(db_Info))
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		logger1.debug('Your connected to - ' + str(record))
		connection.commit()
except Error as e :
	logger1.error('Error while connecting to MySQL' + str(e))

def GetActors():
    
    
    aktieri = list()
    lomas = list()
    url = e1.get()
    #ar try  tiek mēģināts savienoties ar ievadīto url, ja neizdodas tad tiek izvadīts kļūdas paziņojums log failā
    logger.info("Connecting to Url.")
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
    try:
        i=1
        for a in range(len(aktieri)):
            if a in range(len(lomas)):
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO actors" "('actor','role','url')" "VALUES('"+str(actors[a])+"','"+str(roles[a])+"','"+str(e1.get())+"')")
                    
                    connection.commit()
                    cursor.close
                except Error as e :
                    logger1.error("INSERT INTO actors ('actor','role','url') VALUES('"+aktieri[a]+"','"+lomas[a]+"','"+e1.get()+"')")
                tk.Label(frame1, text=(aktieri[a] + ' played as ' + lomas[a])).grid(row=i+1)
                
                i = i+1

            else:
                print(str(i) + '.Actor '+aktieri[a])
                i = i+1
        logger.info('Succesfully printed all the actors listed on the page.')
    except:
        logger.info("The given page didn't have any list of actors. Make sure you are using the imdb.com website url.")
        quit()

if __name__ == "__main__":

    #definē interfeisu
    canvas = tk.Canvas(root, height=700, width=500,bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relheight=0.05,relwidth=0.8,relx=0.1,rely=0.08)
    frame1 = tk.Frame(root, bg="white")
    frame1.place(relheight=0.7,relwidth=0.8,relx=0.1,rely=0.2)

    tk.Label(frame, text="Paste a movie link from imdb.com").grid(row=1)

    e1 = tk.Entry(frame)
    e1.grid(row=1, column=1)
    get_actors = tk.Button(root, text = 'List actors',padx=10,pady= 5, fg='white', bg ='#263D42', command=GetActors)
    get_actors.pack()
    root.mainloop()