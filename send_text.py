from twilio.rest import TwilioRestClient
#if from twilio import rest
#use client = rest.TwilioRestClient(..., ...)
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbb7b483e06e59096bd557174f13ca077"
auth_token  = "101aa9318733881e066b95cb4ff5d8e4"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="sup?",
    to="+14089123437",    # Replace with your phone number
    from_="+16504467481") # Replace with your Twilio number
print message.sid
