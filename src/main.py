import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Load DISCORD_TOKEN from .env or environment variable

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Check message content
    c = message.content.lower()
    if message.content.lower() == c:
        await message.channel.send(f"Hello {message.author.name} 👋")

    # Allow commands to still work
    await bot.process_commands(message)
    

bot.run(os.getenv("DISCORD_TOKEN"))

"""import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
df = pd.DataFrame(load_iris()["data"])
df.plot()
plt.show()
st.pyplot(plt)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

import socket
import ssl
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.google.com"  # Replace with your desired host
port = 443  # HTTPS default port
context = ssl.create_default_context()
secure_socket = context.wrap_socket(s1, server_hostname=host)
secure_socket.connect((host, port))
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
secure_socket.sendall(request.encode())

#s1.send(b"GET / HTTPS/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n")
response = b""
while True:
    chunk = secure_socket.recv(4096)
    if not chunk:
        break
    response += chunk

#print(response.decode())
def getURLS():
    res = response.decode()
    re=""
    for i in range(len(res)):
        if(res[i]=="<" and res[i+1]=="a"
          and res[i+2]==" " and res[i+6]=="f"):
            re+=res[i+8:i+100]
            re+="\n"
    return re
print(getURLS())
            
print(dir(s1)) """