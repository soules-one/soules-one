import time
import os
def get_time():
        return time.strftime("%X", time.gmtime(time.time()))
def get_date():
        date = time.strftime("%x", time.gmtime(time.time())).split("/")
        return "_".join(date)
    
class work_status:
    def __init__(self):
        self.work_start_time = get_time()
        self.update_time = None
        self.state = None
        self.info = None
    def __str__(self):
        return "Work status - {0}. \n Status info - {1}".format(self.state, self.info)
    def update(self, state, info):
        self.state = state
        self.info = info
        self.update_time = get_time()

class logger:
    def __init__(self):
        self.name = "log_{0}.txt".format(get_date())
        if "log" not in os.listdir():
            os.mkdir(os.getcwd()+"/log")
        if self.name in os.listdir(os.getcwd()+"/log"):
            self.write_mode = "a"
        else:
            self.write_mode = "w"
        

