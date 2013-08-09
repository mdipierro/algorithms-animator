import urllib
print 'Installing update...'
print 'dowloading replacement file csc321frames.pyc'
try:
    data=urllib.urlopen("http://www.phoenixcollective.org/mdp/CSC321/csc321frames.pyc"). read()
    file=open("csc321frames.pyc", "w").write(data)
    print 'DONE'
    print 'Version 1.1 of CSC321 will be posted soon but is not available yet.'
    print 'Please check again in few weeks\n\n'
    print 'Restart Program now'
except:
    print 'Download failure. TRY AGAIN!'


