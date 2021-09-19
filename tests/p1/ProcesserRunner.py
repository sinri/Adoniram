from nehushtan.helper.CommonHelper import CommonHelper

from adoniram.SharedKit import adoniram_read_config, adoniram_load_config
from adoniram.config.config import adoniram_config_in_env
from p1.AdoniramProcesserClientForP1 import AdoniramProcesserClientForP1

if __name__ == '__main__':
    adoniram_load_config(adoniram_config_in_env)
    AdoniramProcesserClientForP1(
        adoniram_read_config(('server', 'host')),
        adoniram_read_config(('server', 'port')),
        CommonHelper.generate_random_uuid_hex()
    ).listen()
