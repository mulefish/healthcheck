from aiohttp import web
import aiohttp
import asyncio
import json
import time

tokenHolder = {}
tokenHolder['token'] = None
tokenHolder['when'] = None

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def setToken(request):
    print("setToken! ")
    rightNow = int(time.time())
    getNew = False
    if tokenHolder['when'] == None:
        # New it up!
        getNew = True
    elif (rightNow - tokenHolder['when']) > 5.0:
        # Get a new one!
        getNew = True
        print("setToken! B  ")

    if getNew == True:
        async with aiohttp.ClientSession() as session:
            token = await fetch(session, 'http://localhost:5000/jwttoken')
            tokenHolder['when'] = rightNow
            tokenHolder['token'] = token
            print("Get a new value  {}".format(tokenHolder ))
    else:
        print("setToken! C ")
        print("Use the old one {}".format(tokenHolder ))

async def exec(request):
    await setToken(request)
    print("exec and the token is {}".format( tokenHolder))
    msg = 'zoom hello world and {} when {}'.format(tokenHolder['token'], tokenHolder['when'])
    return web.Response(text=msg)

async def getEndpoints(request):
    endpoints = {}
    path = "config.json"
    with open(path) as f:
        data = json.load(f)
        return web.json_response(data)

app = web.Application()
app.on_startup.append(setToken)
app.add_routes([web.get('/exec', exec), web.get('/getEndpoints', getEndpoints)])

if __name__ == '__main__':
    web.run_app(app)