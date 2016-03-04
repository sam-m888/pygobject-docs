===========
Development
===========

https://bugzilla.gnome.org/page.cgi?id=browse.html&product=pygobject

make check

make check SKIP_PEP8=1

make check TEST_NAMES=test_everything.TestEverything

git format-patch HEAD^

./autogen.sh --with-python=python2
./autogen.sh --with-python=ptyhon3

https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes

jhbuild build pygobject pygobject-python2
