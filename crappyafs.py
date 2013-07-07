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
        '''retrive acl for AFS directory; returns new ACL'''
        pass

    def apply(self, dir, follow=True):
        '''applies this ACL to the given dir'''
        pass

    def _clean(self):
        '''remove entries w/ neutral ACLs'''
        pass

    def set(self, user, rights, negative=False):
        '''sets pos/neg rights for user'''
        pass

    def remove(self, user, negative=False):
        '''remove the ACLs for this user'''
        pass
