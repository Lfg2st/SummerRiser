import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE1OTExMzM5MzI3NDM3MjIwNg.GUgzRy.2trP1QpoIjwioJoZXO5c4QsNRX9-bvvzeJpIdM'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!' )

    client.run(TOKEN)