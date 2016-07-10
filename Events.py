import Action
class Event (object):
    def __init__(self, name, idx, **kw):
        self.name = name
        self.idx = idx
        self.proporties = kw
    def eventHappens(self):
        try:
            act = self.proporties['action']
            self.proporties.pop('action')
            x = self.run(self.idx, **self.proporties)
            self.proporties['action'] = act
            return x
        except:
            print 'If you want a special action to run, subclass this class or add an action to self.proporties underthe key \'action\'.'
            return (self.name, self.idx, self.proporties)


