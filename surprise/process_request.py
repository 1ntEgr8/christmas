import maketree
from surprise import db
from surprise.models import Creator, Recepient

""" This script will be run alongside the server
	It will check the database for new request every 30 min 
	and will then process those requests
	Once the request has been processed, it will send an email to
	recepients and creators notifying them of the completion 
	of their order  
"""