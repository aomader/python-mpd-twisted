#!/usr/bin/env python

from mpd import MPDFactory
from twisted.internet import reactor

def letsDoSomething(connector):
    def myResult(result):
        print 'Yeah I got the status %s' % result
    connector.status().addCallback(myResult)

m = MPDFactory()
m.connectionMade = letsDoSomething

reactor.connectTCP('MPD_HOST', 6600)
reactor.run()
