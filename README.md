# ScrapyPrototype

* create venv python3.7 from IDE or CLI
  `> python3 -m venv venv`
  `> source venv/bin/activate`
* install dependency
  `> pip3 install -r requirements.txt`
* install dependency for dev only (optional)
  `> pip3 install -r requirements_dev.txt`
* unit test
  `> pytest`

* crawler
  `> scrapy crawl blogspider`

* run flask
  `> export FLASK_APP=server`
  `> flask run`

* Example mongoDB
```
MONGODB_SERVER = "mongodb+srv://admin:yjE6ATG1I0xMe619@cluster0.wsrjh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGODB_PORT = 27017
MONGODB_DB = "prototype"
MONGODB_COLLECTION = "articles"
```