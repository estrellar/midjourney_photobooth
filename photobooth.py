import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui as pg
import cv2
import pygetwindow as gw
import os
from PIL import Image
import requests
from io import BytesIO


# Set up camera

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())

# Open the first camera connected to the computer.
cap = cv2.VideoCapture(0)
background_image_url = "https://cdn.discordapp.com/attachments/1131904046488354897/1131906142021357568/chihiro007.jpg"
@client.event
async def on_ready():
    print("Bot connected")

@client.event
async def on_message(message):
    msg = message.content
    print(message)

    # Start Automation by typing "automation" in the discord channel
    if msg == 'automation':
        time.sleep(3)
        pg.press('tab')
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(3)
            cv2.imwrite("frame.jpg", frame)
            await message.channel.send(file=discord.File('frame.jpg'))
            time.sleep(5)

    # Listen for the bot's own messages
    if message.author == client.user:
        for attachment in message.attachments:
            image_url = attachment.url
            # Loop through all windows

            pg.write(f'/imagine {image_url} {background_image_url} anime, hand-drawn and cel animation techniques, guests at party, natural design, beautifully rendered and expressive rich colors, vibrant pastel colors,imaginative and fantastical landscapes, sharp attention to detail,realism and a strong sense of nostalgia and warmth, sharp attention to small details and textures,fantastical creatures, settings, depth and emotions emphasized and accentuated by lighting and shading,extremely high quality, incredibly high finite definition, high resolution, hand-drawn and cel animation techniques, anime --ar 3:2 --stylize 1000 --q 2 --niji 5')
            time.sleep(3)
            pg.press('enter')
            time.sleep(5)

     # Still need to test this, 
     # but also need to have none blocking thread 
     # to listen to button press instead of constantly capturing
     # Listen for messages from Midjourney Bot
    if message.author.id == 9282:
        for attachment in message.attachments:
            response = requests.get(attachment.url)
            img = Image.open(BytesIO(response.content))
            width, height = img.size
            img1 = img.crop((0, 0, width // 2, height // 2))
            img2 = img.crop((width // 2, 0, width, height // 2))
            img3 = img.crop((0, height // 2, width // 2, height))
            img4 = img.crop((width // 2, height // 2, width, height))
            img1.save('img1.jpg')
            img2.save('img2.jpg')
            img3.save('img3.jpg')
            img4.save('img4.jpg')

client.run(discord_token)
