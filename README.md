# ScrapyPrototype

* create venv python3.7 from IDE or CLI
```
python3 -m venv venv
source venv/bin/activate
```
* install dependency
```
pip3 install -r requirements.txt
```
* unit test
```
pytest
```
* crawler
```
scrapy crawl blogspider
```
* run flask
```
export FLASK_APP=server
flask run
```
* Example mongoDB
```
MONGODB_SERVER = "mongodb+srv://admin:alreadychanged@cluster0.wsrjh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGODB_PORT = 27017
MONGODB_DB = "prototype"
MONGODB_COLLECTION = "articles"
```
* Demo
```
gcloud builds submit --tag gcr.io/{project_id}/scrapprototype
gcloud beta run deploy scrapprototype \
  --image gcr.io/{project_id}/scrapprototype\
  --platform managed \
  --region australia-southeast1 \
  --memory 1G \
  --cpu 2

https://scrapprototype-b4xnulhkbq-ts.a.run.app/?search=proxy%20network
```
