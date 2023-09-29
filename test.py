import requests
import asyncio
import aiohttp
import time

url="https://api.genderize.io?name=luc"

def call_API_normal():
    response = requests.get(url)
    response_json = response.json()
    print(response.status_code)
    return [response.status_code, response_json]

t_normal_start=time.time()
tasks=[]
for i in range(100):
    tasks.append(call_API_normal())
t_normal_stop=time.time()
print(f"{t_normal_stop-t_normal_start} sec")
print(tasks)

async def call_API_async():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session,session.get(url=url) as response:
        response_json = await response.json()
        print(response.status)
        return [response.status, response_json]

async def async_process():
    tasks=[]
    for i in range(100):
        task=asyncio.ensure_future(call_API_async())
        tasks.append(task)
    return await asyncio.gather(*tasks)

t_normal_start=time.time()

print(1)
loop=asyncio.get_event_loop()
results = loop.run_until_complete(async_process())
print(1)
t_normal_stop=time.time()
print(f"{t_normal_stop-t_normal_start} sec")
print(results)