from datetime import datetime

class Logger:
    def __init__(self, category):
        self.category = category

    def log(self, level, message):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("%s|%s|%s - %s" % (ts, self.category, level, message))

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)