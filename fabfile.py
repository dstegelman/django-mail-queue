from fabric.api import local

__author__ = 'derek'


def deploy(version):
    local('python runtests.py')
    local("git tag -a %s -m %s" % (version, version))
    local('python setup.py sdist upload')