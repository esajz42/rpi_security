#!/usr/bin/env python

import smtplib

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
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.username, self.password)
        return server

    def send(self, email_address, message):
        """Method to send an email message (currently text only)

        Inputs:
            email_address - An email address
                            ex: buggsbunny@gmail.com
                                porkypig@yahoo.com

            message - String containing message to send
        """
        self.server.sendmail(self.username, self.email_address, self.message)




