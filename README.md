# avysoup

Parse locations of avalanches from sierraavalanchecenter.org

## Dev setup

Initial setup

    conda create -n avysoup python=3.8
    . activate avysoup
    pip install -e .[dev]

Run tests

    pytest

Run and record all http resposes in session.json

    python -m avysoup.tests.record

When all necessary http traffic captured replay it without touching web

    python -m avysoup.tests.play


## Run

    $ avysoup > incidents.json
    https://www.sierraavalanchecenter.org/observation/2021/feb/14/1000/incline-peak has no geo?
    https://www.sierraavalanchecenter.org/observation/2021/feb/12/1330/somewhere-near-blue-lakes has no geo?
    https://www.sierraavalanchecenter.org/observation/2021/feb/12/0945/flagpole-peak has no geo?
    $ head incidents.json
    [
    {
        "date": "03/21/2021 - 11:00",
        "url": "https://www.sierraavalanchecenter.org/observation/2021/mar/21/1100/upper-flume-creek-sierra-buttes",
        "geo": {
        "lat": 39.587521,
        "long": -120.633384
        }
    },
    {
    $    
