import asyncio
from motor.motor_asyncio import AsyncioIOMotorClient
from pymongo.server_api import ServerApi

async def ping_server():
    # 자리 표시자를 Atlas 연결 문자열로 바꾸세요.
    uri = "mongodb://root:example@localhost:27017"

    # 새 클라이언트를 만들 때 안정적인 API 버전을 설정합니다.
    client = AsyncioIOMotorClient(uri, server_api=ServerApi('1'))

    # ping을 보내 성공적인 연결을 확인합니다.
    try:
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

asyncio.run(ping_server())
