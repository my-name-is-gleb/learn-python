import asyncio
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str, timed: int | None = None) -> int:
    if timed:
        await asyncio.sleep(timed)
    async with session.get(url) as result:
        return result.status