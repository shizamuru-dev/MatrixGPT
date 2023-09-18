
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
  

# Run

That's all, it remains only to launch the bot: ```python3 main.py```
After starting, you need to confirm the session to do this, follow the instructions: [*Сlick\*](https://simple-matrix-bot-lib.readthedocs.io/en/latest/manual.html#verification)

