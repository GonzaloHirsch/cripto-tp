# Lib imports
import sys
# Local imports
from config import Config
from bmpStructure import BMPStructure

# Parses CLI options
def parse_cli():
    action = sys.argv[1]
    secret_image = sys.argv[2]
    k = sys.argv[3]
    directory = sys.argv[4]
    return Config(action, secret_image, k, directory)

def main():
    # Parse program arguments and get config object
    config = parse_cli()

    # Parsing the BMP image
    bmpStructure = BMPStructure(config.secret_image)
    print(bmpStructure)
    # print(bmpStructure.mapPixelArrayIntoBlocks())
    bmpStructure.writeNewImage(config.directory, 'eggs.bmp')

# Program entrypoint
if __name__ == "__main__":
   main()
