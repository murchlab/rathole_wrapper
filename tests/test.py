import os
from context import rathole_wrapper, test_dir
import time

config_path = os.path.join(test_dir, 'client.toml')
rs = rathole_wrapper.RatholeService(config_path)
rs.start()
time.sleep(5)
rs.stop()
