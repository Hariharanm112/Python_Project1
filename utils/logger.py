import os
import logging

def setup_logger():
    log_dir="log"
    os.makedirs("log",exist_ok=True)

    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()


    file_handler=logging.FileHandler(os.path.join(log_dir,"automation.log"))
    formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger