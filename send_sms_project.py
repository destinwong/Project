# Download the helper library from https://www.twilio.com/docs/python/install
import os
import time
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# print("What is your phone number?") 
# phone_Number = str(input()) # puts phone number to text into phone_number


print("What do you want to be reminded about?")
remind_topic = str(input())
print("How many times do you want to be reminded?")
number_times = int(input())
x="Reminding you to stretch, drink water, and "
complete_remind = x+remind_topic

print("How often do you want to me reminded? (in minutes)")
local_time = float(input())
local_time = local_time * 60

for i in range(0,number_times):
  time.sleep(local_time)
  message = client.messages \
                .create(
                     body=complete_remind,
                     from_='+12059526912',
                     to='+15108289878'
                 )

  #print(message.sid)
