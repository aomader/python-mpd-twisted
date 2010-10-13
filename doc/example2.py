#!/usr/bin/env python

# Thats like our first example except that we use MPDFactory
# to establish a connection. Thats useful if you got long running connections
# which may get terminated and you don't want to bother yourself reconnecting.

from twisted.internet import reactor

from mpd import MPD_HOST, MPD_PORT, MPDFactory

# Gets called everytime a connection has been established.
# So e.g. directly after startup or if the connection terminates
# and the factory reconnected.
def connectionMade(protocol):
    # Called after the protocol processed the data without an error.
    # For a more "synchronous" way of doing this check doc/example3.py
    def mpdStatus(result):
        print 'The server\'s status: %s' % result
        # We drop the current connection and you'll see, that the factory
        # takes care of the reconnection.
        protocol.transport.loseConnection()
    
    # Register a callback to get the actual result. You may consider to add
    # an errback as well to handle failures.
    protocol.status().addCallback(mpdStatus)

# When a connection dies this function gets called
def connectionLost(protocol, reason):
    print 'Connection lost: %s' % reason

factory = MPDFactory()

# Register our callbacks. No Deferred like in example1, just plain
# callables.
factory.connectionMade = connectionMade
factory.connectionLost = connectionLost

# Connect our factory and run.
reactor.connectTCP(MPD_HOST, MPD_PORT, factory)
reactor.run()
