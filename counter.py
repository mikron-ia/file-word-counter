import sys
import traceback
from interface.walker import Walker
from domain.errors import ConfigError

from domain.document import Document

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ConfigError(
                "Usage:\n\nTo scan for all files in path: counter path\nTo scan a single file: counter path filename"
            )
        path = str(sys.argv[1])

        filename = None
        if len(sys.argv) > 2:
            filename = str(sys.argv[2])

        docs = []

        if filename:  # single file
            print("Single file mode initiated for", filename, "at", path)
            docs.append(Document(filename, path))
        else:  # all files under the path
            print("Multiple file mode initiated for path", path)
            walker = Walker(path)
            walker.walk()
            # todo: docs.append()
            print("Scan completed, starting to process...")

        for doc in docs:
            # todo: Database retrieval for comparison
            words = doc.words
            print(doc.name + ":", str(words), "word" + ("" if words == 1 else "s"))

        # todo Actual saving to database
        print("Data saved")
    except ConfigError as e:
        print(str(e))
        exit(1)
    except Exception as e:
        print(str(e))
        traceback.print_exc()  # todo Configurable error output?
        exit(1)
