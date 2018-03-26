# Health Buddy Slack app

Health Buddy is a Slack App that helps you maintain mental and physical health throughout the day by sending periodic reminders and uplifting messages.

## Sources used

- [Slack API documentation](https://api.slack.com/)
- [How to write a Slack bot with Python code](https://medium.com/@julianmartinez/how-to-write-a-slack-bot-with-python-code-examples-4ed354407b98)
- [Slack developer kit](https://slackapi.github.io/python-Slackclient/)

## How to install on your own Slack channel

- First things first, you need to create a folder to hold all of these files and set up a virtualenv.
- Next, you must install Slack Developer Kit for Python. Do that by typing `pip install slackclient` in the command line.
- Then you must open Slack in your browser, and retrieve the Slack channel ID, located in the URL. Paste that into "channel."
- After that, generate your own Slack token. [Read about different Slack tokens.](https://api.slack.com/docs/token-types) You need the OAuth Bot User Token.
- Invite health-buddy to the Slack channel!
- If you want, you can add more messages into the JSON file.
- Finally, deploy to Heroku. [Here is a helpful video we used.](https://www.youtube.com/watch?v=DwWPunpypNA) We also used Heroku Scheduler to have Health Buddy run every four hours.
- You're good to go!

## Questions, comments, concerns?

- Gabrielle Calise
	-  [Github](https://github.com/gabriellecalise)
	-  [Twitter](https://twitter.com/gabriellecalise)

- Mary-Lou Watkinson
	-   [Github](https://github.com/M-Watkinson)
	-  [Twitter](https://twitter.com/Mary_Lou_W)
