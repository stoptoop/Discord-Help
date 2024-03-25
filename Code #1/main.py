import disnake # импортируем библиотеку disnake
from disnake.ext import commands
# для большей информации можете перейти на сайт https://docs.disnake.dev/en/latest/ext/commands/commands.html

intents = disnake.Intents.all() # для полной информации для чего: https://ru.guide.disnake.dev/popular-topics/intents
bot = commands.Bot(command_prefix='!', intents = intents) # даем префикс боту


@bot.event
async def on_ready(): # при включении бота он будет писать в консоль "Бот готов!" (Для удобства)
    print("Бот готов!")


@bot.slash_command() # создаем слэш команду
async def ping(ctx): # слэш команда с названием ping
    await ctx.send("Понг!")


@bot.slash_command() # создаем слэш команду
async def invisible_ping(ctx): # слэш команда с названием invisible_ping
    await ctx.send("Сообщение которое видно только вам!", ephemeral=True) # добовляем к слэш команде ephermal и даем значение True для того чтобы сообщение было видно только тому, кто вызвал команду


@bot.slash_command(description="Команда с описанием!") # создаем слэш команду, с полем description и в нём пишем наше описание для команды
async def ping_description(ctx): # слэш команда с названием ping_description
    await ctx.send("Понг!") # после await пишем ctx.send("text") что позволит нам отправить ответ на вызов команды



bot.run("TOKEN")        # для создания токена перейдите на сайт https://discord.com/developers/applications
