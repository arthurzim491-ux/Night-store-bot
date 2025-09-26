import discord
from discord.ext import commands
import os

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

# Quando o bot ficar online
@bot.event
async def on_ready():
    print(f"🤖 Bot {bot.user} está online!")
    await bot.change_presence(activity=discord.Game(name="Night Store 🛒"))

# Comando de boas-vindas
@bot.command()
async def boasvindas(ctx):
    await ctx.send("✨ Bem-vindo(a) à **Night Store**! Aqui você encontra os melhores produtos 🌙")

# Comando de ajuda
@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title="📌 Comandos da Night Store",
        description="Aqui estão os comandos disponíveis:",
        color=discord.Color.purple()
    )
    embed.add_field(name="!boasvindas", value="Mensagem de boas-vindas", inline=False)
    embed.add_field(name="!produtos", value="Lista os produtos disponíveis", inline=False)
    embed.add_field(name="!horario", value="Mostra o horário de funcionamento", inline=False)
    await ctx.send(embed=embed)

# Comando de produtos
@bot.command()
async def produtos(ctx):
    embed = discord.Embed(
        title="🛍 Produtos da Night Store",
        description="Confira nossos produtos disponíveis:",
        color=discord.Color.blue()
    )
    embed.add_field(name="🎧 Headset Gamer", value="R$ 199,90", inline=False)
    embed.add_field(name="⌨️ Teclado Mecânico", value="R$ 299,90", inline=False)
    embed.add_field(name="🖱 Mouse Gamer RGB", value="R$ 149,90", inline=False)
    embed.set_footer(text="Night Store - Qualidade e confiança 🌙")
    await ctx.send(embed=embed)

# Comando de horário
@bot.command()
async def horario(ctx):
    await ctx.send("🕒 A **Night Store** funciona das **9h às 20h**, todos os dias!")

# Iniciar o bot
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
