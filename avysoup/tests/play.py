import avysoup
import avysoup.http as h
from pathlib import Path
import sys

from avysoup.tests.record import _SESSION_JSON

if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else _SESSION_JSON
    avysoup.main(h.load_session(path))

