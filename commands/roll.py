async def roll(ctx):
    """ Rolls a pseudorandom number from 0 to 100 """
    num = randint(0, 100)
    num = str(num)
    await ctx.send(ctx.message.author.mention + ' rolled ' + num)