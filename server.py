from aiohttp import web
import time

tokenHolder = {}
tokenHolder['token'] = None
tokenHolder['when'] = None

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def setToken():
    global tokenHolder
    rightNow = time.time()
    if rightNow - tokenHolder['when'] > 60:
        async with aiohttp.ClientSession() as session:
            token = await fetch(session, 'http://localhost:5000/jwttoken')
            tokenHolder['when'] = rightNow
            tokenHolder['token'] = token


async def exec(request):
    return web.Response(text='hello world')

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/exec', exec), 
                web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)