from asyncio import create_task
from asyncio import gather
from asyncio import new_event_loop
from asyncio import set_event_loop
from json import load
from os import path
from os import sep
from re import search

from aiohttp import ClientSession
from tqdm import tqdm

from export_data import export_data
from html_parser import html_parser
from module.fetch_tweet import fetch_tweet
from module.get_contents import get_contents
from module.get_tokens import get_tokens


async def main():
    url: str = "https://nitter.net/imasml_theater"
    script_dir: str = path.dirname(path.realpath(__file__))

    assert "headers" not in f"{script_dir}{sep}config", "Please check is your header.json exists in config folder."

    with open(f"{script_dir}{sep}config{sep}headers.json", "r") as headers:
        headers: dict = load(headers)

    print("Fetching Nitter.net list...")

    async with ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            queue: list[str] = html_parser(await response.text())
            print("Fetch complete!")

    tokens: dict = {**(await get_tokens())}
    expression: str = r"https:\/\/.+\/imasml_theater\/status\/(\d+)"
    tasks: list = []
    for counter, url in enumerate(tqdm(queue, desc="Fetching tweets from queue array...", unit=" data")):
        # Parsing tweetId
        tweetId: int = search(expression, url).group(1)
        api_callback: dict = await fetch_tweet(tokens, tweetId)
        content: dict = {**(await get_contents(api_callback))}

        # Data handling
        directory: str = f"{script_dir}{sep}test{sep}"
        tasks.append(create_task(export_data(directory, counter + 1, content)))

    await gather(*tasks)
    print("Task complete!")


loop = new_event_loop()
set_event_loop(loop)
loop.run_until_complete(main())
