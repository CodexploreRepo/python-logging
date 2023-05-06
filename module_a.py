import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # need to set overal level


# create handler
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler("log/execution.log")

# Configure level and formatter and add it to handlers
console_handler.setLevel(level=logging.INFO)
file_handler.setLevel(level=logging.ERROR)

# formatter
formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("This is info")
logger.error("This is an error")
