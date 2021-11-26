import avysoup
import avysoup.http as h
from pathlib import Path
import sys

_SESSION_JSON = Path(__file__).parent / "session.json"

if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else _SESSION_JSON
    avysoup.main(h.SessionRecorder(path))
