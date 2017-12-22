# Comilio Python SMS Send

Python client module to send SMS messages using Comilio SMS Gateway.

To use this library, you must have a valid account on https://www.comilio.it.

**Please note** SMS messages sent with this library will be deducted by your Comilio account credits.

For any questions, please contact us at tech@comilio.it

# Installation

```bash
$ pip install comilio
```

# Send a message

```py
import comilio

comilio_client = comilio.Client('username', 'password')
comilio_client.send('Hello!', '+393401234567')

# returns:
{"message_id": "string"}
```

By default, client sends Classic type messages. You can change that per message:
```py
comilio_client.send(text, type=comilio.SMART)
```
Or, you can change it globally:
```py
comilio_client.set_default_type(comilio.SMART)
```
Available options are `comilio.CLASSIC`, `comilio.SMART` and `comilio.SMARTPRO`.

# Setting default options
You might want to send bulk messages. We're making it slightly easier for you!
`comilio_client.set_default_sender` and `comilio_client.set_default_recipients` are also available. Check examples for more informations.

# Check status of message

```py
comilio_client.status('A95455F7031140769030CCA81E764C5F')

# returns:
[
  {"phone_number": "+393401234567", "status": "Sent"}
]
```

# Handling insufficient credit
If you have insufficient credit, by default, you'll get a response like this one:
```json
{"error": "Insufficient+credit"}
```
If you'd prefer to have an exception thrown in such case, set `raise_insufficient_credit` attribute to `True` on the initialized Client object:
```py
comilio_client.raise_insufficient_credit = True
```

# More info

You can check out our website https://www.comilio.it
