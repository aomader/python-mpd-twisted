#!/usr/bin/env python

# Use command_lists whenever possible for example to chain update or
# add operations to increase your overall performance.

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
    # Start our command_list operation.
    protocol.command_list_ok_begin()

    # Lets ask the server 10 times for its status
    for i in xrange(1, 11):
        # Each command inside a command_list is like a normal command,
        # except that it never returns a generator and that MPD won't start
        # processing your request until you've send a command_list_end.
        # That means yielding in this very place would block continuously.
        protocol.status()

    # We get a list of all results for each command we issued during our
    # command list operation. Each single command gets the result for its
    # own operation as well, but you got to remember that MPD wont start
    # to process your commands until you've issued command_list_end.
    # An important point is that command_list operations always return a
    # list instead of a generator, no matter what you configured.
    result_list = yield protocol.command_list_end()

    print 'The server\'s 10 statuses: %s' % result_list
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
