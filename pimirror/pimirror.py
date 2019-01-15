import os
import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from widget_data import clock_data, internet_data, news_data, weather_data
from widgets import Ui_clock_widget, Ui_internet_widget, Ui_mirror, Ui_news_widget, Ui_weather_widget

APP = QtWidgets.QApplication([])

WINDOW = QtWidgets.QMainWindow()
MIRROR = Ui_mirror.Ui_MainWindow()
MIRROR.setupUi(WINDOW)

class SmartMirror():

    def __init__(self, parent):
        self.parent = parent

    def setup_clock(self):
        self.clockthread = QtCore.QThread()
        self.datethread = QtCore.QThread()

        self.clock_update = clock_data.Clock(timeformat="12")
        self.date_update = clock_data.Date()
        self.clock_update.current_time.connect(self.update_time)
        self.date_update.current_date.connect(self.update_date)
        self.clockthread.started.connect(self.clock_update.update_time)
        self.clock_update.moveToThread(self.clockthread)
        self.datethread.started.connect(self.date_update.update_date)
        self.date_update.moveToThread(self.datethread)

        self.clock_widget = QtWidgets.QWidget(self.parent)
        self.clock = Ui_clock_widget.Ui_clock_widget()
        self.clock.setupUi(self.clock_widget)

    def update_time(self, text: str):
        time_str = text[:5]
        ampm_str = text[5:].lower()
        self.clock.label_time.setText("<html><head/><body><p><span style=\" font-size:32pt;\">%s</span><span style=\" font-size:22pt;\">%s</span></p></body></html>" % (time_str, ampm_str))

    def update_date(self, date: list):
        self.clock.label_date.setText("<html><head/><body><p><span style=\" font-size:14pt;\">%s %s</span><span style=\" font-size:14pt; vertical-align:super;\">%s</span><span style=\" font-size:14pt;\">, %s, %s</span></p></body></html>)" % (date[0], date[1], date[-1], date[2], date[3]))

    def setup_weather(self):
        self.weatherthread = QtCore.QThread()

        self.weather_update = weather_data.Forecast(unit="c", location="London")
        self.weather_update.current_lookup.connect(self.update_weather)
        self.weatherthread.started.connect(self.weather_update.update_forecast)
        self.weather_update.moveToThread(self.weatherthread)

        self.weather_widget = QtWidgets.QWidget(self.parent)
        self.weatherui = Ui_weather_widget.Ui_weather_widget()
        self.weatherui.setupUi(self.weather_widget)

        self.weather_widget.move(0, 110)

    def update_weather(self, weather):
        self.weatherui.label_city.setText("<html><head/><body><p><span style=\" font-size:14pt;\">%s</span></p></body></html>" % weather.location.city)
        self.weatherui.label_weatherstatus.setText("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">%s</span></p></body></html>" % weather.condition.text)
        self.weatherui.label_currenttemp.setText("<html><head/><body><p><span style=\" font-size:36pt;\">%s°</span></p></body></html>" % weather.condition.temp)
        self.weatherui.label_currenthi.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Hi %s°</span></p></body></html>" % weather.forecast[0].high)
        self.weatherui.label_currentlo.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Lo %s°</span></p></body></html>" % weather.forecast[0].low)
        self.weatherui.label_humidity.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Humidity: %s%%</span></p></body></html>" % weather.atmosphere.humidity)
        self.weatherui.label_wind.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Wind: %s %s</span></p></body></html>" % (weather.wind.speed, weather.units.speed))
        self.weatherui.label_forecastday_1.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[1].day)
        self.weatherui.label_forecastday_2.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[2].day)
        self.weatherui.label_forecastday_3.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[3].day)
        self.weatherui.label_forecastday_4.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[4].day)
        self.weatherui.label_forecastday_5.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[5].day)
        self.weatherui.label_forecastday_6.setText("<html><head/><body><p><span style=\" font-size:9pt;\">%s</span></p></body></html>" % weather.forecast[6].day)
        self.weatherui.label_forecasthi_1.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[1].high)
        self.weatherui.label_forecasthi_2.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[2].high)
        self.weatherui.label_forecasthi_3.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[3].high)
        self.weatherui.label_forecasthi_4.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[4].high)
        self.weatherui.label_forecasthi_5.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[5].high)
        self.weatherui.label_forecasthi_6.setText("<html><head/><body><p><span style=\" font-size:9pt;\">H %s°</span></p></body></html>" % weather.forecast[6].high)
        self.weatherui.label_forecastlo_1.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[1].low)
        self.weatherui.label_forecastlo_2.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[2].low)
        self.weatherui.label_forecastlo_3.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[3].low)
        self.weatherui.label_forecastlo_4.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[4].low)
        self.weatherui.label_forecastlo_5.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[5].low)
        self.weatherui.label_forecastlo_6.setText("<html><head/><body><p><span style=\" font-size:9pt;\">L %s°</span></p></body></html>" % weather.forecast[6].low)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.weatherui.label_currentweathericon.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.condition.code+".png")))
        self.weatherui.label_forecasticon_1.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[1].code+".png")))
        self.weatherui.label_forecasticon_2.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[2].code+".png")))
        self.weatherui.label_forecasticon_3.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[3].code+".png")))
        self.weatherui.label_forecasticon_4.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[4].code+".png")))
        self.weatherui.label_forecasticon_5.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[5].code+".png")))
        self.weatherui.label_forecasticon_6.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "weather", weather.forecast[6].code+".png")))

    def setup_internet(self):
        self.internetthread = QtCore.QThread()

        self.internet_update = internet_data.Connection()
        self.internet_update.connection_signal.connect(self.update_internet)
        self.internetthread.started.connect(self.internet_update.check_connection)
        self.internet_update.moveToThread(self.internetthread)

        self.internet_widget = QtWidgets.QWidget(self.parent)
        self.internetui = Ui_internet_widget.Ui_internet_widget()
        self.internetui.setupUi(self.internet_widget)

        self.internet_widget.move(640, 0)

    def update_internet(self, status: bool):#
        current_dir = os.path.dirname(os.path.realpath(__file__))
        if status:
            self.internetui.label_status.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Connected</span></p></body></html>")
            self.internetui.label_statusicon.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "check", "yes.png")))
        else:
            self.internetui.label_status.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Disconnected</span></p></body></html>")
            self.internetui.label_statusicon.setPixmap(QtGui.QPixmap(os.path.join(current_dir, "resources", "icons", "check", "no.png")))

    def setup_news(self):
        self.newsthread = QtCore.QThread()

        self.news_update = news_data.News()
        self.news_update.current_headlines.connect(self.update_news)
        self.newsthread.started.connect(self.news_update.update_headlines)
        self.news_update.moveToThread(self.newsthread)

        self.news_widget = QtWidgets.QWidget(self.parent)
        self.newsui = Ui_news_widget.Ui_news_widget()
        self.newsui.setupUi(self.news_widget)

        self.news_widget.move(320, 0)

    def update_news(self, content):
        print(len(content))
        self.newsui.label_articletitle_1.setText("<html><head/><body><p><span style=\" font-size:14pt;\">%s</span></p></body></html>" % content[0]["title"])
        self.newsui.label_articletitle_2.setText("<html><head/><body><p><span style=\" font-size:14pt;\">%s</span></p></body></html>" % content[1]["title"])
        self.newsui.label_articletitle_3.setText("<html><head/><body><p><span style=\" font-size:14pt;\">%s</span></p></body></html>" % content[2]["title"])
        self.newsui.label_articlebody_1.setText(content[0]["content"])
        self.newsui.label_articlebody_2.setText(content[1]["content"])
        self.newsui.label_articlebody_3.setText(content[2]["content"])


SM = SmartMirror(WINDOW)
SM.setup_clock()
SM.setup_weather()
#SM.setup_internet()
SM.setup_news()

WINDOW.showFullScreen()

SM.clockthread.start()
SM.datethread.start()
SM.weatherthread.start()
#SM.internetthread.start()
SM.newsthread.start()

if __name__ == "__main__":
    sys.exit(APP.exec_())
