
# MatrixGPT

**Attention**! This project was created by **thrown together hastily**, **I do not exclude** that there are places for improvement in my code, so do not throw 🍅 at me... 🙃

A little bit about functionality:
 - [x] 🤖 Support for private messages with the user
 - [x] 👥 Support for working with multiple users
 - [x] 📝 Short-term memory ( 20 messages )
 - [x] 🧹 Forced memory cleanup
 - [x] 💸 Free api for working with chatgpt
 - [ ] 🖲️Using PostgreSQL as storage
 - [ ] There could be your suggestion here...

# Installing

In order to launch this bot, you need to:

 - Have a created account on the matrix server
 - Dedicated server on Ubuntu/Debian/Arch etc..


Okay, let's move on to the installation:

 - Clone this repo : ```git clone https://github.com/shizamuru-dev/MatrixGPT.git```
 - Go to the downloaded directory ```cd MatrixGPT```
 - Now you need to install all the dependencies: ```pip install -r requirements.txt```
 - Go to ```Config``` and edit ```cfg.py``` file (To be precise: ```botID```,```botPassword```,```homeServer```)   
  
 - **AND NOW ATTENTION! AT THE MOMENT**, support for code blocks in simplematrixbotlib is broken, so for the bot to function correctly, you will need to fix it, see how to do it below



# Fix SimpleMatrixBotLib

I won't explain what's what, just repeat after me:

 - To begin with, let's find out where simplematrixbotlib is located: ```pip show simplematrixbotlib```
 - Find the line: ```Location: ......``` (In my situation ```Location: /usr/local/lib/python3.11/site-packages```)
 - Go to location
 - Open folder ```simplematrixbotlib```
 - Open ```api.py``` :
 - Find this:
 ```python
  async def send_markdown_message(self, room_id: str, message, msgtype: str = "m.text"):
      """
		 Send a markdown message in a Matrix room.
		 Parameters
		 -----------
		 room_id : str
		 The room id of the destination of the message.
		 message : str
		 The content of the message to be sent.
		 msgtype : str, optional
		 The type of message to send: m.text (default), m.notice, etc
	  """

        await self._send_room(room_id=room_id,
                              content={
                                  "msgtype": msgtype,
                                  "body": message,
                                  "format": "org.matrix.custom.html",
                                  "formatted_body": markdown.markdown(message,
                                                                      extensions=['nl2br'])
                              })```                            
                              
                             
```
And replace```extensions=['nl2br'])``` with ``extensions=['fenced_code','nl2br']``
Then save the changes...

# Run

That's all, it remains only to launch the bot: ```python3 main.py```
After starting, you need to confirm the session to do this, follow the instructions: [*Сlick\*](https://simple-matrix-bot-lib.readthedocs.io/en/latest/manual.html#verification)

