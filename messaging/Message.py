#!/usr/bin/env python

import smtplib

"""Message.py

Classes that can send sms, mms, or emails from a gmail account.

"""

class Message(object):
    """Main class for sending sms, mms, or email messages. 

    """

    def __init__(self, username, password):
        """Initializes an instance of Message.

        Inputs:
            username - gmail address
            password - password for gmail address

        Outputs:
            none
        """
        self.username = username
        self.password = password
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

    def sms(self, phone_address, message):
        """Method to send sms messages (text only). 

        Only works for US numbers (assumes country code is 1).

        Inputs:
            phone_number - String with number and domain of a cell phone
                           ex: 1234567890@txt.att.net #att
                               1234567890@tmomail.net #tmobile
                               1234567890@page.nextel.com #sprint pcs
                               1234567890@vtext.com #verizon

            message - String containing message to send
        """
        server.sendmail(self.username, phone_address, message)


