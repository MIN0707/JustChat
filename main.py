import os
from stream_chat import StreamChat

api_key = 'YOUR_API_KEY'
seceret_key = 'SECRET_KEY'

chat = StreamChat(api_key=api_key, api_secret=seceret_key)

# Create a User
name = input("이름을 입력하세요 >> ")
chat.upsert_user({"id": name, "name": name})

# Create a Channel
ChannelName = input("채널명을 입력하세요 >> ")
channel = chat.channel("messaging", ChannelName)

channel.create(name)
channel.send_message({"text": "님이 접속했어요"}, user_id=name)

while True:
    os.system('cls')
    messages = channel.query().get('messages')
    for message in messages:
        print(message['user']['name'] + ": " + message['text'])
    answer = input("메세지를 입력하세요 >>")
    if answer == "/exit":
        channel.send_message({"text": "님이 나갔어요"}, user_id=name)
        break
    if answer == "/clear":
        messages = channel.query().get('messages')
        for message in messages:
            chat.delete_message(message['id'], hard=True)
    if answer == "/update":
        pass
    else:
        channel.send_message({"text": answer}, user_id=name)
