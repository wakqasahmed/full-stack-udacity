from twilio.rest import Client

# Your Account SID from twilio.com/console
test_account_sid = "ACf3bcb0affffc334f1b8ad79fdfcb97ae"
account_sid = "AC47a06f1df5ea50e29aecaf1e787bbf48"
# Your Auth Token from twilio.com/console
test_auth_token  = "696a7b8ab8b7b633b154f91dad8eb641"
auth_token = "25b28233013c56e8518a949cfb31eaa0"

# Twilio Number
test_twilio_number = "+15005550006"
twilio_number = "+13126255438"

# Delivery Number
delivery_number = "+971562418355"

# Delivery Message
delivery_message = "Another reminder, follow the path of the Prophets"

client = Client(account_sid, auth_token)
test_client = Client(test_account_sid, test_auth_token)

test_message = test_client.messages.create(
    to=delivery_number, 
    from_=test_twilio_number,
    body=delivery_message)

message = client.messages.create(
    to=delivery_number, 
    from_=twilio_number,
    body=delivery_message)

print(test_message.sid)
print(message.sid)
