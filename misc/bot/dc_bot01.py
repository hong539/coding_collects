import discord
import aiohttp
import io

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message contains a URL
    if 'http' in message.content:
        url = message.content
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    await message.channel.send('Could not download file...')
                    return
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, 'image.png'))

client.run('YOUR_BOT_TOKEN')