import os

mongurl = os.environ.get('mongodb://51.158.125.197:27017/', 'mongodb://mongo:27017/')

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