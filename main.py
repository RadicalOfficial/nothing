import scratchattach as scratch3
import requests
import os
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return jsonify({"detail": "Something Odd Usually Lies."})

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
   'X-Requested-With': 'XMLHttpRequest'
   }
key = os.environ["KEY"]
session = scratch3.Session(key, username="Knightbot63")

conn = session.connect_cloud("959936525")

def get_count():
  text = requests.get(
    "https://corsproxy.io/?https://scratch.mit.edu/users/Knightbot63/followers/",headers=headers
  ).text
  text = text.split("Followers (")[1]
  text = text.split(")")[0]
  return text

# Used to JS :P
print("We are waiting to prevent rate-limits......")
time.sleep(10)
counter = get_count()
print("Setting")
conn.set_var("count", counter)
