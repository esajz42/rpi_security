from dbupload import DropboxConnection

conn = DropboxConnection("email@example.com", "password")
conn.upload_file("local_file.txt","/remote/path/","remote_file.txt")
