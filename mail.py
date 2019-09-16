from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# Parses a RFC 2822 date/time
from email.utils import parsedate_tz
from datetime import datetime as dt

class Gmail:

    def __init__(self, credentials,scope):
        self.credentiasl = credentials
        self.scope = scope
        self.service = self.authenticate()


    def authenticate(self):
        
        '''
        Checks for an existing token and authenticates
        Returns an already authenticated service
        '''

        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.credentials,self.scope)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))
        return service        
    
    def get_messages(self):
        '''
        Takes no parameters
        Returns a list of dictionarios, each representig a message containing both the message and thread unique id
        '''
        results = self.service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
        return results.get('messages', [])
    
    def get_msg(self, msg_id):
        '''
        Given a gmail message id returns the message
        '''
        msg = self.service.users().messages().get(userId='me', id=msg_id).execute()
        return msg

    def get_parsed_msg(self, msg_id):
        '''
        Recieves a message in the Gmail api format
        Returns a simplyfied version of the msg as a dictionary
        '''
        msg = self.get_msg(msg_id) 
        parsed_msg = {}
        for header in msg['payload']['headers']:
            if header['name'] == 'Subject':
                parsed_msg['subject'] = header['value']
            if header['name'] == 'Date':
                parsed_msg['date'] = dt(*parsedate_tz(header['value'])[:6]).strftime('%Y-%m-%d')
            if header['name'] == 'From':
                parsed_msg['from'] = header['value']
            parsed_msg['body'] = msg['snippet']
        return parsed_msg



