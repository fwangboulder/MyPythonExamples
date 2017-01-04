from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACb5d0bd65a471192f7ef653daedd00686"
auth_token = "6a4cd9a11793c659b4541dcaed54475b"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14805592055", from_="+14083311619",
                                     body="Hello there!")
