import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
    print('Zalogowano do bota')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        m1 = discord.Embed(title = "Błąd", description = "❌ Nie masz uprawnień do wykonania tego polecenia ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        m1 = discord.Embed(title = "Błąd", description = "❌ Nieprawidłowy argument polecenia ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.message.delete()
    elif isinstance(error, commands.CommandNotFound):
        m1 = discord.Embed(title = "Błąd", description = "❌ Nie znaleziono polecenia ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.send.message.delete()


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit = amount)

    em = discord.Embed(description=f"Usunięto {amount} wiadomości.", colour=discord.Colour.blue())
    await ctx.send(embed=em)


@client.group(invoke_without_command=True)
@commands.has_permissions(send_messages=True)
async def user(ctx, member : discord.Member):
    embed =  discord.Embed(colour = discord.Colour.purple())
    embed.add_field(name = "ID Użytkownika", value = member.id, inline = False)
    embed.add_field(name="Dołączenie na serwer", value=member.joined_at.date(), inline=False)
    embed.set_author(name = member.display_name, icon_url = member.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

client.run("OTE2NzAzNjY5ODk3MDE1MzM3.YauA0g.6DIW2nj446W5q3eqFRzgiTm4Axg")