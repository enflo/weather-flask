import os

mongurl = os.environ.get(mongodbURL, 'mongodb://mongo:27017/')

setMongo = {
    "url": mongurl,
    "dbname":"weather",
    "dbcolweather":"weather",
    "dbcolusers":"users"
}

swagger = {
    "url":"/api",
    "descriptorUrl":"/static/swagger.json"
}