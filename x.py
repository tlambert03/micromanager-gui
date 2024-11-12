from qtpy.QtWidgets import QApplication

from micromanager_gui._slackbot._slackbot_process import SlackBotProcess

app = QApplication([])
p = SlackBotProcess()
p.start()
app.exec()
