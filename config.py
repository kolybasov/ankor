import yaml
import io

from copy import deepcopy

config = yaml.safe_load(io.open('./config.yml', 'r'))


def get(path, default_val=None):
    """ Method to safely get a value from the config.
    Allows to use nested keys and provide default value. """

    keys = path.split('.')
    last_key_idx = len(keys) - 1
    value = deepcopy(config)

    for idx, key in enumerate(keys):
        value = value.get(key, default_val)

        if idx < last_key_idx and not isinstance(value, dict):
            value = default_val
            break

    return value
