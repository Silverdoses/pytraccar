# PyTraccar

[![Build Status][travis-image]][travis-url]



## Overview

Python interface to interact with Traccar REST API.

## Installation
Tested with Python 2.7, Python 3.4, Python 3.5, Python 3.6 and Python 3.7  

Installation from source (requires git):
```sh
$ git clone 
$ cd pytraccar
$ python setup.py install
```

## Usage example

_For more info, please refer to the [Traccar API Reference][traccar-api-reference]._

## Development setup
For testing purpouses, check these variables in file test_api_calls.py and set them with your traccar server values.  

Your Traccar's server URL (default: localhost)
```
test_url = 'http://127.0.0.1:8082'
```
  
Email and password from a standard user or admin. (default: admin)

```python
username, correct_password = 'admin', 'admin'
```
  
Standard user token. Needed for all tests with limited user permissions.
```
user_token = 'YOUR_TOKEN_HERE'
```
  
Admin user token. Needed for all tests with admin permissions
```
admin_token = 'YOUR_TOKEN_HERE'
```
  
Then, run pytest to start testing.
```sh
python -m pytest
```

## Release History

* 0.0.1
    * Work in progress

## Contributing

1. Fork it (<https://github.com/Legacier/pytraccar/fork>)
2. Create your feature branch (`git checkout -b feature/yourbranch`)
3. Commit your changes (`git commit -am 'info here'`)
4. Push to the branch (`git push origin feature/yourbranch`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[travis-image]: https://travis-ci.com/Legacier/pytraccar.svg?branch=master
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
[traccar-api-reference]: https://www.traccar.org/api-reference/

## License Information

**PyTraccar is built on top of code developed from/by:**
  * Anton Tananaev, https://github.com/tananaev
  * Traccar, https://github.com/traccar/traccar

Released under the GPLv3 License