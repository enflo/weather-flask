from flask import Blueprint, render_template
from gateways.models import getWeatherData


web = Blueprint("web", __name__, template_folder='templates')

@web.route("/", methods=['GET'])
def home():
    items = getWeatherData.get_last_item()
    cityName = items["city"]
    return render_template("index.html",
                            city=cityName[0],
                            temperature=items["temperature"],
                            humidity=items["humidity"],
                            pressure=items["pressure"])

#@web.route("/profile", methods=['GET'])
#def profile():
#    items = getWeatherData.get_last_item()
#    return render_template("profile.html",
#                            celcius=items["temperature"],
#                            humidity=items["humidity"],
#                            pressure=items["pressure"])


#@web.route("/about", methods=['GET'])
#def about():
#    return render_template("about.html")
