import mongoengine as me

me.connect("Users", host="mongodb")


class User(me.Document):
    name = me.StringField(min_length=2, max_length=128)
    country = me.StringField(min_length=2, max_length=128)
    address = me.StringField(min_length=2, max_length=256)
    email_address = me.StringField(min_length=2, max_length=256)
