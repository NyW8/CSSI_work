#import appengine's datastore
from google.appengine.ext import ndb

class Movie(ndb.Model):

    title = ndb.StringProperty(required = True)
    media_type = ndb.StringProperty(required = True, default = 'Movie')
    runtime = ndb.IntegerProperty(required = False)
    user_rating = ndb.FloatProperty(required = False)
    director = ndb.StringProperty(required = False)

    def __init__(self, mov_title, runtime, user_rating, director):
        self.title = mov_title
        self.runtime = runtime
        self.rating = user_rating
        self.director = director

class Users(ndb.Model):

    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = True)
    username = ndb.StringProperty(required = True)
    bitmoji = ndb.BooleanProperty(required = True, default = False)
    location = ndb.GeoPtProperty(required = False)
    pickle = ndb.PickleProperty(required = False)
    phone= ndb.IntegerProperty(required = False)
    #friends = ndb.StructuredProperty(Friends, repeated = True)
    #subscriptions = ndb.StructuredProperty(Subscriptions, repeated = True)

class Subscriptions(ndb.Model):
    channel = ndb.IntegerProperty(required = True)
    author = ndb.StringProperty(required = False)
    article = ndb.StringProperty(required = True)
    read = ndb.BooleanProperty(required = True, default = False)

class Stories(ndb.Model):
    time = ndb.DateTimeProperty(required = True)
    location = ndb.GeoPtProperty(required = False)
    duration = ndb.IntegerProperty(required = True)

    def __init__(self, time, location, duration):
        self.time = time
        self.location= location
        self.duration = duration

class Bitmoji(ndb.Model):
    bitmoji = ndb.BooleanProperty(required = True, default = False)
    def __init__(self, bitmojiTrue):
        self.bitmoji = bitmojiTrue

class Friends(ndb.Model):
    user1 = ndb.StructuredProperty(Users, repeated = True)
    user2 = ndb.StructuredProperty(Users, repeated = True)

    def __init__(self, user1, user2):
        if user1 > user2:
            self.user1 = user1
            self.user2 = user2
        else:
            self.user1 = user2
            self.user2 = user1
