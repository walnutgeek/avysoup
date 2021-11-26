from typing import Dict, Union
import requests
from pathlib import Path
import json

urljoin = requests.compat.urljoin # type:ignore

class Requester:
    def __getitem__(self, url:str) -> str :
        return requests.get(url).text


class SessionRecorder:
    def __init__(self, file:Union[str,Path]) -> None:
        self.delegate = Requester()
        self.state:Dict[str, str] = {}
        self.file = Path(file)

    def __getitem__(self, url:str) -> str:
        if url in self.state:
            return self.state[url]
        text = self.delegate[url]
        self.state[url] = text
        self.file.write_text(json.dumps(self.state))
        return text


def load_session(file:Union[str,Path])->Dict[str, str]:
    return json.loads(Path(file).read_text())
