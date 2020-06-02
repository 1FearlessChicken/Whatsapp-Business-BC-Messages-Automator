from twilio.rest import Client 
 
account_sid = 'ACf717a2a13c03821aa5976151196139c1'
auth_token = 'dc7ca6a7d274240443c33a08bf71906d'
client = Client(account_sid, auth_token) 



def whatsapp_bc_sender():
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Test Message For Whatsapp BC database',
                              to='whatsapp:+2349091425496'
                              )

    print(message.sid)


