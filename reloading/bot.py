import asyncio
import os

from discord.ext import commands


class TestBot(commands.Bot):
    def __init__(self, **options):
        super().__init__("!", **options)
        self.discord_token = os.environ["DISCORD_TOKEN"]

        # The code to reload needs to be an *extension* that then adds the cogs itself
        self.load_extension("reloading.cog")

    def run(self, reload: bool = False, *args, **kwargs):
        if reload:
            # We start the watcher in the event loop
            loop = asyncio.get_event_loop()
            loop.create_task(self.reload_watcher())

        super().run(self.discord_token, *args, **kwargs)

    async def reload_watcher(self):
        from watchgod import awatch
        from pathlib import Path

        async for changes in awatch(Path("./reloading").resolve()):

            if changes != set():
                print(f"Detected file change in '{[c[1] for c in changes]}'. Reloading...")

                try:
                    self.reload_extension("reloading.cog")
                except Exception as e:
                    print(e)
