from datetime import datetime
# https://docs.python.org/3/howto/logging.html

class Logger:
    nome = "Logger bello"

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

    # ERROR_LV = [DEBUG,INFO,WARNING,ERROR,CRITICAL]

    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, lv, msg):
        text = str(datetime.now()) + ": " + lv + " - " + msg + "\n"
        with open(self.file_name, "a") as file:
            file.write(text)
        print(text, end="")

    def error(self,msg):
        self.log("ERROR", msg)


logger = Logger("log.txt")
logger.log("INFO", "logger created")


try:
    raise Exception("Mio errore nuovo")
except Exception as error:
    logger.error(str(error))
