import requests
import json
import pickle
import pyperclip
import time
import os
from config import config

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtGui import QPixmap
from Ui_MainWindow import Ui_MainWindow


class Client(QMainWindow):
    """获取token"""
    def __init__(self):
        super(Client, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.url = config.get('url', None)
        self.upload_url = config.get('upload_url', None)
        self.username = config.get('username', None)
        self.password = config.get('password', None)
        self.headers = {'Content-Type': 'application/json'}
        self.payload = {'username': self.username, 'password': self.password}
        self.pkiFile = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'token.pki')
        self.file_to_upload = ""

        # signal slot binding
        self.ui.btnUpload.clicked.connect(self.upload)
        self.ui.btnSelect.clicked.connect(self.select_file)
        self.ui.btnCopy.clicked.connect(self.copy_to_clipboard)

    def plot(self, filename):
        image = QPixmap()
        image.load(filename)
        item = QGraphicsPixmapItem(image)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.ui.graphicsView.setScene(scene)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select file", "./", "Picture(*.png *.jpg *.jpeg *.gif)")
        print(file)
        if file is not None:
            self.ui.pteFilename.setPlainText(file)
            self.file_to_upload = file
        print(self.file_to_upload)
        self.plot(file)

    def get_token(self):
        # 获取token
        token = {}
        r = requests.post(self.url, headers=self.headers, data=json.dumps(self.payload))
        t = r.text
        timestamp = int(time.time())
        token.setdefault('token', t)
        token.setdefault('timestamp', timestamp)
        with open(self.pkiFile, 'wb') as f:
            pickle.dump(token, f)

    def show_token(self):
        # 从文件获取token
        with open(self.pkiFile, 'rb') as f:
            t = pickle.load(f)
            return t.get('token')

    def is_token_expired(self):
        # 验证是否过期
        if not os.path.exists(self.pkiFile):
            self.get_token()
        with open(self.pkiFile, 'rb') as f:
            token = pickle.load(f)
        if int(time.time()) - token.get('timestamp') > 600:
            return True
        else:
            return False

    def upload(self):
        # 从剪切板获取图片上传
        upload_url = self.url + self.upload_url
        print(upload_url)
        if self.is_token_expired():
            self.get_token()
        token = self.show_token()
        h1 = {'token': token}
        # filename 检查 是否存在
        if os.path.exists(self.file_to_upload):
            files = {'file': open(self.file_to_upload, 'rb')}
            ru = requests.post(upload_url, headers=h1, files=files)
            self.ui.ptePublicLink.setPlainText(ru.text)

    def copy_to_clipboard(self):
        text = self.ui.ptePublicLink.toPlainText()
        if text != "":
            pyperclip.copy(text)


if __name__ == '__main__':
    app = QApplication()

    client = Client()
    client.show()

    app.exec_()
