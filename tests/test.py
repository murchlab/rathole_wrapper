import os
from context import rathole_wrapper, test_dir
import time

# Define the path to the client configuration file in TOML format
config_path = os.path.join(test_dir, 'client.toml')

# Create an instance of the RatholeService class and pass in the client configuration file path
rs = rathole_wrapper.RatholeService(config_path)

# Start the rathole instance with custom configurations
rs.start()

# Wait for 5 seconds to allow the rathole instance to start
time.sleep(5)

# Stop the rathole instance
rs.stop()