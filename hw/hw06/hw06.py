
passphrase = '*** PASSPHRASE HERE ***'


def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '9c557774afa3f7b5670f10a5ca54be0eedb8384a780375daa0340b45'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()