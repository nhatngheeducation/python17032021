import logging
from datetime import datetime

logging.getLogger("NHATNGHE")

# Setup level xuất hiện log
logging.basicConfig(
    level=logging.INFO,
    filename='applog_{:%Y_%m_%d}.log'.format(datetime.now()),
    filemode="a", # a: append, w: write
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s :line %(lineno)s : %(message)s'
)

logging.debug(f"Time: {datetime.now()}")
logging.info(f"START LOGGING")
logging.warning(f"Time: {datetime.now()}")
logging.error(f"Time: {datetime.now()}")
logging.critical(f"Time: {datetime.now()}")