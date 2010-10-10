#!/usr/bin/env python

from mpd import MPDFactory
from twisted.internet import reactor

def letsDoSomething(connector):
    def myFinalListResult(result):
        print 'Yeah, thats my list of results for each command in the ' \
              'list %s' % result

    def myItemResult(result):
        print 'Hey the command returned %s' % result

    # Every command in the list returns the normal information like
    # it would have been called normally. The command_list_end command
    # returns a list of all results from each command in the list.
    #
    # BEWARE ...
    #   command_list operations never return a generator but a list!
    connector.command_list_ok_begin()
    connector.add(MY_FILE).addCallback(myItemResult)
    connector.add(MY_FILE).addCallback(myItemResult)
    connector.command_list_end().addCallback(myFinalListResult)

m = MPDFactory()
m.connectionMade = letsDoSomething

reactor.connectTCP('MPD_HOST', 6600)
reactor.run()
