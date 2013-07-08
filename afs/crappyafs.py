#/usr/bin/env python

import os
import subprocess

def abspath2(path):
    '''like os.path.abspath(), but handles both rel and abs input paths'''
    return os.path.normpath(path if os.path.isabs(path)
            else os.path.join(os.getcwd(), path))

class ACL(object):
    class BadACL(RuntimeError):
        pass

    class BadDir(RuntimeError):
        pass

    def __init__(self, pos, neg):
        '''
        {pos,neg}: dict of {pos,neg} permissions: name: AFS-letters
        '''
        self._pos = {}
        self._neg = {}

        for perms in (pos, neg):
            for name, perm in perms.iteritems():
                self.set(name, perm, perms is neg)

    _canonical = {
        'read': 'rl',
        'write': 'rlidwk',
        'all': 'rlidwka',
        'mail': 'lik',
        'none': '',
    }

    _perms = 'rliwdkaABCDEFGH'

    @staticmethod
    def retrieve(dir, follow=True):
        '''retrive acl for AFS directory; returns new ACL'''
        absdir = abspath2(dir)
        if not os.path.isdir(absdir):
            raise self.BadDir('Invalid directory: %s' % absdir)


    def apply(self, dir, follow=True):
        '''applies this ACL to the given dir'''
        absdir = abspath2(dir)

        #TODO the hard part
        #p = subprocess.Popen(['fs', 'sa'

    def _clean(self):
        '''remove entries w/ neutral ACLs'''
        for acl_type in (self._pos, self._neg):
            for name, rights in acl_type.items():
                if rights == '':
                    acl_type.pop(name, None)

    def set(self, user, rights, negative=False):
        '''sets pos/neg rights for user'''
        r = set(rights)
        if not r.issubset(self._perms):
            raise self.BadACL('Invalid permissions: %s' % rights)
        pass
        r_string = ''.join(r)
        acl_type = self._neg if negative else self._pos
        acl_type[user] = r_string

    def remove(self, user, negative=False):
        '''remove the ACLs for this user'''
        self._pos.pop(user, None)
        self._neg.pop(user, None)
