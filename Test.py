from twilio.rest import Client 
 
account_sid = 'ACf717a2a13c03821aa5976151196139c1' 
auth_token = '9e63223620e8b5540ec7969cc156b1ef' 
client = Client(account_sid, auth_token) 


def whatsapp_bc_sender():
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Test Message For Whatsapp BC database',
                              to='whatsapp:+2349091425496'
                              )

    print(message.sid)
