from defs import *

class Block:
    def __init__(self, a, b, block_type='normal'):
        self.x = a 
        self.y = b
        self.block_type = block_type  # Can be 'normal', 'corner', 'edge', etc.
