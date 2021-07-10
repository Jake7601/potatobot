import asyncio, discord
from discord.ext import commands
from discord.ext.commands import Bot
  
app = commands.Bot(command_prefix='!')
  
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)
    await app.change_presence(status=discord.Status.online, activity=discord.Game("봇 작동중"))
      
@app.command()
async def 이벤트(ctx):
    event=discord.Embed(title="노리서버 이벤트 안내", description="7/24(토)~  - 노리 올림픽 \n 올림픽 폐막후 - 1.17 버전업" , color=0xFF5733)
    await ctx.send(embed=event)

@app.command()
async def 지도(ctx):
    maps=discord.Embed(title="노리서버 지도", description="7/4(일) 기준입니다." , color=0xFF5733)
    maps.set_image(url='https://i.ibb.co/LvFF4vt/2021-07-04-10-38-30.png')
    await ctx.send(embed=maps)

@app.command()
async def 서버(ctx):
    server=discord.Embed(title="노리서버", description="노리서버 주소 : playpark.aternos.me \n 노리서버 버전 : 1.16.3" , color=0xFF5733)
    await ctx.send(embed=server)    

@app.command()
async def 감자봇(ctx):
    await ctx.send("안녕! 내 이름은 감자! \n 너의 노리서버 생활을 돕기위해 왔지! \n 혹시 궁금한게 있으면 !명령어 를 입력해봐!")

@app.command()
async def 명령어(ctx):
    comlist=discord.Embed(title="감자봇 명령어 리스트", description="!감자봇 : 감자봇의 소개글입니다. \n !서버 : 서버의 정보를 나타냅니다. \n !지도 : 서버의 지도를 나타냅니다. \n !이벤트 : 서버의 이벤트를 나타냅니다." , color=0xFF5733)
    await ctx.send(embed=comlist)   

app.run('ODYzMjI1NjQxMTgwMDY5OTEw.YOjzhg.XJQNrVxrSYp1LhKGA5dXSk_L6eA')