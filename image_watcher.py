author = "jdzollw"

import os
import time
import pickle
from messaging.Email import Email
import threading

class ImageWatcher(threading.Thread):
    """ Class that watches a directory for JPEG (.jpg) files and sends 
    found files via email, sms, or mms.
    """

    def __init__(self, messager_list=[]):
        self.messager_list = messager_list
        self._stopevent = threading.Event()
        threading.Thread.__init__(self, name='ImageWatcher')

    def run(self):
        """ Method that finds certain types of files in a directory.
        """
        
        while not self._stopevent.isSet():

            # Loop over dir and find files of given type
            for f in os.listdir(os.getcwd()):

                if f.endswith(".jpg"):
                    print f 
                    # Send file
                    for messager in self.messager_list:
                        try:
                            messager.send(f)
                        except:
                            continue

                    # Delete file
                    os.remove(f)

    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)

if __name__ == "__main__":
    info = pickle.load(open("../rpi_security_tests/messager_info.pickle", "rb"))
    messager_list = [Email(info[0], info[1], info[2][0], info[3])]

    watcher = ImageWatcher(messager_list=messager_list)
    watcher.start()
    time.sleep(4.0)
    watcher.join()
