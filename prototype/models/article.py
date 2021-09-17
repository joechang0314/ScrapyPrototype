from models import BaseModel

class Article(BaseModel):
    def __init__(self, raw_data):
        self.id = None
        self.title = None
        self.url = None
        self.__from_dict(raw_data)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
        }
    
    def __from_dict(self, raw_data):
        self.id = str(raw_data['_id'])
        self.title = raw_data['title']
        self.url = raw_data['url']