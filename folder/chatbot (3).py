#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().system('pip install chatterbot')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)
trainer.train([
    "Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
    
])
trainer.train([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
    
])

while True:
	request=input('you :')
	if request == 'OK' or request == 'ok':
		print('Bot: bye')
		break
	else:
		response=bot.get_response(request)

		print('Bot:', response)


# In[ ]:




