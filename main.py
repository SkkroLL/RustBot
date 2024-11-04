import discord, raid_resources, config, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
config_bot = {
    'prefix': os.getenv('PREFIX'),
    'token': os.getenv('TOKEN_BOT'),
}

bot = commands.Bot(token=config_bot['token'], intents=intents, command_prefix=config_bot['prefix'])

help_command = '''
!commands (!c) - Выводит список всех команд бота 

**посчитать ресурсы для крафта:**

!с4 (количество) - для крафта с4
!rockets (!roc) (количество) - для крафта ракет
!beancan_grenade (!gr) (количество) - для крафта бобовых гранат
!satchel (!sa) (количество) - для крафта сачелей
!explosive_ammo (!ea) (количество) - для крафта разрывных патронов

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

@bot.command(aliases=['roc'])
async def rockets(ctx, quantity):
    res_rockets = raid_resources.rocket(int(quantity))
    embed = discord.Embed(
        title='Ракеты',
        description='Количество ресурсов для крафта ракет',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/9/95/Rocket_icon.png/revision/latest?cb=20151106061039'
    )
    embed.add_field(
        name='Количетсво ракет: ',
        value=quantity,
        inline=False,
    )
    embed.add_field(
        name='взрывчатое вещество: ',
        value=res_rockets['взрывчатое вещество'],
        inline=False,
    )
    embed.add_field(
        name='Металлические трубы: ',
        value=res_rockets['Металлические трубы'],
        inline=False,
    )
    embed.add_field(
        name='Порох: ',
        value=res_rockets['Порох для ракет'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для взрывчатого вещества: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Порох: ',
        value=res_rockets['Порох для ВВ'],
        inline=False,
    )
    embed.add_field(
        name='Топливо: ',
        value=res_rockets['Топливо'],
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_rockets['Сера для ВВ'],
        inline=False,
    )
    embed.add_field(
        name='Металл: ',
        value=res_rockets['Металл'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для пороха: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_rockets['Сера для пороха'],
        inline=False,
    )
    embed.add_field(
        name='Уголь: ',
        value=res_rockets['Уголь'],
        inline=False,
    )
    await ctx.reply(embed=embed)
@rockets.error
async def rockets_error(ctx, error):
    await ctx.reply(f'**Произошла ошибка:** {error}')
@bot.command(aliases=['gr'])
async def beancan_grenade(ctx, quantity):
    res_grenade = raid_resources.beancan_grenade(int(quantity))
    embed = discord.Embed(
        title='бобовые гранаты',
        description='Количество ресурсов для крафта бобовых гранат',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/b/be/Beancan_Grenade_icon.png/revision/latest?cb=20151106060959'
    )
    embed.add_field(
        name='Количетсво бобовых гранат: ',
        value=quantity,
        inline=False,
    )
    embed.add_field(
        name='Металл: ',
        value=res_grenade['Металл'],
        inline=False,
    )
    embed.add_field(
        name='Порох: ',
        value=res_grenade['Порох'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для пороха: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_grenade['Сера'],
        inline=False,
    )
    embed.add_field(
        name='Уголь: ',
        value=res_grenade['Уголь'],
        inline=False,
    )
    await ctx.reply(embed=embed)
@beancan_grenade.error
async def beancan_grenade_error(ctx, error):
    await ctx.reply(f'**Произошла ошибка:** {error}')
@bot.command(aliases=['sa'])
async def satchels(ctx, quantity):
    res_satchels = raid_resources.satchels(int(quantity))
    embed = discord.Embed(
        title='сачели',
        description='Количество ресурсов для крафта сачелей',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/b/ba/Satchel_Charge_icon-0.png/revision/latest?cb=20191108210142'
    )
    embed.add_field(
        name='Количетсво сачелей: ',
        value=quantity,
        inline=False,
    )
    embed.add_field(
        name='Бобовая граната: ',
        value=res_satchels['Бобовая граната'],
        inline=False,
    )
    embed.add_field(
        name='Маленький тайник: ',
        value=res_satchels['Маленький тайник'],
        inline=False,
    )
    embed.add_field(
        name='Веревка: ',
        value=res_satchels['Веревка'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для Бобовых гранат: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='порох: ',
        value=res_satchels['порох'],
        inline=False,
    )
    embed.add_field(
        name='Металл: ',
        value=res_satchels['Металл'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для пороха: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_satchels['Сера'],
        inline=False,
    )
    embed.add_field(
        name='Уголь: ',
        value=res_satchels['Уголь'],
        inline=False,
    )
    await ctx.reply(embed=embed)
@satchels.error
async def satchels_error(ctx, error):
    await ctx.reply(f'**Произошла ошибка:** {error}')
@bot.command(aliases=['ea'])
async def explosive_ammos(ctx, quantity):
    res_ammos = raid_resources.explosive_ammos(int(quantity))
    embed = discord.Embed(
        title='разрывные патроны',
        description='Количество ресурсов для крафта разрывных патронов',
        color=0xd69d00,
    )
    embed.set_thumbnail(
        url='https://static.wikia.nocookie.net/play-rust/images/3/31/Explosive_5.56_Rifle_Ammo_icon.png/revision/latest?cb=20151106061449'
    )
    embed.add_field(
        name='Количетсво разрывных патронов: ',
        value=quantity,
        inline=False,
    )
    embed.add_field(
        name='Порох: ',
        value=res_ammos['Порох'],
        inline=False,
    )
    embed.add_field(
        name='Металл: ',
        value=res_ammos['Металл'],
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_ammos['Сера для патронов'],
        inline=False,
    )
    embed.add_field(
        name='Ресурсы для пороха: ',
        value='',
        inline=False,
    )
    embed.add_field(
        name='Уголь: ',
        value=res_ammos['Уголь'],
        inline=False,
    )
    embed.add_field(
        name='Сера: ',
        value=res_ammos['Сера для пороха'],
        inline=False,
    )
    await ctx.reply(embed=embed)
@explosive_ammos.error
async def explosive_ammos_error(ctx, error):
    await ctx.reply(f'**Произошла ошибка:** {error}')


if __name__ == '__main__':
    bot.run(config_bot['token'])

