import discord
from discord import Option
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord.utils import get
import random
import asyncio
import embed_builder
import os
from discord import ChannelType
import time
from discord.utils import get

bot = commands.Bot(command_prefix='/')

servers = 987154617186013246 #server ids

named_tuple = time.localtime() # получить struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents, command_prefix= '!')

#READYBOT
@bot.event
async def on_ready():
    clear = lambda: os.system('cls')
    clear()
    print("We have logged in!")
    with open('logs\log.txt', 'a') as log:
        log.write(f'{time_string} We have logged in!\n')

#EMBEDS
embed = discord.Embed(
    title="Вас нет в реестре Администрации", 
    description="Для того чтобы попасть в реестр вам нужно отписать Yvetlin.#6678", 
    colour=0x9300f5)
embed2 = discord.Embed(
    title="Bot Commands", 
    description="Команды в основном разрешены только для людей в реестре, для того чтобы попасть туда нужно написать автору данного бота.\nТри типа прав в боте:\nA - Администратор\nM - Модератор\nU - Пользователь",
    colour=0x9300f5)
embed3 = discord.Embed(
    title="Неверный код для восстановления/выдачи статуса", 
    description="Для того чтобы восстановить коды отписать: Yvetlin.#6678", 
    colour=0x9300f5)
embed4 = discord.Embed(description="Это единственный открытый канал, на который у меня включены все типы уведомлений.\n1. По хуйне не пинговать\n2. Хуйню не писать\n\nСюда отписывать если: \n1. Что то пошло по пизде\n2. Кому-то дать пизды\n3. Выдача прав\n4. Добавить бота и прочую хуйню если нет прав на такие деяния\n\nЕсли делайте хуйню кидаю в кулдаун и вытаскиваю явно не на следующий день\n(если его снимут, накину еще и той личности которая его сняла, предварительно сняв права нахуй, либо вовсе забаню, мне впринципе похуй как-то)",
                      colour=0x8700f5)

embed2.set_author(name="yvetlin.", url="https://vk.com/yvetlin", icon_url="https://imgur.com/yhBek2C.gif")
embed2.add_field(name="/aban [member] [reason]", value="перманентная блокировка пользователя на сервере (A)\n")
embed2.add_field(name="/kick [member] [reason]", value="исключение пользователя с сервера (A)")
embed2.add_field(name="/addpass [member]", value="выдача админ-прав на сервере (A)\nтак же добавляется автоматически в реестр уровня администратор\n")
embed2.add_field(name="/depass [member]", value="изъятие прав админа на сервере (А)\nтак же удаляется из реестра уровня администратор и в дальнейшем не добавляется\n")
embed2.add_field(name="/pasha", value="пуш Паши, впоследствии вы можете выбить \"- натс\"!\n")
embed2.add_field(name="/ping [member]", value="тип любого пользователя на сервере\n")
embed2.set_image(url="https://cdn.fishki.net/upload/post/2021/07/09/3833029/06d12d9929ffb2e0044dbf8b3f23b7cd.jpg")
embed2.set_footer(text="Copyright by yvetlin.", icon_url="https://slate.dan.onl/slate.png")

embed4.set_author(name="Ticket system")
embed4.add_field(name="Если бот в сети, советую воспользоваться командой /ticket и описать просьбу, проблему там!",
                value="")
embed4.set_footer(text="Copyright by yvetlin.")


#MAIN
@bot.slash_command()
async def main(ctx):
    await ctx.respond(embed=embed2)
    with open('logs\log.txt', 'a') as log:
        log.write(f"{time_string} <@{ctx.author.id}> take main\n")

#BAN
@bot.slash_command(guild_ids = servers, name = "aban", description = "Bans a member")
async def aban(ctx, member, reason: Option(str, description = "Why?", required = False)):
    with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
    if ctx.author.id in arr:
        await ctx.send(embed=embed)
    else:
        if member.id == ctx.author.id: #checks to see if they're the same
            await ctx.respond("BRUH! You can't ban yourself!")
        elif member.guild_permissions.administrator:
            await ctx.respond("Stop trying to ban an admin! :rolling_eyes:")
        else:
            if reason == None:
                reason = f"None provided by {ctx.author}"
                await member.ban(reason = reason)
                await ctx.respond(f"<@{ctx.author.id}>, <@{member.id}> has been banned successfully from this server!\n\nReason: {reason}")
    
    with open('log.txt', 'a') as log:
        log.write(f'{time_string} <@{ctx.author.id}>, <@{member.id}> has been banned successfully from this server!Reason: {reason}\n')
        
