#THINKING WITH PORTALS
#
#|      O  ~~~
#| <=()\|/  ~~~
#|     /\ ~~~
#

import openai
import os
from dotenv import load_dotenv

openai.organization = os.getenv("ORG_KEY")
openai.api_key = os.getenv("OPEN_API_KEY")

open_position = "Senior python developer"

cv_text = 

messages = [
	{
		"role": "system",
		"content": f"Tresc naszej wiadomosci{open_position}"
	},
	{
		"role": "user",
		"content": f"Candidate's CV text: {cv_text}"
	}
]

chat_completion = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=messages
)

#
#|  ~~ O
#| ~ /|/()=>
#| ~~/\
#