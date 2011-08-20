from meinheld import server

CLIENT_KEY = 'meinheld.client'
CONTINUATION_KEY = 'meinheld.continuation'
GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

OPCODE_CONTINUATION = 0x0
OPCODE_TEXT = 0x1
OPCODE_BINARY = 0x2
OPCODE_CLOSE = 0x8
OPCODE_PING = 0x9
OPCODE_PONG = 0xa


class Continuation(object):

    def __init__(self, client):
        self.client = client

    def suspend(self, timeout=0):
        return server._suspend_client(self.client, timeout)
    
    def resume(self, *args, **kwargs):
        return server._resume_client(self.client, args, kwargs)