@aban.error
async def banerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("You need Ban Members and Administrator permissions to do this!")
    else:
        await ctx.respond("Something went wrong...") #most likely due to missing permissions
        raise error

#KICK
@bot.slash_command(guild_ids = servers, name = "kick", description = "Kicks a member")
async def kick(ctx, member: Option(discord.Member, description = "Who do you want to kick?"), reason: Option(str, description = "Why?", required = False)):
    with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
    if ctx.author.id in arr:
        await ctx.send(embed=embed)
    else:
        if member.id == ctx.author.id: #checks to see if they're the same
            await ctx.respond("BRUH! You can't kick yourself!")
        elif member.guild_permissions.administrator:
            await ctx.respond("Stop trying to kick an admin! :rolling_eyes:")
        else:
            if reason == None:
                reason = f"None provided by {ctx.author}"
            await member.kick(reason = reason)
            await ctx.respond(f"<@{ctx.author.id}>, <@{member.id}> has been kicked from this server! \n\n Reason: {reason}")
    
    with open('log.txt', 'a') as log:
        log.write(f'{time_string} <@{ctx.author.id}>, <@{member.id}> has been kicked from this server! Reason: {reason}\n')

@kick.error
async def kickerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("You need Kick Members and Administrator permissions to do this!")
    else:
        await ctx.respond("Something went wrong...") #most likely due to missing permissions 
        raise error

#LOGINA
@bot.slash_command()
async def alogin(ctx):
    with open('users\Admins.txt', 'r', encoding='utf-8') as f:
        arr = [int(i.rstrip()) for i in f]
    
    for i in arr:
        admin = i
        print(admin)

        user = get(bot.get_all_members(), id=admin)
        if user:
            channel = await user.create_dm()
        else:
            continue

        with open('logs\pass.txt', 'r', encoding='utf-8') as p:
            arr2 = [i.rstrip() for i in p]
        
        if i in arr:
            await channel.send("Резервные кодировки для восстановления прав администратора на сервере: ")
            await channel.send(arr2)
    
    with open('logs\paslogs.txt', 'a') as log:
        log.write(f'{time_string} {ctx.author} get passwords at {time}\n')

