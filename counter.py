import sys
from interface.walker import Walker
from domain.errors import ConfigError

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ConfigError('Provide path as the first parameter.')
        path = str(sys.argv[1])
        print('Initiating scan of ' + path)
        walker = Walker(path)
        walker.walk()
        print('Scan completed, saving...')
        # todo: Database part
        print('Data saved')
    except Exception as e:
        print(str(e))
        exit()
