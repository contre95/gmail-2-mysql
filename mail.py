from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

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




