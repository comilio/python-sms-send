import comilio


# Please register on https://www.comilio.it
comilio_username = 'your-username'
comilio_password = 'your-password'

sender = 'ComilioTest'
recipients = ['+393400000000', '+393499999999']
text = 'Hello world!'

client = comilio.Client(comilio_username, comilio_password)

message_ids = []

# Provide all info to send() directly
msg = client.send(text, recipients, comilio.SMART, sender)
message_ids.append(msg['message_id'])

# Set default values when, for example, bulk messaging
client.set_default_sender(sender)
client.set_default_recipients(recipients)
client.set_default_type(comilio.SMART)
msg = client.send(text)
message_ids.append(msg['message_id'])

# But, you can still override some/all parameters!
msg = client.send(text, sender=sender)
message_ids.append(msg['message_id'])

print('Here are the message IDs:')
for msg_id in message_ids:
    print(msg_id)
