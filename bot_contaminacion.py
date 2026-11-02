import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot de contaminación conectado")


@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot sobre la contaminación.")
    await ctx.send("Usa estos comandos: $contaminacion, $consejo, $manualidad, $reciclar, $tiempo")


@bot.command()
async def contaminacion(ctx):
    mensaje = """
     CONTAMINACIÓN AMBIENTAL
    Ocurre cuando tiramos basura y dañamos el planeta.
     Aire: humo de carros.
     Agua: basura en los ríos.
     Suelo: plásticos tirados.
    """
    await ctx.send(mensaje)


@bot.command()
async def consejo(ctx):
    await ctx.send(" Consejo: usa botellas reutilizables para no gastar tanto plástico.")



@bot.command()
async def manualidad(ctx):
  
    await ctx.send(" **Idea fácil:** Corta una botella de plástico por la mitad y úsala como maceta para una planta o para guardar tus lápices.")



@bot.command()
async def reciclar(ctx):

    mensaje = """
     **¿Qué se recicla?** Botellas de plástico, cajas de cartón, papel y latas limpias.
     **¿Qué NO se recicla?** Servilletas sucias, pañales y restos de comida.
    """
    await ctx.send(mensaje)


@bot.command()
async def tiempo(ctx):

    mensaje = """
     **¿Cuánto tardan en desaparecer?**
    - Papel: 2 a 5 meses
    - Bolsa de plástico: 15 a 50 años
    - Botella de plástico: 450 años
    - Vidrio: miles de años
    """
    await ctx.send(mensaje)
