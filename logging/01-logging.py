import logging

# logging.basicConfig(level=logging.ERROR)

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debugging message")
logging.info("This is an info message")
logging.warning("This is an warning message")
logging.error("This is an error message")
logging.critical("This is an critical message")