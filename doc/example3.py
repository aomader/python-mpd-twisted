#!/usr/bin/env python

# That does the exact same thing as in example1 but it looks more like
# synchronous way of doing it.

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.internet.protocol import ClientCreator

# Import the protocol. MPD_HOST and MPD_PORT try to read the appropriate
# environment variables or fallback to the default values.
from mpd import MPD_HOST, MPD_PORT, MPDProtocol

# Called after the connection attempt succeeded. You can use protocol with
# commands described in doc/commands.txt since its just an instance of
# MPDProtocol.
# The inlineCallbacks decorator lets us write asynchronous code in a
# synchronous fashion.
@inlineCallbacks
def connected(protocol):
    # We yield and let the reactor do what ever he wants until we got the
    # data we want and can continue from the exact same point. It may
    # look like synchronous but it actually isn't. :)
    result = yield protocol.status()

    print 'The server\'s status: %s' % result
    reactor.stop()

# This function gets called in case the connector wasn't able to establish
# a connection. If you wan't to watch for connection problems after you
# have been connected you may override protocol.connectionLost
def couldntConnect(failure):
    print 'Couldn\'t connect: %s' % failure.getErrorMessage()
    reactor.stop()

connector = ClientCreator(reactor, MPDProtocol)

# Create the connection and register our callback with the Deferred.
defer = connector.connectTCP(MPD_HOST, MPD_PORT)
defer.addCallback(connected)
defer.addErrback(couldntConnect)

reactor.run()
