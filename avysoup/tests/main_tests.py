import avysoup
from avysoup import http
from avysoup.tests.record import _SESSION_JSON

def test_main():
    assert 0 == avysoup.main(http.load_session(_SESSION_JSON))