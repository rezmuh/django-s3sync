VERSION = (0, 1)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if len(VERSION) == 3:
        version = '%s.%s' % (version, VERSION[2])
    return version
