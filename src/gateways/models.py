from middlewares import mongodb_middleware_weather


class insertWeatherData():
    def insert_data(mongoData):
        connection = mongodb_middleware_weather()
        connection.insert_one(mongoData)

class getWeatherData():
    def get_all_data():
        connection = mongodb_middleware_weather()
        documentList = []
        for document in connection.find():
            documentList.append(document)
        return documentList
    def get_last_item():
        connection = mongodb_middleware_weather()
        documentList = []
        for document in connection.find():
            documentList.append(document)
        return documentList[-1]