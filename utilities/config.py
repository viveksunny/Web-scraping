import configparser
import os

configs = configparser.ConfigParser()
config_path = r'utilities\configurations\configurations.cfg'
config_path = os.path.join(os.getcwd(), config_path)


class ScanConfigurations:
    def __init__(self, main_config, sub_config):
        configs.read(config_path)
        self.main_config = main_config
        self.sub_config = sub_config

    def getvalue(self):
        return configs.get(self.main_config, self.sub_config)