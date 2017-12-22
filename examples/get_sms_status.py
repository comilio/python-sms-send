import json
import comilio


# Please register on https://www.comilio.it
comilio_username = 'your-username'
comilio_password = 'your-password'

message_id = 's0m3-id'

client = comilio.Client(comilio_username, comilio_password)

# Get status of a sent message
status = client.status(message_id)

# and then print it nicely
print(json.dumps(status, indent=4))
