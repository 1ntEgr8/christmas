from send_email import send_email_creator, start_server, quit_server
import maketree
from surprise import db
from surprise.models import Creator, Recepient

def notify():

	# need to go through the database
	# check if the received part is True
	# add functionality to bypass the truthiness of received
	# collect all of the thank you notes in a dictionary

	creators = Creator.query.all()

	server = start_server()
	count = 0

	for creator in creators:
		flag = True
		posts_to_send = {}
		recepients_for_creator = Recepient.query.filter_by(creator_id=creator.id)
		for recepient in recepients_for_creator:
			if recepient.received == False:
				flag = False
				break
		if flag == True:
			print("True")
			for recepient in recepients_for_creator:
				if recepient.thank_you_note:
					posts_to_send[recepient.recepient_name] = recepient.thank_you_note
			send_email_creator(server, creator.first_name, creator.email, posts_to_send)
			count+=1

	quit_server(server)	
	print("DONE NOTIFYING")
	print(f"{count} people notified")



