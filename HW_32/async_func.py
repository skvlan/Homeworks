import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched data from: {url}")
        return data


async def process_data(data):
    print("Processing data...")
    return f"Processed {len(data)} characters"


async def fetch_and_process(session, url):
    data = await fetch_url(session, url)
    processed = await process_data(data)
    return processed


async def fetch_with_future(session, url, future):
    print(f"Fetching with future from {url}")
    data = await fetch_url(session, url)
    future.set_result(data)


async def monitor_and_process(future):
    print("Waiting for future...")
    data = await future
    print("Future is done, processing result...")
    processed = await process_data(data)
    return processed


async def main():
    urls = ["https://lms.ithillel.ua", "https://python.org", "https://openai.com"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_process(session, url) for url in urls]

        future1 = asyncio.Future()
        future2 = asyncio.Future()

        tasks.append(fetch_with_future(session, urls[0], future1))
        tasks.append(fetch_with_future(session, urls[1], future2))

        tasks.append(monitor_and_process(future1))
        tasks.append(monitor_and_process(future2))

        results = await asyncio.gather(*tasks)
        print("All tasks completed:")
        print(results)


asyncio.run(main())
