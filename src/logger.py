"""Logger"""
class Logger:
    """Different methods for logging"""
    @staticmethod
    def newline():
        """Print a new line"""
        print()

    @staticmethod
    def log(*args):
        """Normal logging method"""
        print("[#]", *args)

    @staticmethod
    def error(*args):
        """Log an error"""
        print("!", *args)