from adoniram.SharedKit import adoniram_distributor_init_shared_kit, adoniram_read_config
from adoniram.distributor.AdoniramDistributorServer import AdoniramDistributorServer

if __name__ == '__main__':
    adoniram_distributor_init_shared_kit()
    AdoniramDistributorServer(adoniram_read_config(('server', 'port'))) \
        .listen()
