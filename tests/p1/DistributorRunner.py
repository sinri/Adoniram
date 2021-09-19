from adoniram.SharedKit import adoniram_distributor_init_shared_kit, adoniram_read_config, adoniram_load_config
from adoniram.config.config import adoniram_config_in_env
from adoniram.distributor.AdoniramDistributorServer import AdoniramDistributorServer

if __name__ == '__main__':
    adoniram_load_config(adoniram_config_in_env)
    adoniram_distributor_init_shared_kit()
    AdoniramDistributorServer(adoniram_read_config(('server', 'port'))) \
        .listen()
