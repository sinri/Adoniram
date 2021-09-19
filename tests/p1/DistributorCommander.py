from adoniram.SharedKit import adoniram_read_config, adoniram_load_config
from adoniram.config.config import adoniram_config_in_env
from adoniram.distributor.AdoniramDistributorCommander import AdoniramDistributorCommander

if __name__ == '__main__':
    adoniram_load_config(adoniram_config_in_env)
    AdoniramDistributorCommander(
        adoniram_read_config(('server', 'host')),
        adoniram_read_config(('server', 'port')),
        'ShutdownServer'
    ).listen()
