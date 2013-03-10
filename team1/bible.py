from compressor import encode_file, decode_file


encode_file('bible.txt', 'bible.small')
decode_file('bible.small', 'bible.big')

import os
print 'Same' if os.path.getsize('bible.txt') == os.path.getsize('bible.big') else 'Not Same'