from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACf3bcb0affffc334f1b8ad79fdfcb97ae'
auth_token = '696a7b8ab8b7b633b154f91dad8eb641'
client = Client(account_sid, auth_token)

incoming_phone_number = client.incoming_phone_numbers.create(phone_number="+15005550006")

print(incoming_phone_number.sid)
