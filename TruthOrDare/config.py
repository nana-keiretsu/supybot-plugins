###
# Licensed under the WTFPLv2
# Full license text can be found here: http://www.wtfpl.net/about/
# I'd put copyright, but that's inherent in the US and I prefer copyleft.
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('TruthOrDare', True)

TruthOrDare = conf.registerPlugin('TruthOrDare')
