# Slack-like Chat Messaging Application

Web chat application hosted with Flask and live updating through Socket.IO. 
Application.py contains the route to generate html templates, most of which 
use additional JavaScript for functionality. Basic styling done in css file.

## Login and First Steps

On first visit, users are prompted to create username, which is saved in local
storage and linked to their messages. From any page, a user can view and 
visit available channels. 

## Messaging

When loaded, channel page uses JavaScript code
to pull messages from the Flask application. Messages are stored in an array
of JSON objects. Code is run per channel page to filter out the most recent
100 messages on that channel.

Messages are displayed in list with most recent at the top. User can send
messages to the channel from the text box, which trigger socket events
to push messages to any using the application without reloading page.

## Creating and Editing Channels

There are additional routes where users can create a new channel, or edit the
channels available. On the edit page, user can clear a channel, delete a 
channel (which clears messages and removes from the list of channels), and 
delete all messages they have sent across the channels.

## Session Data

If a user is on a channel and leaves the application, this is stored and loaded
the first time they revisit the page. Lastly, there is a logout button clears
local storage, removing the username and any saved tabs.

> Designed for HarvardX CS50: Web Programming with Python and JavaScript
