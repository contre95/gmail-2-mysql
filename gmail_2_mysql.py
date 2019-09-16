#!python3
#from mail import Gmail, Outlook ...
from mail import Gmail
from mensaje import Message

SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
CREDENTIALS = 'meli-service-account-credentials.json' 
KEYWORDS = {'devops','DEVOPS','DevOps'}

def has_keywords(msg, keywords):
    '''
    Recieves a Set of keywords
     'meli-service-account-credentials.json'Checks efficiently if a Messge contains Keyworkds
    Returns True or False
    '''
    for keyword in msg['subject'].split(' ')+msg['body'].split(' '):
        if keyword in keywords:
           return True
    return False   
    

def main():
    gmail = Gmail(CREDENTIALS,SCOPE)
    messages = gmail.get_messages()
    print(f'Subject --> Has Keywords {KEYWORDS}')
    print()
    for msg in messages:
        parsed_msg = gmail.get_parsed_msg(msg['id'])
        if has_keywords(parsed_msg,KEYWORDS):
            print(parsed_msg['subject'],'-->','Yes')
            try:
                new_msg = Message(parsed_msg['from'],parsed_msg['date'],parsed_msg['subject'])
                new_msg.save()
            except Exception as e:
                print(e)
        else:
            print(parsed_msg['subject'],'-->','No')
    
main()
