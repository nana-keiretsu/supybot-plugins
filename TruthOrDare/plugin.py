###
# Licensed under the WTFPLv2
# Full license text can be found here: http://www.wtfpl.net/about/
# I'd put copyright, but that's inherent in the US and I prefer copyleft.
###

class TruthOrDare(callbacks.Plugin):
    """Helps organize games of Truth or Dare
    """
    pass

    def ask(self, irc, msg, args, nick):
      """[<nick>]
      Asks <nick> whether they want to choose truth or dare.
      """
      irc.reply(str(result),prefixNick=True)

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

    def pass(self, irc, msg, args):
      """[]
      Passes your turn in a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    pass = wrap(pass)

    def truth(self, irc, msg, args):
      """[]
      Selects Truth in a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    truth = wrap(truth)

    def dare(self, irc, msg, args):
      """[]
      Selects Dare in a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    dare = wrap(dare)

    def double(self, irc, msg, args):
      """[]
      Selects both Truth and Dare in a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    double = wrap(double)

    def players(self, irc, msg, args):
      """[]
      Shows players in a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    players = wrap(players)

    def tod(self, irc, msg, args):
      """[]
      Configures settings for a game of Truth or Dare.
      """
      irc.reply(_('You have passed!'),prefixNick=True)

    tod = wrap(tod)
    
Class = TruthOrDare