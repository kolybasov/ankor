import config as cfg
import yaml
import io

config = yaml.safe_load(io.open('./config.yml', 'r'))


class TestConfig:
    def test_get(self):
        assert cfg.get('db') == config['db']
        assert cfg.get('db.name') == config['db']['name']
        assert cfg.get('db.name.none', 'default') == 'default'
