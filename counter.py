import os.path
import sys
import traceback

from domain.document import Document
from domain.errors import ConfigError
from interface.walker import Walker

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ConfigError(
                "Usage: py counter.py <target>\n\n"
                "Providing a directory will scan all files in it."
            )
        target = str(sys.argv[1])

        if os.path.isfile(target):  # single file
            print("Single file mode initiated for", target)
            docs = [Document(target)]
        else:  # all files under the path
            print("Multiple file mode initiated for path", target)
            walker = Walker(target)
            docs = walker.walk()
            print("Files found: ", len(docs))

        print("Scan completed, starting to process...")
        for doc in docs:
            # todo: Database retrieval for comparison
            words = doc.words
            print(doc.file + ":", str(words), "word" + ("" if words == 1 else "s"))

        # todo Actual saving to database
        print("Data saved")
        sys.exit(0)
    except ConfigError as e:
        print(str(e))
        sys.exit(1)
    except Exception as e:
        print(str(e))
        traceback.print_exc()  # todo Configurable error output?
        sys.exit(1)
