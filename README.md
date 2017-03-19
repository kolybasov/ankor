# Ankor

![main](https://i.imgur.com/c9BWAHW.png)
![links](https://i.imgur.com/X7RbbjA.png)

## Requirements

* python 3
* pip 3
* sqlite 3

## Installation

* `$ git clone https://github.com/kolybasov/ankor && cd ankor`
* `$ make init`
* `$ [sudo] chmod +x ./run.py`

## Usage

* `$ ./run.py`
* Copy URL with length 30+ symbols and open url from config.
Default is [http://127.0.0.1:3333](http://127.0.0.1:3333)

## Tests

* `$ make test`

## Configuration

You can edit file config.yml.

Available options:

* host
* port
* db
* …

## License

MIT
