#!/usr/bin/env python

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage 

"""Mms.py

Class that can send mms messages from a gmail account to a US cell phone.

"""

class Mms(object):
    """Main class for sending Mms messages. 

    """

    def __init__(self, username, password, phone_address, message):
        """Initializes an instance of Mms.

        Inputs:
            username - gmail address
            password - password for gmail address
            phone_address - String with number and domain of a cell phone
                           ex: 1234567890@mms.att.net #att
                               1234567890@tmomail.net #tmobile
                               1234567890@vzwpix.com #verizon
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

    def send(self, local_file):
        """Method to send mms messages (text and a pic). 
        
        Inputs:
            self.local_file - file to attache to message

        Only works for US numbers (assumes country code is 1).
        """
        
        # Message header
        msg = MIMEMultipart()
        msg['To'] = self.phone_address
        msg['From'] = 'rpi_security'

        # Text part of the message
        msgText = MIMEText(self.message)
        msgText.set_charset("ISO-8859-1")
        msg.attach(msgText)

        # Open image as string
        with open(local_file, 'rb') as file_as_string:
        
            # Make attachment
            attachment = MIMEImage(file_as_string.read())

        attachment.add_header('Content-Disposition','attachment',filename=local_file)
        msg.attach(attachment)

        self.server.sendmail(self.username, self.phone_address, msg.as_string())


