import smtplib
from email.mime.text import MIMEText

def start_server():
	server = smtplib.SMTP_SSL('smtp.gmail.com')

	server.connect("smtp.gmail.com",465)

	return server

def send_email_recepient(server,name, toaddr, link):
	greeting = '<html><body>Hi ' + name + ','
	body = """	<p><strong>Santa</strong> here!!</p>
				<p>I saw that you attempted to receive your gift earlier but couldn't because it was being processed.
				 I am extremely sorry for the inconvenience.</p>
				 <br><br>
				 <p>The good news is that your gift is READY NOW!!! Please use the following link to claim it.</p>
				 <a href='""" + link + """'>"""+link+"""</a><br><br><p>MERRY CHRISTMAS AND A HAPPY NEW YEAR!!!!</p><br><br>
				 <p>Hope you loved the gift :)</p>
				</body>"""

	salutation="<p>Love,</p><p>Santa</p></body></html>"
	
	message = (greeting+body+salutation)

	msg = MIMEText(message,'html')

	msg['Subject'] = 'YOUR GIFT FROM Santa IS READY!!!'
	msg['From'] = 'santaklausiscool@gmail.com'
	msg['To'] = toaddr

	server.sendmail('santaklausiscool@gmail.com', toaddr, msg.as_string())

def send_email_creator(server, name, toaddr, posts): 
	greeting = '<html><body>Hi ' + name + ','
	body = """<p><strong>Santa</strong> here!!</p> 
			<p>Thank you so much for using my tool to spread the joy of Christmas at absolutely no cost!
	       This really means a lot to me.</p> <br><br><p>Here's what your recepients had to say:</p><br><br>"""
	post_data = '<p>'

	for post in posts:
		post_data+= post + " :<br>" + posts[post] + '<br>'

	conclusion = """<p>I hope this cheered you up! MERRY CHRISTMAS AND A HAPPY NEW YEAR!!!!</p>>"""
	salutation="<p>Love,</p><p>Santa</p></body></html>"

	message = (greeting+body+post_data+conclusion+salutation)

	msg = MIMEText(message,'html')

	msg['Subject'] = 'A NOTE FROM Santa!!!'
	msg['From'] = 'santaklausiscool@gmail.com'
	msg['To'] = toaddr

	server.sendmail('santaklausiscool@gmail.com', toaddr, msg.as_string())

def quit_server(server):
	server.quit()


# send_email_recepient(toaddr='eltonp3103@gmail.com',name='Elton', link='localhost:5000')

# posts={
# 	"Elton":"Yo",
# 	"Mandy":"Wassup"
# }

# send_email_creator(toaddr='eltonp3103@gmail.com', name='Elton', posts=posts)
