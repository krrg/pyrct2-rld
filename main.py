from __future__ import print_function
import sys

def main():
    if len(sys.argv) < 4:
        print("Usage:\n python3 main.py [TD6 input] [output]")
        sys.exit()

    td6_file = sys.argv[2]
    output_file = sys.argv[3]


class RunlengthDecoder(object):

    def decode(self, td6):
        # td6 is an array of bytes
        encoded, checksum = td6[:-4], td6[-4:]

        


if __name__ == "__main__":
    main()

    