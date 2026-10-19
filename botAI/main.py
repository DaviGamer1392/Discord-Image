import discord
from discord.ext import commands
from visao_computacional import classificar_imagem

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send('he ' * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename

            caminho_arquivo = f'./{file_name}'
            await attachment.save(caminho_arquivo)
            await ctx.send(f'Arquivo {file_name} recebida! A IA está pensando... ')

            try:
                classe, confianca = classificar_imagem(caminho_arquivo)

                porcentagem_confianca = confianca * 100
                await ctx.send(f'eu acho que isso é: {classe}, (certeza: {porcentagem_confianca:.2f}%)')

            except Exception as e:
                await ctx.send(f'Ops! Tive um problema ao analisar a imagem com a IA.')
                print(f'Erro na IA: {e}')


bot.run('Token')