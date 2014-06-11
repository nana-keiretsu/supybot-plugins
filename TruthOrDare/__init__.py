###
# Licensed under the WTFPLv2
# Full license text can be found here: http://www.wtfpl.net/about/
# I'd put copyright, but that's inherent in the US and I prefer copyleft.
###

"""
This plugin handles the game Truth or Dare for a channel.
"""

import supybot
import supybot.world as world

# The usual version stuff
__version__ = ""
__author__ = "Sevens System"
__contributors__ = {}
__url__ = 'https://github.com/SevensSystem/supybot-plugins/tree/master/TruthOrDare'

# Have to do this for plugins
import config
import plugin
reload(plugin)

# For testing purposes
if world.testing:
    import test

Class = plugin.Class
configure = config.configure






