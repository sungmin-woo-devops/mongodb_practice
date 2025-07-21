from mongoengine import Document, StringField

class User(Document):
    email = StringField(required=True, unique=True, primary_key=True)
    name = StringField(max_length=50)

