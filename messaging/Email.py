#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from time import sleep

"""Email.py

Class that sends emails from a gmail account.

"""

class Email(object):
    """Main class for sending email messages. 

    """

    def __init__(self, username, password, email_address, message):
        """Initializes an instance of email.

        Inputs:
            username - gmail address
            password - password for gmail address
            email_address - An email address
                            ex: buggsbunny@gmail.com
                                porkypig@yahoo.com
            message - String containing message to send

        Outputs:
            none
        """
        self.username = username
        self.password = password
        self.email_address = email_address
        self.message = message
        self.server = self.login()

    def login(self):
        """Logs into gmail account and returns an instance of an SMTP server
        object.
        
        Inputs:
            none

        Outputs:
            server - An SMTP server object that can be used to send emails and
                     messages
        """
        print "Logging in to " +  self.username + "."
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.username, self.password)
        print "Logged in to " + self.username + "!"
        return server

    def send(self, *args):
        """Method to send an email message (currently text only)

        Inputs:
            email_address - An email address
                            ex: buggsbunny@gmail.com
                                porkypig@yahoo.com

            message - String containing message to send
        """
        if len(args) == 0:
            self.server.sendmail(self.username, self.email_address, self.message)
        else:
            msg = MIMEMultipart()
            msg['To'] = self.email_address
            msg['From'] = 'rpi_security'
            msg['Subject'] = 'Home Security Alert'

            msgText = MIMEText(self.message)
            msgText.set_charset("ISO-8859")
            msg.attach(msgText)

            with open(args[0], 'rb') as file_as_string:
                attachment = MIMEImage(file_as_string.read())

            attachment.add_header('Content-Disposition', 'attachment', filename=args[0])
            msg.attach(attachment)

            try:
                print "Sending mail from " + self.username + " to " + self.email_address + "..."
                self.server.sendmail(self.username, self.email_address, msg.as_string())
                print "Sent mail successfully!"
            except:
                print "Sending mail failed, tryin again..."
                sleep(1)
                self.send(args)
