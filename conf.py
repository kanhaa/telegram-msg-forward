
# NOTE: Please rename this file (sample-conf.py) to 'conf.py' before using this bot.

# To get API_ID value follow these steps
# Go to https://my.telegram.org/auth
# Login with your normal telegram user account number.
# Go to API development tools
# A Create new application window will appear. Fill in your application details.
# There is no need to enter any URL. Just enter the App title and short name of your choice.
# Click on Create application at the end.
# Copy the API_ID and API_HASH values and paste here.
API_ID = 1144902
# NOTE: The API_HASH must be in single quotes. Below is a sample.
API_HASH = 'e743e5a4f35076e4c558a4bd713082e9'


# OWN_CHANNEL_ID is the unique id of your channel/group where you want to receive the updates.
# To get this id run the get_id.py file using 'python get_id.py'.
#  After login, if you have'nt already. It would instruct to you to got to the channel you want the id for and send any message there.
# After you send the message check your terminal. Find your message and copy the channel id to OWN_CHANNEL_ID.
# Be careful with the minus(-) sign. If it is in the id then place it as well.
OWN_CHANNEL_ID = -1001268815373

# Get the ids for all the channel you want to receive updates from and paste them here.
CHANNELS_TO_GET_UPDATES_FROM = [-1001381869748]


# You are done!
# Run the telegram_forwarder script using python telegram_forwarder.py using 'python telegram_forwarder.py'.
