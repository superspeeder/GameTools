from Interface import *

class Action (object):
    def __init__(self, idx, rfunc):
        self.idx = idx
        self.rfunc = rfunc
    def run(self,idx,**kw):
        return self.rfunc (idx, **kw)


