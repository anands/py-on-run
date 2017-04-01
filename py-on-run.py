import os, sys, subprocess, datetime, time, pty

class FileWatch(object):
    def __init__(self, filename):
    	self.filename = filename
        self._cached_stamp = os.stat(self.filename).st_mtime
        
    def isChanged(self):
        stamp = os.stat(self.filename).st_mtime
    	if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            return True
        else:
        	return False

fileWatch = FileWatch(sys.argv[1])
while True:
    try:
        if fileWatch.isChanged():
            print "File modified: " + str(datetime.datetime.now())
            (master, slave) = pty.openpty()
            process = subprocess.Popen(os.environ["SHELL"] + " -i -c '" + sys.argv[2] + "'",shell=True,executable=os.environ["SHELL"], stdin=slave, stdout=slave, stderr=slave)
            os.close(master)
            os.close(slave)
        time.sleep(1)
    except KeyboardInterrupt:
        break