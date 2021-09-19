from adoniram.SharedKit import adoniram_read_config
from adoniram.distributor.AdoniramDistributorCommander import AdoniramDistributorCommander

if __name__ == '__main__':
    AdoniramDistributorCommander(
        adoniram_read_config(('server', 'host')),
        adoniram_read_config(('server', 'port')),
        'ShutdownServer'
    ).listen()
