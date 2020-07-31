# for each granularity
# for each lock type
# for each lock placement
# generate configuration for locker

import os
import granularity

dirname = os.path.dirname(__file__)


filename = os.path.join(dirname, 'auction', 'token.json')
print(granularity.get_coarsenings(filename))

