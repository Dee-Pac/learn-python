import aiohttp, asyncio

url = "http://httpbin.org/anything"
url = "http://httpbin.org/delay"


async def fetch(url):
    headers = {'accept' : 'application/json'}
    out = None
    async with aiohttp.ClientSession() as s:
        resp = await s.get(url = url, headers = headers, data = {"name":"deepak"})
        # out = await resp.read()
    print("finished", url)
    return resp
    
async def get(url):
    k= await asyncio.gather(fetch(url + "/" + str(10)), fetch(url + "/" + str(3)),fetch(url + "/" + str(2)))
    print(k)
    
asyncio.run(get(url))

# async def donwload_aio(urls:Iterable[str])->List[Tuple[str, bytes]]:
#     async def download(url: str) -> Tuple[str, bytes]:
#         print(f"Start downloading {url}")
#         async with aiohttp.ClientSession() as s:
#             resp = await s.get(url)
#             out = image_name_from_url(url), await resp.read()
#         print(f"Done downloading {url}")
#         return out
        
#     return await asyncio.gather(*[download(url) for url in urls])