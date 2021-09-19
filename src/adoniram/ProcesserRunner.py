from nehushtan.helper.CommonHelper import CommonHelper

from adoniram.SharedKit import adoniram_read_config
from adoniram.processor.AdoniramProcesserClient import AdoniramProcesserClient

if __name__ == '__main__':
    AdoniramProcesserClient(
        adoniram_read_config(('server', 'host')),
        adoniram_read_config(('server', 'port')),
        CommonHelper.generate_random_uuid_hex()
    ).listen()
