from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from uuid import uuid1
from win_tkinter import win_tk, win_tk_java
from download_mod import download, tags_stonelauncher, createFolder, download_dir, download_resourcepacks, record_login_version, download_java_8, add_server_ip
import minecraft_launcher_lib
import subprocess
import os
import time
import pylnk3

download_dir()

minecraft_directory = r"C:\.stoneworld\SWMinecraft"

class LaunchTread(QtCore.QThread):
    launch_setup_signal = QtCore.pyqtSignal(str, str)
    progress_update_signal = QtCore.pyqtSignal(int, int, str)
    state_update_signal = QtCore.pyqtSignal(bool)
    
    version_id = ""
    username = ""
    
    progress = 0
    progress_max = 0
    progress_label = ""
    
    def __init__(self):
        super().__init__()
        self.launch_setup_signal.connect(self.launch_setup)

    def launch_setup(self, version_id, username):
        self.version_id = version_id
        self.username = username
        
    def update_progress_label(self, value):
        self.progress_label = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)
        
    def update_progress(self, value):
        self.progress = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)
        
    def update_progress_max(self, value):
        self.progress_max = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def create_shortcut(path, target, description):
        link = pylnk3.PyLnk()
        link.create(path)
        link.path = target
        link.description = description
        link.write()
    
    def run(self):
        
        CREATE_NO_WINDOW = 0x08000000
        
        self.state_update_signal.emit(True)
        if self.version_id == "Forge 1.7.10":
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\versions\1.7.10"):
                minecraft_launcher_lib.install.install_minecraft_version(versionid="1.7.10", minecraft_directory=minecraft_directory, callback= {"setStatus": self.update_progress_label, "setProgress": self.update_progress, "setMax": self.update_progress_max})
            time.sleep(5)
            
            download(self.version_id)
            
            minecraft_launcher_lib.install.install_minecraft_version(versionid="1.7.10-Forge10.13.4.1614-1.7.10", minecraft_directory=minecraft_directory, callback= {"setStatus": self.update_progress_label, "setProgress": self.update_progress, "setMax": self.update_progress_max})
        
        elif self.version_id == "Forge 1.12.2":
            if not os.path.exists(r"C:\.stoneworld\SWMinecraft\versions\1.12.2"):
                minecraft_launcher_lib.install.install_minecraft_version(versionid="1.12.2", minecraft_directory=minecraft_directory, callback= {"setStatus": self.update_progress_label, "setProgress": self.update_progress, "setMax": self.update_progress_max})
            
            time.sleep(5)
            
            download(self.version_id)
            
            minecraft_launcher_lib.install.install_minecraft_version(versionid="1.12.2-forge-14.23.5.2859", minecraft_directory=minecraft_directory, callback= {"setStatus": self.update_progress_label, "setProgress": self.update_progress, "setMax": self.update_progress_max})
                    
        else:
            minecraft_launcher_lib.install.install_minecraft_version(versionid=self.version_id, minecraft_directory=minecraft_directory, callback= {"setStatus": self.update_progress_label, "setProgress": self.update_progress, "setMax": self.update_progress_max})
        
        if self.username == "":
            self.username = "None"
        options = {
            'username': self.username,
            'uuid': str(uuid1),
            'token': ''
        }
        
        record_login_version(self.version_id, self.username)
        
        #Внутри папки SWMinecraft --------------------------------------------------------
        
        download_resourcepacks(self.version_id)
        
        add_server_ip()
                
        #---------------------------------------------------------------------------------------

        if self.version_id == "Forge 1.7.10":
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version="1.7.10-Forge10.13.4.1614-1.7.10", minecraft_directory=minecraft_directory, options=options), creationflags=CREATE_NO_WINDOW)
        
        elif self.version_id == "Forge 1.12.2":
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version="1.12.2-forge-14.23.5.2859", minecraft_directory=minecraft_directory, options=options), creationflags=CREATE_NO_WINDOW)
        
        else:
            subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=self.version_id, minecraft_directory=minecraft_directory, options=options), creationflags=CREATE_NO_WINDOW)
        self.state_update_signal.emit(False)
        
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-670, -270, 1641, 891))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\.stoneworld\pictures\fon.jpg"))
        self.label.setObjectName("label")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(90, 370, 221, 41))
        self.play.setObjectName("play")
        self.play.clicked.connect(self.launch_game)
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(140, 430, 111, 41))
        self.settings.setObjectName("settings")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(60, 170, 291, 41))
        self.login.setObjectName("login")
        try:
            with open(file=r"C:\.stoneworld\datalogandver\login\login_data.txt", mode= "r") as file_login:
                self.login.setText(file_login.readline())
                file_login.close()
        except:
            print(SystemError, "при добавление логина")
        self.versions = QtWidgets.QComboBox(self.centralwidget)
        self.versions.setGeometry(QtCore.QRect(60, 270, 291, 41))
        self.versions.setObjectName("versions")
        minecraft_version = ["1.7.10", "1.8", "1.8.2", "1.8.9", "1.9", "1.9.2", "1.10", "1.10.2", "1.11", "1.11.2", "1.12", "1.12.2", "1.13", "1.13.2", "1.14", "1.14.2", "1.15", "1.15.2", "1.16", "1.16.2", "1.17", "1.17.1", "1.18", "1.18.2", "1.19", "1.19.2", "1.20", "1.20.2"]
        try:
            with open(file=r"C:\.stoneworld\datalogandver\login\version_data.txt", mode= "r") as file_version:
                self.versions.addItem(file_version.readline())
                file_version.close()
        except:
            print(SystemError, "при добавление версии")
        for version in minecraft_launcher_lib.utils.get_version_list():
            for i in minecraft_version:
                if (version['id'] == i):
                    self.versions.addItem(version['id'])
        self.versions.addItem("Forge 1.7.10")
        self.versions.addItem("Forge 1.12.2")
        self.name_sw = QtWidgets.QLabel(self.centralwidget)
        self.name_sw.setGeometry(QtCore.QRect(10, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Ostrovsky")
        font.setPointSize(38)
        self.name_sw.setFont(font)
        self.name_sw.setObjectName("name_sw")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(60, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_login.setObjectName("label_login")
        self.label_versions = QtWidgets.QLabel(self.centralwidget)
        self.label_versions.setGeometry(QtCore.QRect(60, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_versions.setFont(font)
        self.label_versions.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_versions.setObjectName("label_versions")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 340, 269, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.launch_tread= LaunchTread()
        self.launch_tread.state_update_signal.connect(self.state_update)
        self.launch_tread.progress_update_signal.connect(self.update_progress)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StoneWorldLauncher"))
        MainWindow.setWindowIcon(QtGui.QIcon(r"C:\.stoneworld\pictures\icon.jpg"))
        self.play.setText(_translate("MainWindow", "Играть"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.name_sw.setText(_translate("MainWindow", "Stone World"))
        self.label_login.setText(_translate("MainWindow", "Логин:"))
        self.label_versions.setText(_translate("MainWindow", "Версия:"))
    
    def update_progress(self, progress, max_progress, label):
        self.progressBar.setValue(progress)
        self.progressBar.setMaximum(max_progress)
    
    def state_update(self, value):
        self.play.setDisabled(value)
        self.progressBar.setVisible(value)
    def launch_game(self):
        self.launch_tread.launch_setup_signal.emit(self.versions.currentText(), self.login.text())
        self.launch_tread.start()

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.setFixedSize(430, 550)
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    if tags_stonelauncher():
        print("Да")
        time.sleep(1)
        win_tk()
        sys.exit()

    if download_java_8():
        print("Да java")
        time.sleep(1)
        win_tk_java()
        sys.exit()
        
    sys.exit(app.exec_())
