"""
roulette.py: /KILL roulette
"""
import secrets

from pylinkirc import utils


def hook_privmsg(irc, source, command, args):
    channel = args['target']
    text = args['text']
    try:
        user = irc.users[source]
    except KeyError:
        return

    if channel.lower() == '#roulette' and text.startswith('!roulette'):
        if secrets.randbelow(6) == 1:
            irc.kill(irc.pseudoclient.uid, source, '\x02*BANG*\x02')
        else:
            irc.msg(channel, f'{user.nick}: *CLICK*')

utils.add_hook(hook_privmsg, 'PRIVMSG')
