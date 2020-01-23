from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

import urllib
import urllib.request

def SportDemo():
    # Set url parameter
    url = "http://api.isportsapi.com/sport/football/team/search?api_key=NV8MdqXXgeriwer5&name=uruguay"

    # Call iSport Api to get data in json format
    f = urllib.request.urlopen(url)
    content = f.read()

    print(content.decode('utf-8'))

# Set url parameter
    url = "http://api.isportsapi.com/sport/football/player/search?api_key=NV8MdqXXgeriwer5&name=suarez"

    # Call iSport Api to get data in json format
    f = urllib.request.urlopen(url)
    content = f.read()

    print(content.decode('utf-8'))

from database import *	

##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/info_page')
def infopage():
	info = SportDemo()
	return render_template("info.html", uruguay_info=player_info)

@app.route('/history_page')
def historypage():
	return render_template("history.html")

@app.route('/quiz_page')
def quizpage():
	return render_template("quiz.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)