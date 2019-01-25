import sys
import grade_calculator
import qdarkstyle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_Graduator(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.graduator = grade_calculator.grade_calculator()

    def setupUi(self, Graduator):
        Graduator.setObjectName("Graduator")
        Graduator.resize(287, 521)
        self.centralwidget = QtWidgets.QWidget(Graduator)
        self.centralwidget.setObjectName("centralwidget")
        self.infobox = QtWidgets.QGroupBox(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(20, 280, 251, 101))
        self.infobox.setObjectName("infobox")
        self.Parametribox = QtWidgets.QGroupBox(self.centralwidget)
        self.Parametribox.setGeometry(QtCore.QRect(20, 0, 251, 271))
        self.Parametribox.setObjectName("Parametribox")
        self.lineEdit_cfucdl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cfucdl.setGeometry(QtCore.QRect(140, 40, 113, 21))
        self.lineEdit_cfucdl.setObjectName("lineEdit_cfucdl")
        self.lineEdit_cfucdl.setText('120')
        self.label_cfucdl = QtWidgets.QLabel(self.centralwidget)
        self.label_cfucdl.setGeometry(QtCore.QRect(40, 40, 70, 16))
        self.label_cfucdl.setObjectName("label_cfucdl")
        self.lineEdit_durata = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_durata.setGeometry(QtCore.QRect(140, 80, 113, 21))
        self.lineEdit_durata.setObjectName("lineEdit_durata")
        self.lineEdit_durata.setText('0')
        self.label_durata = QtWidgets.QLabel(self.centralwidget)
        self.label_durata.setGeometry(QtCore.QRect(40, 80, 90, 16))
        self.label_durata.setObjectName("label_durata")
        self.lineEdit_media = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_media.setGeometry(QtCore.QRect(140, 120, 113, 21))
        self.lineEdit_media.setObjectName("lineEdit_media")
        self.lineEdit_media.setText('0')
        self.label_media = QtWidgets.QLabel(self.centralwidget)
        self.label_media.setGeometry(QtCore.QRect(40, 120, 61, 16))
        self.label_media.setObjectName("label_media")
        self.lineEdit_cfuesami = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cfuesami.setGeometry(QtCore.QRect(140, 160, 113, 21))
        self.lineEdit_cfuesami.setObjectName("lineEdit_cfuesami")
        self.lineEdit_cfuesami.setText('96')
        self.label_cfuesami = QtWidgets.QLabel(self.centralwidget)
        self.label_cfuesami.setGeometry(QtCore.QRect(40, 160, 75, 16))
        self.label_cfuesami.setObjectName("label_cfuesami")
        self.lineEdit_vototesi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vototesi.setGeometry(QtCore.QRect(140, 200, 113, 21))
        self.lineEdit_vototesi.setObjectName("lineEdit_vototesi")
        self.lineEdit_vototesi.setText('18')
        self.label_vototesi = QtWidgets.QLabel(self.centralwidget)
        self.label_vototesi.setGeometry(QtCore.QRect(40, 200, 60, 16))
        self.label_vototesi.setObjectName("label_vototesi")
        self.label_nlodi = QtWidgets.QLabel(self.Parametribox)
        self.label_nlodi.setGeometry(QtCore.QRect(30, 240, 71, 21))
        self.label_nlodi.setObjectName("label_nlodi")
        self.lineEdit_nlodi = QtWidgets.QLineEdit(self.Parametribox)
        self.lineEdit_nlodi.setGeometry(QtCore.QRect(120, 240, 113, 21))
        self.lineEdit_nlodi.setObjectName("lineEdit_nlodi")
        self.lineEdit_nlodi.setText('0')
        self.infobox = QtWidgets.QGroupBox(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(20, 280, 251, 101))
        self.infobox.setObjectName("infobox")
        self.plainTextEdit_info = QtWidgets.QPlainTextEdit(self.infobox)
        self.plainTextEdit_info.setGeometry(QtCore.QRect(10, 30, 231, 51))
        self.plainTextEdit_info.setObjectName("plainTextEdit_info")
        self.laureabox = QtWidgets.QGroupBox(self.centralwidget)
        self.laureabox.setGeometry(QtCore.QRect(20, 400, 251, 91))
        self.laureabox.setObjectName("laureabox")
        self.plainTextEdit_votolaurea = QtWidgets.QPlainTextEdit(self.laureabox)
        self.plainTextEdit_votolaurea.setGeometry(QtCore.QRect(30, 30, 121, 41))
        self.plainTextEdit_votolaurea.setObjectName("plainTextEdit_votolaurea")
        self.calcola_button = QtWidgets.QPushButton(self.laureabox)
        self.calcola_button.setGeometry(QtCore.QRect(160, 20, 71, 38))
        self.calcola_button.setObjectName("calcola_button")
        self.calcola_button.clicked.connect(self.compute)
        self.reset_button = QtWidgets.QPushButton(self.laureabox)
        self.reset_button.setGeometry(QtCore.QRect(170, 60, 51, 27))
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self.clear)
        Graduator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Graduator)
        self.statusbar.setObjectName("statusbar")
        Graduator.setStatusBar(self.statusbar)

        self.retranslateUi(Graduator)
        QtCore.QMetaObject.connectSlotsByName(Graduator)

    def retranslateUi(self, Graduator):
        _translate = QtCore.QCoreApplication.translate
        Graduator.setWindowTitle(_translate("Graduator", "Graduator"))
        self.label_cfucdl.setText(_translate("Graduator", "CFU c.d.l."))
        self.label_durata.setText(_translate("Graduator", "Durata (mesi)"))
        self.label_media.setText(_translate("Graduator", "Media "))
        self.label_cfuesami.setText(_translate("Graduator", "CFU esami"))
        self.label_vototesi.setText(_translate("Graduator", "Voto tesi"))
        self.Parametribox.setTitle(_translate("Graduator", "Parametri"))
        self.label_nlodi.setText(_translate("Graduator", "N. lodi"))
        self.infobox.setTitle(_translate("Graduator", "Info"))
        self.plainTextEdit_info.setPlainText(_translate("Graduator", "c.d.l. = corso di laurea\n""Media da esprimere in trentesimi\n"""))
        self.laureabox.setTitle(_translate("Graduator", "Voto di laurea in 110"))
        self.calcola_button.setText(_translate("Graduator", "Calcola"))
        self.reset_button.setText(_translate("Graduator", "Reset"))


    def compute(self):
        #self.graduator.compute_grade()
        self.plainTextEdit_votolaurea.clear()
        cfucdl = self.get_cfu_cdl()
        mesi = self.get_durata()
        avg = self.get_media()
        cfues = self.get_cfu_es()
        vototesi = self.get_voto_ts()
        nlodi = self.get_lodi()

        self.graduator.set_cfu_totali(cfucdl)
        self.graduator.set_mesi_totali(mesi)
        self.graduator.set_media_esami(avg)
        self.graduator.set_cfu_esami(cfues)
        self.graduator.set_voto_tesi(vototesi)
        self.graduator.set_lodi(nlodi)

        self.graduator.compute_grade()
        voto_finale = str(self.graduator.get_voto_finale())
        self.plainTextEdit_votolaurea.insertPlainText(voto_finale)


    def get_cfu_cdl(self):
        try:
            cfu_cdl = int(self.lineEdit_cfucdl.text())
            return cfu_cdl
        except:
            print('Input non valido')


    def get_durata(self):
        try:
            durata = int(self.lineEdit_durata.text())
            return durata
        except:
            print('Input non valido')


    def get_media(self):
        try:
            media = float(self.lineEdit_media.text())
            return media
        except:
            print('Input non valido')


    def get_cfu_es(self):
        try:
            cfu_es = int(self.lineEdit_cfuesami.text())
            return cfu_es
        except:
            print('Input non valido')


    def get_voto_ts(self):
        try:
            voto_ts = int(self.lineEdit_vototesi.text())
            return voto_ts
        except:
            print('Input non valido')


    def get_lodi(self):
        try:
            lodi = int(self.lineEdit_nlodi.text())
            return lodi
        except:
            print('Input non valido')


    def clear(self):
        self.lineEdit_cfucdl.setText('120')
        self.lineEdit_durata.setText('0')
        self.lineEdit_media.setText('0')
        self.lineEdit_cfuesami.setText('96')
        self.lineEdit_vototesi.setText('18')
        self.lineEdit_nlodi.setText('0')
        self.plainTextEdit_votolaurea.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Ui_Graduator()
    window.show()
    sys.exit(app.exec_())
