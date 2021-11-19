# discord api
import discord 
from discord.ext import commands

# .env configuration
from dotenv import load_dotenv
load_dotenv()

# system
import psutil
import os

# custom utilities and setup
from Utilities import db, log

log = log.Logger("client")

# client runtime variable
Token = os.getenv("CLIENT_TOKEN")

class Client(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # client version
        self.Version = "0.1.0"

        # operational level variables
        self.Updating = False
        self.Debugging = False
        self.Maintaining = False

        # psutil utilization
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    async def on_ready(self):
        await log.info(f"{self.user} is online.")
        await db.build()

# calling and initializing the client
client = Client(
    commands.when_mentioned_or("."),
    intents=discord.Intents.all(), 
    case_insensitive=True, 
    help_command=None
)

# Load cogs
for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")

client.run(Token, reconnect=True)