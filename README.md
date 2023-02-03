# Rathole Wrapper

A Python package for managing the Rathole application.

## Requirements

- Python 3.x
- Requests library
- Subprocess library
- Zipfile library

## Features

- Initialize: Downloads the Rathole executable automatically.
- Start: Launches the Rathole application with the specified configuration file.
- Stop: Terminates the running Rathole process.
- Restart: Restarts the Rathole process.

## Usage

The package provides the `RatholeService` class which has the following methods:

- `start()`: Starts the Rathole application with the specified configuration file.
- `stop()`: Terminates the running Rathole process.
- `restart()`: Restarts the Rathole process.

## Example

```python
from rathole_service import RatholeService

# Create a new RatholeService instance
service = RatholeService('path/to/config.toml')

# Start the Rathole application
service.start()

# Stop the running Rathole process
service.stop()

# Restart the Rathole process
service.restart()
```

## License
This project is licensed under the MIT License.