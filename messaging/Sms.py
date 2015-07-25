#!/usr/bin/env python

import smtplib

"""Sms.py

Class that can send sms messages from a gmail account to a US cell phone.

"""

class Sms(object):
    """Main class for sending sms messages. 

    """

    def __init__(self, username, password, phone_address, message):
        """Initializes an instance of Sms.

        Inputs:
            username - gmail address
            password - password for gmail address
            phone_address - String with number and domain of a cell phone
                           ex: 1234567890@txt.att.net #att
                               1234567890@tmomail.net #tmobile
                               1234567890@vtext.com #verizon
        Outputs:
            none
        """
        self.username = username
        self.password = password
        self.phone_address = phone_address
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

    def send(self):
        """Method to send sms messages (text only). 

        Only works for US numbers (assumes country code is 1).
        """
        self.server.sendmail(self.username, self.phone_address, self.message)


