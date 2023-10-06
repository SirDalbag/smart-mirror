import asyncio, aiohttp
import concurrent.futures
from model import News

url = "https://newsapi.org/v2/everything?q=Apple&sortBy=popularity&apiKey=075baa772e2b4100b75e82bbfc46ec42"


def init(elem: dict[any]) -> News:
    return News(
        author=elem["author"], title=elem["title"], description=elem["description"]
    )


def threading_init(matrix: list[list[any]]) -> list[News]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in matrix:
            futures.append(executor.submit(init, i))
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.json()


async def get():
    response = await request(url)
    vals = threading_init(matrix=response["articles"])
    return vals


asyncio.run(get())
