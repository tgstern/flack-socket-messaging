import os

from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
messages = []

@app.route("/")
def index():
    """ launch application and if reopening page load last channel in javascript"""
    return render_template("index.html", channels=channels)


@app.route("/home")
def home():
    """ build homepage with list of available channels"""
    return render_template("home.html", channels=channels)


@app.route("/new", methods=["GET", "POST"])
def new():
    """ render new channel page on GET, create new channel and redirect to it on POST """
    if request.method == "GET":
        return render_template("new.html", channels=channels)
    if request.method == "POST":
        new = request.form.get("channel")
        if new != "" and new not in channels:
            channels.append(new)
            return redirect("/" + new)
        else:
            return render_template("new.html", channels=channels)


@app.route("/<string:channel>")
def channel(channel):
    """ generate page for each channel, sending message JSON array to populate with javascript """
    return render_template("channel.html", channels=channels, channel=channel, messages=messages)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """ render edit page on GET, update channel/message lists on POST and redirect to homepage"""
    if request.method == "GET":
        return render_template("edit.html", channels=channels)
    if request.method == "POST":
        global messages
        if request.form.get("clear") != "":
            cchannel = request.form.get("clear")
            newlist = []
            for message in messages:
                if message["channel"] != cchannel:
                    newlist.append(message)
        if request.form.get("channels") != "":
            xchannel = request.form.get("channels")
            channels.remove(xchannel)
            newlist = []
            for message in messages:
                if message["channel"] != xchannel:
                    newlist.append(message)
        if request.form.get("user"):
            xuser = request.form.get("user")
            newlist = []
            for message in messages:
                if message["username"] != xuser:
                    newlist.append(message)
        messages = newlist        
        return redirect("/home")


@socketio.on("send message")
def post(message):
    """ update message JSON array with incoming messages from socket.io """
    messages.insert(0, message)
    emit("post message", messages, broadcast=True)