###
# Licensed under the WTFPLv2
# Full license text can be found here: http://www.wtfpl.net/about/
# I'd put copyright, but that's inherent in the US and I prefer copyleft.
###

import supybot.utils as utils
from supybot.commands import *
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring
_ = PluginInternationalization('Games')

class TruthOrDare(callbacks.Plugin):
    """Helps organize games of Truth or Dare
    """
    pass

    def ask(self, irc, msg, args, nick):
      """[<nick>]
      Asks <nick> whether they want to choose truth or dare.
      """
      irc.reply(_('Asked nick to whatever.'),prefixNick=True)

    ask = wrap(ask,['somethingWithoutSpaces'])

    def play(self, irc, msg, args):
      """[]
      Enters you as a player a game of Truth or Dare.
      """
      irc.reply(_('You have joined the game!'),prefixNick=True)

    play = wrap(play)

    def leave(self, irc, msg, args):
      """[]
      Leaves a game of Truth or Dare.
      """
      irc.reply(_('You have left the game!'),prefixNick=True)

    play = wrap(play)

    def truth(self, irc, msg, args):
      """[]
      Selects Truth in a game of Truth or Dare.
      """
      irc.reply(_('You have selected Truth!'),prefixNick=True)

    truth = wrap(truth)

    def dare(self, irc, msg, args):
      """[]
      Selects Dare in a game of Truth or Dare.
      """
      irc.reply(_('You have selected Dare!'),prefixNick=True)

    dare = wrap(dare)

    def double(self, irc, msg, args):
      """[]
      Selects both Truth and Dare in a game of Truth or Dare.
      """
      irc.reply(_('You have selected Truth and Dare!'),prefixNick=True)

    double = wrap(double)

    def players(self, irc, msg, args):
      """[]
      Shows players in a game of Truth or Dare.
      """
      irc.reply(_('Players currently in the game...'),prefixNick=True)

    players = wrap(players)

    def tod(self, irc, msg, args):
      """[]
      Configures settings for a game of Truth or Dare.
      """
      irc.reply(_('Settings for Truth or Dare...'),prefixNick=True)

    tod = wrap(tod)
    
Class = TruthOrDare