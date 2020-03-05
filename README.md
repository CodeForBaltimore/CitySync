![Code for Baltimore](/docs/img/CfB.png)

## Documentation

## Setup
To run this locally the following software is required:
*  [Python](https://www.python.org/) (version minimum 3.6)
*  [Flask](https://palletsprojects.com/p/flask/)
*  [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io)
*  [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
*  [Docker](https://docker.com) (*for optional container image usage*)

### Local Server
To run this application on your local machine you first need to install dependencies.  From the project root, run the following command:
```shell
pip install -r requirements.txt
```
(*note* in some environments you may need to run `pip3` instead of `pip` if you're running both Python 2.6 and 3.x.)

Once that completes you can run the application by running the following from the project root:
```shell
python server.py
```
(*note* in some environments you may need to run `python3` instead of `python` if you're running both Python 2.6 adn 3.x.)

#### Docker
Alternatively if you wish to run this in Docker instead of on your local you may do so using the included `Dockerfile`. To use the Docker simply run the following commands:
```shell
docker build -t citysync-dockerimg:latest .
docker run -d -p 5000:5000 citysync-dockerimg:latest
```
To stop the container run:
```shell
docker ps
```
Take note of the `CONTAINER ID` then run:
```shell
docker stop <container id>
```
You may then make changes to the code and re-run the initial `build` and `run` commands. 

## Using this product
Once setup and running (via Docker or locally) you can see the output by making queries to http://localhost:5000

Example: API request for general nonprofit data using curl.
```shell
curl -X GET http://localhost:5000/api/orgs/id/1

{ 
  "id": 1,
  "ein": 10591773,
  "name": "CONGREGATION YALKUT HA URIM INC",
  "ico": "% RABBI ISRAEL JAKOBOVITZ",
  "street": "6214 BENHURST RD",
  "raw_street": "",
  "city": "BALTIMORE",
  "state": "MD",
  "zipcode": "21209-3807",
  "latitude": 39.366293,
  "longitude": -76.690235,
  "geo_accuracy": 1.0,
  "group": 0,
  "subsection": 3,
  "affiliation": 3,
  "classification": 7000,
  "ruling": 200212,
  "deductability": 1,
  "foundation": 10,
  "activity": 0,
  "organization": 1,
  "status": 1,
  "tax_period": "",
  "asset_cd": 0,
  "income_cd": 0,
  "filing_req_cd": 6,
  "pf_filing_req_cd": 0,
  "acct_pd": 12,
  "asset_amt": 0,
  "income_amt": 0,
  "revenue_amt": 0,
  "ntee": "X30",
  "sort_name": "",
  "activity_full": ""
}

```

Example: API Request for Nonprofit organization address using curl.
```shell
curl -X GET http://localhost:5000/api/orgs/id/1/address

{
  "id": 1, 
  "ein": 10591773, 
  "name": "CONGREGATION YALKUT HA URIM INC", 
  "street": "6214 BENHURST RD", 
  "city": "BALTIMORE", 
  "state": "MD", 
  "zipcode": "21209-3807"
}
```

Example: API Request for Nonprofit geocoordinate location using curl.
```shell
curl -X GET http://localhost:5000/api/orgs/id/1/geocode

{
  "id": 1, 
  "ein": 10591773, 
  "name": "CONGREGATION YALKUT HA URIM INC", 
  "longitude": -76.690235, 
  "latitude": 39.366293, 
}
```

## Testing

## Sources and Links
