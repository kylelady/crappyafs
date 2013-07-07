#/usr/bin/env python


class ACL(object):
    def __init__(self, pos, neg):
        '''
        {pos,neg}: dict of {pos,neg} permissions: name: aclstr
        '''
        self.pos = pos
        self.neg = neg

    @staticmethod
    def retrieve(dir, follow=True):
        pass

    def apply(self, dir, follow=True):
        pass

    def _clean(self):
        pass

    def set(self, user, bitmask, negative=False):
        pass

    def remove(self, user, negative=False):
        pass
