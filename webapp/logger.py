from datetime import datetime

class Logger:
    def __init__(self, category, path=None):
        self.category = category
        self.path = path

    def log(self, level, message):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = "%s|%s|%s - %s" % (ts, self.category, level, message)
        print(log_line)

        if not self.path is None:
            with open(self.path, 'a') as file:
                file.write('%s\n' % log_line)

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)