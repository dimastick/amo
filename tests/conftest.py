import pytest
import yaml


@pytest.fixture(scope='session')
def conf():

    with open('../.script_config/config.yaml') as config_file:
        conf = yaml.load(config_file)
    return conf
