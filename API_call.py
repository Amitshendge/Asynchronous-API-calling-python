#%%
import requests
import asyncio
import aiohttp
import time

url="https://www.google.co.in/"

#%%
def call_API_normal():
    response = requests.get(url)
    print(response.status_code)
    # print(response.json())

t_normal_start=time.time()
for i in range(100):
    call_API_normal()
t_normal_stop=time.time()
print(f"{t_normal_stop-t_normal_start} sec")
# %%
async def call_API_async():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session,session.get(url=url) as response:
        print(response.status)

async def async_process():
    tasks=[]
    for i in range(100):
        task=asyncio.ensure_future(call_API_async())
        tasks.append(task)
        await task
    final = await asyncio.gather(*tasks)

t_normal_start=time.time()

print(1)
loop=asyncio.get_event_loop()
loop.run_until_complete(async_process())
print(1)
t_normal_stop=time.time()
print(f"{t_normal_stop-t_normal_start} sec")
# %%
