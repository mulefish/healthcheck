from aiohttp import web
import aiohttp
import asyncio

import time

tokenHolder = {}
tokenHolder['token'] = None
tokenHolder['when'] = None

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def setToken(request):
    rightNow = int(time.time())
    getNew = False
    if tokenHolder['when'] == None:
        # New it up!
        getNew = True
    elif (rightNow - tokenHolder['when']) > 5.0:
        # Get a new one!
        getNew = True

    if getNew == True:
        async with aiohttp.ClientSession() as session:
            token = await fetch(session, 'http://localhost:5000/jwttoken')
            tokenHolder['when'] = rightNow
            tokenHolder['token'] = token
            print("Get a new value  {}".format(tokenHolder ))
    else:
        print("Use the old one {}".format(tokenHolder ))

async def exec(request):
    msg = 'zoom hello world and {} when {}'.format(tokenHolder['token'], tokenHolder['when'])
    return web.Response(text=msg)

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.on_startup.append(setToken)
app.add_routes([web.get('/exec', exec), 
                web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)