#!/usr/bin/env python

import os
#from  dbupload import DropboxConnection
#import dropbox
import subprocess

"""Uploader.py

Classes that can upload files to cloud services such as Dropbox
"""

class Uploader(object):
    """Main class for uploading data to cloud services.
   
    """

#    def __init__(self, email_address, password):
    def __init__(self):
        """Initializes an instance of Uploader.

        Inputs:
            email_address - Email address that is linked to a cloud account
            password - Password for cloud account
           
        Outputs:
            none
        """
#        self.email_address = email_address
#        self.password = password

    def dropbox(self, local_file):
        subprocess.call(["dropbox_uploader.sh", "upload", local_file, "/"])

#    def _connect_to_dropbox_(self):
#        app_key = 'askdasdasdasd'
#        app_secret = 'asdasdasdasd'
#        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
#        authorize_url = flow.start()
#        print '1. Go to: ' + authorize_url
#        print '2. Click "Allow" (you might have to log in first)'
#        print '3. Copy the authorization code.'
#        code = raw_input("Enter the authorization code here: ").strip()
#        access_token, user_id = flow.finish(code)
#        #access_token, user_id = flow.finish('4FZTgsZmAewAAAAAAAB99KvlQdC-wizHEAcBzyfMgCs')
#        client = dropbox.client.DropboxClient(access_token)
#        return client
#
#    def dropbox(self, local_file):
#        client = self._connect_to_dropbox_()
#        fname = os.path.split(local_file)[1]
#        print 'fname: ' + fname
#        f = open(local_file, 'rb')
#        response = client.put_file('/' + fname, f)
#        print 'uploaded: ', response

#    def _connect_to_dropbox_(self):
#        """Method that returns a connection to the Dropbox server.
#        """
#        return DropboxConnection(self.email_address, self.password)
#
#    def dropbox(self, local_file, dropbox_destination):
#        """Method that sends a specified local file to a specified location on
#        a Dropbox server.
#
#        Inputs:
#            local_file - Filepath to local file to upload
#            dropbox_destination - Destination filepath on Dropbox filesystem
#
#        Outputs:
#            none
#        """
#        [path, fname] = os.path.split(local_file)
#        connection = self._connect_to_dropbox_()
#        connection.upload_file(local_file, dropbox_destination, fname)


      
