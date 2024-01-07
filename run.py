from highrise.__main__ import *
from importlib import import_module
import time
import asyncio
import traceback
from keep_alive import keep_alive
import os

bot_file_name = "main"
bot_class_name = "Bot"
room_id = "64e77d88355c4b00c114688f"
bot_token = "e600bdde238e06994947cc53be7fffe003a16921fc2e0f724d050ae9d1574780"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id,bot_token)

# Start the Flask server to keep the bot alive
keep_alive()

async def run_bot():
    while True:
        try:
            definitions = [my_bot]
            await main(definitions)
        except Exception as e:
            traceback.print_exc()  # Print the full traceback of the exception
            print(f"An exception occurred: {e}")
            time.sleep(5)
        finally:
            print("Bot has stopped. Restarting in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    # Check if the watchdog script is not running
    if not os.environ.get("REPL_WATCHDOG"):
        asyncio.run(run_bot())  # Run the bot
