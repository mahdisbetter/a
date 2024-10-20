from flask import Flask
import aiohttp
import asyncio 
app = Flask(__name__)

async def send_message():
    async with aiohttp.ClientSession() as session:
        await session.post('https://discord.com/api/webhooks/1297349451647815721/0v1ZFYX78kWnE8C6vyrCO-pQY6DOQWlUbZ4cCQpmj31jAN0YnGqBeSe7hWjIe-TxCLgk', json={'content':'@everyone from first'})

async def callback():
    async with aiohttp.ClientSession() as session:
        await session.get('https://fucking-vercel-2.vercel.app/callback')

async def maina():
    tasks = [callback(), send_message()]
    await asyncio.gather(*tasks)
    
@app.route('/callback')
def main():
    asyncio.run(maina())
    return 'first'
