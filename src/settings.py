import os

eget = os.environ.get

setMongo = {
    "url": eget('MONGO_PATH','mongodb://localhost:27017/'),
    "dbname":"weather",
    "dbcolweather":"weather",
    "dbcolusers":"users"
}

swagger = {
    "url":"/api",
    "descriptorUrl":"/static/swagger.json"
}