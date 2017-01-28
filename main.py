from __future__ import print_function
import sys
from collections import deque

# Also, see: https://github.com/OpenRCT2/OpenRCT2/blob/develop/src/openrct2/ride/track_design.h


def main():
    if len(sys.argv) < 3:
        print("Usage:\n python3 main.py [TD6 input] [output]")
        sys.exit()

    td6_file = sys.argv[1]
    output_file = sys.argv[2]

    for i, byte in enumerate(RunlengthDecoder().decode(bytearray(open(td6_file, 'rb').read()))):
        print("{}\t:{}".format(hex(i), byte))


class RunlengthDecoder(object):

    def decode(self, td6):
        # td6 is an array of bytes
        encoded, checksum = deque(td6[:-4]), td6[-4:]
        
        while len(encoded) > 0:
            next_byte = encoded.popleft()

            # Check the most-significant bit
            bit = (next_byte & 0b10000000)

            if bit == 0:
                # Then copy n + 1 bytes
                for i in range(0, next_byte + 1):
                    yield encoded.popleft()
            else:
                copy_length = 257 - next_byte
                copy_byte = encoded.popleft()

                for i in range(copy_length):
                    yield copy_byte

        
        
    

        


if __name__ == "__main__":
    main()

    