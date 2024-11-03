import discord, raid_resources, config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
config_bot = {
    'prefix': config.prefix,
    'token': config.TOKEN,
}

bot = commands.Bot(token=config_bot['token'], intents=intents, command_prefix=config_bot['prefix'])

help_command = '''
!commands (!c) - Выводит список всех команд бота 

**посчитать ресурсы для крафта:**

!с4 (количество) - для крафта с4
!rocket (количество) - для крафта ракет
!beancan_grenade (количество) - для крафта бобовых гранат
!satchel (количество) - для крафта сачелей
!explosive_ammo (количество) - для крафта разрывных патронов

**Вывести таблицу для рейда:**
!raid_table (!r) - таблица для рейда

'''
@bot.event
async def on_ready():
    print(f'Bot status: {bot.status}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!commands'))

@bot.command(aliases=['c'])
async def commands(ctx):
    embed = discord.Embed(
        title='RustBot',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/3/37/Mechanics_icon.png/revision/latest/scale-to-width-down/90?cb=20150326025228'
    )
    embed.add_field(
        name='Список команд:',
        value=help_command,
    )
    await ctx.reply(embed=embed)

@bot.command(aliases=['r'])
async def raid_table(ctx):
    embed = discord.Embed(
        title='Таблица для рейда',
        color=0xd69d00,
    )
    embed.set_image(
        url='https://sun9-14.userapi.com/impg/gDw77XSU1SFsyB_X_LxfSsD_6pMinqE0zPn0aw/bFFlXTw9OUg.jpg?size=1280x709&quality=96&sign=d0c87cabb881e5656ed36084fd15c010&c_uniq_tag=vngltAcq_rsTdrqhW97w4wQxoIqXizEi1UZdFGP_fCI&type=album'
    )
    await ctx.reply(embed=embed)

@bot.command()
async def c4(ctx, quantity):
    res_c4 = raid_resources.c4(int(quantity))
    embed = discord.Embed(
        title='C4',
        description='Количество ресурсов для крафта C4',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/6/6c/Timed_Explosive_Charge_icon.png/revision/latest?cb=20151106061610'
    )
    embed.add_field(
        name='Количетсво С4: ',
        value=quantity,
        inline=False,
    )
    embed.add_field(
        name='взрывчатое вещество: ',
        value=res_c4['взрывчатое вещество'],
        inline=False,
    )
    embed.add_field(
        name='Ткань: ',
        value=res_c4['Ткань'],
        inline=False,
    )
    embed.add_field(
        name='старые микросхемы: ',
        value=res_c4['старые микросхемы'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для взрывчатого вещества: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Порох: ',
        value=res_c4['Порох'],
        inline=False,
    )
    embed.add_field(
        name='Топливо: ',
        value=res_c4['Топливо'],
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_c4['Сера для ВВ'],
        inline=False,
    )
    embed.add_field(
        name='Металл: ',
        value=res_c4['Металл'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для пороха: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_c4['Сера для пороха'],
        inline=False,
    )
    embed.add_field(
        name='Уголь: ',
        value=res_c4['Уголь'],
        inline=False,
    )
    await ctx.reply(embed=embed)
@c4.error
async def c4_error(ctx, error):
    await ctx.reply(f'**Произошла ошибка:** {error}')



bot.run(config_bot['token'])
