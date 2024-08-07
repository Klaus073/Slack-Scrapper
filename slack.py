import os
from slack_sdk import WebClient

# Initialize a Slack WebClient
slack_token = "slack_token"
client = WebClient(token=slack_token)

# Define the channel ID
channel_id = "channel_id"

# Call the conversations.history method to retrieve messages
response = client.conversations_history(channel=channel_id)

# Check if the request was successful
if response["ok"]:
    messages = response["messages"]
    for message in messages:
        print(message)
else:
    print("Error:", response["error"])
