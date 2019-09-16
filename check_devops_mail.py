#!python3
#from mail import Gmail, Outlook ...
from mail import Gmail
from mensaje import Message

SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
KEYWORDS = {'devops','DEVOPS','DevOps'}

def parse_msg(msg):
    '''
    Recieves a message in the Gmail api format
    Returns a simplyfied version of the msg as a dictionary
    '''
    parsed_msg = {}
    for header in msg['payload']['headers']:
        if header['name'] == 'Subject':
            parsed_msg['subject'] = header['value']
        if header['name'] == 'Date':
            parsed_msg['date'] = header['value']
        if header['name'] == 'From':
            parsed_msg['from'] = header['value']
        parsed_msg['body'] = msg['snippet']
    return parsed_msg

def has_keywords(msg, keywords):
    '''
    Recieves a Set of keywords
    Checks efficiently if a Messge contains Keyworkds
    Returns True or False
    '''
    for keyword in msg['subject'].split(' ')+msg['body'].split(' '):
        if keyword in keywords:
           print(msg['subject'],'-->',msg['from']) 
           print() 
           print(msg['body']) 
           print() 
           print() 
           return True
    return False   
    

def main():
    gmail = Gmail('meli-script-client.json',SCOPE)
    messages = gmail.get_messages()
#    return
    for msg in messages:
        parsed_msg = parse_msg(gmail.get_msg(msg['id']))
        if has_keywords(parsed_msg,KEYWORDS):
            new_msg = Message(parsed_msg['from'],"2019-03-02",parsed_msg['subject'])
            new_msg.save()
            
    
     
     
    

main()
