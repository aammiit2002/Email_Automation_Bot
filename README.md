# Email_Automation_Bot

import smtplib

#🔴🔴🔴Template to send one email start🔴🔴🔴

#📌📌📌 Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.

#📌📌📌 Here is the detail of the parameters −
# host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.

# port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.

# local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost as of this option.
server = smtplib.SMTP('smtp.gmail.com',587)
#server = smtplib.SMTP('host',port no.)

#📌📌📌 StartTLS is a protocol command used to inform the email server that the email client wants to upgrade from an insecure connection to a secure one using TLS.
server.starttls()

#📌📌📌 SMTP.login(user, password, *, initial_response_ok=True)
# Log in on an SMTP server that requires authentication. The arguments are the username and the password to authenticate with

server.login('thakuramit14675@gmail.com','bkpmkntvdkggjefz')

# An SMTP object has an instance method called 🌟sendmail🌟, which is typically used to do the work of mailing a message. It takes three parameters −

# The sender − A string with the address of the sender.

# The receivers − A list of strings, one for each recipient.

# The message − A message as a string formatted as specified in the various RFCs.

server.sendmail('thakuramit14675@gmail.com',
                'thakuramit4961@gmail.com', 'hi i know u')

#🔴🔴🔴Template to send one email start🔴🔴🔴

#🔴SPEECH RECOGNISATION🔴
pip install SpeechRecognition
📌📌USE THE COMMAND IN THE TERMINAL
#🔴RECOGNISATION🔴

#🔴SPEECH RECOGNISATION🔴
pip install PyAudio
📌📌USE THE COMMAND IN THE TERMINAL
#🔴RECOGNISATION🔴

