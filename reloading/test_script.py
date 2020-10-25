import dotenv
from reloading.bot import TestBot

dotenv.load_dotenv()

stats_bot = TestBot()

stats_bot.run(reload=True)
