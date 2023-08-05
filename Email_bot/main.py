import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

#🔴🔴🔴Template to get the voice input from the user and print it on ther terminal start🔴🔴🔴

#here we are creating a listener in our python code to to that we use the command below so that it will recoh=gnize whatever I am saying
listener = sr.Recognizer()
#creating an speaking engine to speak it us and we can start it by calling pyttsx3.init()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

#now after stting up the recognizer we write our code in a try catch block
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            #we create a variable voice to listen whatever #is coming from the source and recognize it
            voice = listener.listen(source)
            #whatever the info we will be getting from the user
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

#🔴🔴🔴Template to get the voice input from the user and print it on ther terminal end🔴🔴🔴


#🔴🔴🔴Template to send one email start🔴🔴🔴
def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('thakuramit14675@gmail.com','bkpmkntvdkggjefz')

    email = EmailMessage()
    email['From'] = 'thakuramit14675@gmail.com'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)

    # server.sendmail('thakuramit14675@gmail.com','thakuramit4961@gmail.com', 'hi i know u')

#🔴🔴🔴Template to send one email end🔴🔴🔴

#🔴Email List in form of dicitionary🔴
email_list = {'thakur':'amitkota4961@gmail.com',
              'amit': 'thakuramit4961@gmail.com',
              'pratik':'pratikkumar0014@gmail.com'
}
#🔴Email List🔴


#🔴🔴🔴An assistant to ask info about about email start🔴🔴🔴
def get_email_info():
    talk('To whom you want send email')
    name = get_info()
    receiver = email_list[name.lower()]
    print(receiver)
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the text of your email')
    msg = get_info()
    send_email(receiver,subject,msg)
    talk('Your email is sent successfully')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' == send_more:
        get_email_info()
    else:
        talk('Thank you for using our email bot service')


get_email_info()


#🔴🔴🔴An assistant to ask info about about email end🔴🔴🔴
