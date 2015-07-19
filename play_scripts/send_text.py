import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'account@gmail.com', 'password' )

# for pic or video message
#server.sendmail( 'josh', '5855078560@mms.att.net', 'yolo' )

# for text only message
server.sendmail( 'josh', '1234567890@txt.att.net', 'yolo' )