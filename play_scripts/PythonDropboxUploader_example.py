#!/usr/bin/env python

from dbupload import DropboxConnection

#https://github.com/jncraton/PythonDropboxUploader

conn = DropboxConnection("email@example.com", "password")
conn.upload_file("local_file.txt","/remote/path/","remote_file.txt")
