from aiohttp import web
import asyncio
from discord.ext import commands


class BotStatsAPI:
    def __init__(self, bot):
        self.bot = bot

    async def webserver(self):
        async def handler(request):
            data = {"status": "online", "count": "2"}
            return web.json_response(data)

        app = web.Application()
        app.router.add_get("/", handler)

        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, "192.168.1.193", 8999)
        await self.bot.wait_until_ready()
        await self.site.start()

    def __unload(self):
        asyncio.ensure_future(self.site.stop())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BotStatsAPI(bot))