#ADDMOD
@bot.slash_command(pass_context=True)
async def mod(ctx, member: discord.Member):
    with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]

    if ctx.author.id in arr:
        await ctx.respond(embed=embed)
    else:
        role_get = get(member.guild.roles, id=1003058963799089273) 
        await member.add_roles(role_get)

    with open('users\DeTest.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
        if f'{member.id}' in arr:
            print (member.id, ' ', arr)
            await ctx.respond(f' <@{member.id}>, Вы не будете внесены в реестр уровня Модератор')
        else:
            with open('users\Testers.txt', 'a') as log:
                log.write(f"{member.id}\n")
            await ctx.respond(f' <@{member.id}>, вы назначены на пост модератора.')
    
    with open('logs\paslogs.txt', 'a') as log:
        log.write(f"{time_string} <@{ctx.author.id}> addmoded <@{member.id}>\n")

#DEMOD
@bot.slash_command(pass_context=True)
async def demod(ctx, member: discord.Member):
    with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
    if ctx.author.id in arr:
        await ctx.respond(embed=embed)
    else:
        role_get = get(member.guild.roles, id=1003058963799089273) 
        await member.remove_roles(role_get)
        await ctx.respond("Done!")
    
    with open('logs\paslogs.txt', 'a') as log:
        log.write(f"{time_string} <@{ctx.author.id}> demoded <@{member.id}>\n")
    
    with open("users\Testers.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            print(i.strip('\n'), ' ', member.id)
            if i.strip('\n') != f"{member.id}":
                f.write(i)
        f.truncate()
    
    with open('users\DeTest.txt', 'a') as log:
        log.write(f"{member.id}\n")

#DEPASS
@bot.slash_command(pass_context=True)
async def depass(ctx, member: discord.Member):
    with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
    if ctx.author.id in arr:
        await ctx.respond(embed=embed)
    else:
        role_get = get(member.guild.roles, id=1105855529147973783) 
        await member.remove_roles(role_get)
        channel = await ctx.author.create_dm()
        await channel.send("Done!")

    
    with open('logs\paslogs.txt', 'a') as log:
        log.write(f"{time_string} <@{ctx.author.id}> depassed <@{member.id}>\n")
    
    with open("users\Admins.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            print(i.strip('\n'), ' ', member.id)
            if i.strip('\n') != f"{member.id}":
                f.write(i)
        f.truncate()
    
    with open('users\DePass.txt', 'a') as log:
        log.write(f"{member.id}\n")
    
#ADDPASS
@bot.slash_command(pass_context=True)
async def addpass(ctx, member: discord.Member, password="code from DM with bot"):
    with open('logs\pass.txt', 'r' ,encoding='utf-8') as f:
        arr = [i.rstrip() for i in f]
        print(password,' ', arr)
    if f"{password}" in arr:
        with open('users\Admins.txt', 'r' ,encoding='utf-8') as f:
            arr = [i.rstrip() for i in f]
        with open('logs\paslogs.txt', 'a') as log:
                log.write(f"{time_string} LUCKY <@{ctx.author.id}> addpassed <@{member.id}> with password: {password}\n")
        if ctx.author.id in arr:
            await ctx.respond(embed=embed)
        else:
            role_get = get(member.guild.roles, id=1105855529147973783) 
            await member.add_roles(role_get)

        with open('users\DePass.txt', 'r' ,encoding='utf-8') as f:
            arr = [i.rstrip() for i in f]
        
        if f'{member.id}' in arr:
            print (member.id, ' ', arr)
            await ctx.respond(f' <@{member.id}>, Вы не будете внесены в реестр уровня Админитратор')
        else:
            with open('users\Admins.txt', 'a') as log:
                log.write(f"{member.id}\n")
            await ctx.respond(f' <@{member.id}>, вы назначены на пост админитратора.')
    
    else:
        await ctx.send(embed=embed3)
        with open('logs\paslogs.txt', 'a') as log:
            log.write(f"{time_string} UNLUCKY <@{ctx.author.id}> addpassed <@{member.id}> with password: {password}\n")


#SHUFFLE
@bot.slash_command()
async def suffle(ctx, voice1: discord.VoiceChannel, voice2: discord.VoiceChannel):
    print("err")
    await ctx.respond("Работаю")
    for guild in bot.guilds:
        for member in guild.members:
            print(member.name)
            if member in voice1.members:
                await ctx.respond("Начало определения группы")
                rand = random.choice([True, False])
                if rand:
                    await ctx.respond("Пользователь определен в группу 1")
                    print('1')
                    await member.move_to(voice2)
                
                else:
                    await ctx.respond("Пользователь определен в группу 2")
                    print('2')
                    await member.move_to(voice1)
            else:
                print('Бот')
    with open('logs\log.txt', 'a') as log:
        log.write(f"{time_string} {ctx.author} shuffle{voice2}, {voice1}\n")

#TICKETS
@bot.slash_command()
async def ticket(ctx, text):
    await ctx.delete()
    user = get(bot.get_all_members(), id=457307609490522132)
    if user:
        channel = await ctx.user.create_dm()
        await channel.send(f"{time_string}, Author: <@{ctx.author.id}> \n Ticket: {text}")
    with open('tickets.txt', 'a') as log:
        log.write(f"{time_string} <@{ctx.author.id}> take ticket {user.name}: {text}\n")
    channel2 = await ctx.author.create_dm()
    await channel2.send(f"Спасибо за обращение! Ваш запрос отправлен разработчику, ожидайте!")

@bot.slash_command()
async def rick(ctx):
    await ctx.send(f"{embed4}, \n twitch")

bot.run('') #token: KEEP THIS SAFE, from your developer portal