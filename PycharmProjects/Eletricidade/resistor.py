#!/usr/bin/python3.7
# -*- coding: utf-8

__author__ = 'Dalilo Sérgio Gomes Rosas'
__copyright__ = 'Copyright© 2020, Dalilo Sérgio Gomes Rosas'
__email__ = "dserggom@gmail.com"
__country__ = "Brazil"
__license__ = "MIT"
__version__ = "1.0"

"""
MIT LICENSE - English

     Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

MIT LICENSE - Português

     A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e arquivos de documentação associados (ao "Software"), para lidar com
o software sem restrição, incluindo, sem limitação, os direitos de
usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e / ou vender cópias deste
software e permitir que as pessoas a quem o software é fornecido o façam, sujeito às seguintes condições:

     O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todos
cópias ou partes substanciais do Software.

     O SOFTWARE É FORNECIDO "TAL COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO A GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO
PARA UMA FINALIDADE ESPECÍFICA E NÃO INFRACÇÃO. EM NENHUM CASO OS AUTORES OU
TITULARES DE DIREITOS AUTORAIS RESPONSABILIZAMOS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA
EM AÇÃO DE CONTRATO, TORT (ATO ILICITO CIVIL EXTRACONTRATUAL) OU OUTRA FORMA, DECORRENTE DE, FORA OU EM
CONEXÃO COM O SOFTWARE OU O USO EM OUTROS NEGÓCIOS DESTE SOFTWARE.


"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton


class Ui_Resistor(object):
    def __init__(self):
        # Labels
        self.lbl01 = QtWidgets.QLabel(Resistor)
        self.lbl02 = QtWidgets.QLabel(Resistor)
        self.lbl03 = QtWidgets.QLabel(Resistor)
        self.lbl04 = QtWidgets.QLabel(Resistor)
        self.lbl05 = QtWidgets.QLabel(Resistor)
        self.lbl06 = QtWidgets.QLabel(Resistor)
        self.lbl07 = QtWidgets.QLabel(Resistor)
        self.lbl08 = QtWidgets.QLabel(Resistor)
        self.lbl09 = QtWidgets.QLabel(Resistor)
        self.lbl10 = QtWidgets.QLabel(Resistor)
        self.lbl11 = QtWidgets.QLabel(Resistor)
        self.lbl12 = QtWidgets.QLabel(Resistor)

        # Buttons
        self.btn01 = QtWidgets.QPushButton(Resistor)
        self.btn02 = QtWidgets.QPushButton(Resistor)
        self.btn03 = QtWidgets.QPushButton(Resistor)
        self.btn04 = QtWidgets.QPushButton(Resistor)
        # self.btn05 = QtWidgets.QPushButton(Resistor)
        self.btn06 = QtWidgets.QPushButton(Resistor)
        self.btn07 = QtWidgets.QPushButton(Resistor)
        self.btn08 = QtWidgets.QPushButton(Resistor)
        self.btn09 = QtWidgets.QPushButton(Resistor)
        self.btn10 = QtWidgets.QPushButton(Resistor)
        self.btn11 = QtWidgets.QPushButton(Resistor)
        self.btn12 = QtWidgets.QPushButton(Resistor)
        self.btn13 = QtWidgets.QPushButton(Resistor)
        self.btn14 = QtWidgets.QPushButton(Resistor)
        self.btn15 = QtWidgets.QPushButton(Resistor)
        self.btn16 = QtWidgets.QPushButton(Resistor)
        self.btn17 = QtWidgets.QPushButton(Resistor)
        self.btn18 = QtWidgets.QPushButton(Resistor)
        self.btn19 = QtWidgets.QPushButton(Resistor)
        self.btn20 = QtWidgets.QPushButton(Resistor)
        self.btn21 = QtWidgets.QPushButton(Resistor)
        self.btn22 = QtWidgets.QPushButton(Resistor)
        self.btn23 = QtWidgets.QPushButton(Resistor)
        self.btn24 = QtWidgets.QPushButton(Resistor)
        self.btn25 = QtWidgets.QPushButton(Resistor)
        self.btn26 = QtWidgets.QPushButton(Resistor)
        self.btn27 = QtWidgets.QPushButton(Resistor)
        self.btn28 = QtWidgets.QPushButton(Resistor)
        self.btn29 = QtWidgets.QPushButton(Resistor)
        self.btn30 = QtWidgets.QPushButton(Resistor)
        self.btn31 = QtWidgets.QPushButton(Resistor)
        self.btn32 = QtWidgets.QPushButton(Resistor)
        self.btn33 = QtWidgets.QPushButton(Resistor)
        self.btn34 = QtWidgets.QPushButton(Resistor)
        self.btn35 = QtWidgets.QPushButton(Resistor)
        self.btn36 = QtWidgets.QPushButton(Resistor)
        self.btn37 = QtWidgets.QPushButton(Resistor)
        self.btn38 = QtWidgets.QPushButton(Resistor)
        self.btn39 = QtWidgets.QPushButton(Resistor)
        self.btn40 = QtWidgets.QPushButton(Resistor)
        self.btn41 = QtWidgets.QPushButton(Resistor)
        self.btn42 = QtWidgets.QPushButton(Resistor)
        self.btn43 = QtWidgets.QPushButton(Resistor)
        self.btn44 = QtWidgets.QPushButton(Resistor)
        self.btn45 = QtWidgets.QPushButton(Resistor)
        self.btn46 = QtWidgets.QPushButton(Resistor)
        self.btn47 = QtWidgets.QPushButton(Resistor)
        self.btn48 = QtWidgets.QPushButton(Resistor)
        self.btn49 = QtWidgets.QPushButton(Resistor)
        self.btn50 = QtWidgets.QPushButton(Resistor)
        self.btn51 = QtWidgets.QPushButton(Resistor)
        self.btn52 = QtWidgets.QPushButton(Resistor)
        # self.btn53 = QtWidgets.QPushButton(Resistor)
        self.btn54 = QtWidgets.QPushButton(Resistor)
        self.btn55 = QtWidgets.QPushButton(Resistor)
        self.btn56 = QtWidgets.QPushButton(Resistor)
        self.btn57 = QtWidgets.QPushButton(Resistor)
        self.btn58 = QtWidgets.QPushButton(Resistor)
        # self.btn59 = QtWidgets.QPushButton(Resistor)
        # self.btn60 = QtWidgets.QPushButton(Resistor)
        self.btn_exit = QtWidgets.QPushButton(Resistor)
        self.btn_calculator = QtWidgets.QPushButton(Resistor)
        self.btn_clear = QtWidgets.QPushButton(Resistor)

        # LineEdits
        self.le01 = QtWidgets.QLineEdit(Resistor)
        self.le02 = QtWidgets.QLineEdit(Resistor)
        self.le03 = QtWidgets.QLineEdit(Resistor)
        self.le04 = QtWidgets.QLineEdit(Resistor)
        self.le05 = QtWidgets.QLineEdit(Resistor)
        self.le06 = QtWidgets.QLineEdit(Resistor)
        self.le07 = QtWidgets.QLineEdit(Resistor)
        self.le08 = QtWidgets.QLineEdit(Resistor)
        self.le09 = QtWidgets.QLineEdit(Resistor)

    def setupUi(self, resistor):
        resistor.setObjectName("Resistor")
        resistor.setEnabled(True)
        resistor.resize(820, 455)
        resistor.setMinimumSize(QtCore.QSize(820, 455))
        resistor.setMaximumSize(QtCore.QSize(820, 455))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Eletronica/images/resistor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resistor.setWindowIcon(icon)

        # Labels
        self.lbl01.setGeometry(QtCore.QRect(20, 10, 121, 81))
        self.lbl01.setObjectName("lbl01")
        self.lbl02.setGeometry(QtCore.QRect(260, 50, 331, 16))
        self.lbl02.setObjectName("lbl02")
        self.lbl03.setGeometry(QtCore.QRect(20, 110, 451, 16))
        self.lbl03.setObjectName("lbl03")
        self.lbl04.setGeometry(QtCore.QRect(500, 110, 59, 15))
        self.lbl04.setObjectName("lbl04")
        self.lbl05.setGeometry(QtCore.QRect(500, 140, 59, 15))
        self.lbl05.setObjectName("lbl05")
        self.lbl06.setGeometry(QtCore.QRect(500, 170, 59, 15))
        self.lbl06.setObjectName("lbl06")
        self.lbl07.setGeometry(QtCore.QRect(500, 200, 131, 16))
        self.lbl07.setObjectName("lbl07")
        self.lbl08.setGeometry(QtCore.QRect(500, 230, 121, 16))
        self.lbl08.setObjectName("lbl08")
        self.lbl09.setGeometry(QtCore.QRect(500, 260, 151, 16))
        self.lbl09.setObjectName("lbl09")
        self.lbl10.setGeometry(QtCore.QRect(500, 290, 31, 16))
        self.lbl10.setObjectName("lbl10")
        self.lbl11.setGeometry(QtCore.QRect(500, 320, 61, 16))
        self.lbl11.setObjectName("lbl11")
        self.lbl12.setGeometry(QtCore.QRect(500, 350, 59, 15))
        self.lbl12.setObjectName("lbl12")

        #  Black button 01 settings - Digit 0
        self.btn01.setGeometry(QtCore.QRect(20, 130, 55, 25))
        self.btn01.setMinimumSize(QtCore.QSize(55, 25))
        self.btn01.setMaximumSize(QtCore.QSize(55, 25))
        self.btn01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn01.setStyleSheet("background-color: rgb(0, 0, 0); font: 9pt \"DejaVu Sans\"; color: #ffffff")
        self.btn01.setObjectName("btn01")

        # Black button 02 settings - Digit 0
        self.btn02.setGeometry(QtCore.QRect(90, 130, 55, 25))
        self.btn02.setMinimumSize(QtCore.QSize(55, 25))
        self.btn02.setMaximumSize(QtCore.QSize(55, 25))
        self.btn02.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn02.setStyleSheet("background-color: rgb(0, 0, 0); font: 9pt \"DejaVu Sans\"; color: #ffffff")
        self.btn02.setObjectName("btn02")

        # Black button 03 settings - Digit 0
        self.btn03.setGeometry(QtCore.QRect(160, 130, 55, 25))
        self.btn03.setMinimumSize(QtCore.QSize(55, 25))
        self.btn03.setMaximumSize(QtCore.QSize(55, 25))
        self.btn03.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn03.setStyleSheet("background-color: rgb(0, 0, 0); font: 9pt \"DejaVu Sans\"; color: #ffffff")
        self.btn03.setObjectName("btn03")

        # Black button 04 settings - Multiplier x1
        self.btn04.setGeometry(QtCore.QRect(230, 130, 60, 25))
        self.btn04.setMinimumSize(QtCore.QSize(60, 25))
        self.btn04.setMaximumSize(QtCore.QSize(60, 25))
        self.btn04.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn04.setStyleSheet("background-color: rgb(0, 0, 0); font: 9pt \"DejaVu Sans\"; color: #ffffff")
        self.btn04.setObjectName("btn04")

        # Black button 05 settings - Tolerance. N/A for to band
        # self.btn05.setGeometry(QtCore.QRect(300, 130, 80, 25))
        # self.btn05.setMinimumSize(QtCore.QSize(80, 25))
        # self.btn05.setMaximumSize(QtCore.QSize(80, 25))
        # self.btn05.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn05.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        # self.btn05.setObjectName("btn05")

        # Black button 06 settings - Temperature 250ppm/°C
        self.btn06.setGeometry(QtCore.QRect(390, 130, 85, 25))
        self.btn06.setMinimumSize(QtCore.QSize(85, 25))
        self.btn06.setMaximumSize(QtCore.QSize(85, 25))
        self.btn06.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn06.setStyleSheet("background-color: rgb(0, 0, 0); font: 9pt \"DejaVu Sans\"; color: #ffffff")
        self.btn06.setObjectName("btn06")

        # Brown button 07 settings - Digit 1
        self.btn07.setGeometry(QtCore.QRect(20, 160, 55, 25))
        self.btn07.setMinimumSize(QtCore.QSize(55, 25))
        self.btn07.setMaximumSize(QtCore.QSize(55, 25))
        self.btn07.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn07.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn07.setObjectName("btn07")

        # Brown button 08 settings - Digit 1
        self.btn08.setGeometry(QtCore.QRect(90, 160, 55, 25))
        self.btn08.setMinimumSize(QtCore.QSize(55, 25))
        self.btn08.setMaximumSize(QtCore.QSize(55, 25))
        self.btn08.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn08.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn08.setObjectName("btn08")

        # Brown button 09 settings - Digit 1
        self.btn09.setGeometry(QtCore.QRect(160, 160, 55, 25))
        self.btn09.setMinimumSize(QtCore.QSize(55, 25))
        self.btn09.setMaximumSize(QtCore.QSize(55, 25))
        self.btn09.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn09.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn09.setObjectName("btn09")

        # Brown button 10 settings - Multiplier x10
        self.btn10.setGeometry(QtCore.QRect(230, 160, 60, 25))
        self.btn10.setMinimumSize(QtCore.QSize(60, 25))
        self.btn10.setMaximumSize(QtCore.QSize(60, 25))
        self.btn10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn10.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn10.setObjectName("btn10")

        # Brown button 11 settings - Tolerance 1%
        self.btn11.setGeometry(QtCore.QRect(300, 130, 80, 25))
        self.btn11.setMinimumSize(QtCore.QSize(80, 25))
        self.btn11.setMaximumSize(QtCore.QSize(80, 25))
        self.btn11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn11.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn11.setObjectName("btn11")

        # Brown button 12 settings - Temperature 100ppm/°C
        self.btn12.setGeometry(QtCore.QRect(390, 160, 85, 25))
        self.btn12.setMinimumSize(QtCore.QSize(85, 25))
        self.btn12.setMaximumSize(QtCore.QSize(85, 25))
        self.btn12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn12.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.btn12.setObjectName("btn12")

        # Red button 13 settings - Digit 2
        self.btn13.setGeometry(QtCore.QRect(20, 190, 55, 25))
        self.btn13.setMinimumSize(QtCore.QSize(55, 25))
        self.btn13.setMaximumSize(QtCore.QSize(55, 25))
        self.btn13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn13.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn13.setObjectName("btn13")

        # Red button 14 settings - Digit 2
        self.btn14.setGeometry(QtCore.QRect(90, 190, 55, 25))
        self.btn14.setMinimumSize(QtCore.QSize(55, 25))
        self.btn14.setMaximumSize(QtCore.QSize(55, 25))
        self.btn14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn14.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn14.setObjectName("btn14")

        # Red button 15 settings - Digit 2
        self.btn15.setGeometry(QtCore.QRect(160, 190, 55, 25))
        self.btn15.setMinimumSize(QtCore.QSize(55, 25))
        self.btn15.setMaximumSize(QtCore.QSize(55, 25))
        self.btn15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn15.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn15.setObjectName("btn15")

        # Red button 16 settings - Multiplier x100
        self.btn16.setGeometry(QtCore.QRect(230, 190, 60, 25))
        self.btn16.setMinimumSize(QtCore.QSize(60, 25))
        self.btn16.setMaximumSize(QtCore.QSize(60, 25))
        self.btn16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn16.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn16.setObjectName("btn16")

        # Red button 17 settings - Tolerance 2%
        self.btn17.setGeometry(QtCore.QRect(300, 160, 80, 25))
        self.btn17.setMinimumSize(QtCore.QSize(80, 25))
        self.btn17.setMaximumSize(QtCore.QSize(80, 25))
        self.btn17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn17.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn17.setObjectName("btn17")

        # Red button 18 settings - Temperature 50ppm/°C
        self.btn18.setGeometry(QtCore.QRect(390, 190, 85, 25))
        self.btn18.setMinimumSize(QtCore.QSize(85, 25))
        self.btn18.setMaximumSize(QtCore.QSize(85, 25))
        self.btn18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn18.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.btn18.setObjectName("btn18")

        # Orange button 19 settings - Digit 3
        self.btn19.setGeometry(QtCore.QRect(20, 220, 55, 25))
        self.btn19.setMinimumSize(QtCore.QSize(55, 25))
        self.btn19.setMaximumSize(QtCore.QSize(55, 25))
        self.btn19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn19.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.btn19.setObjectName("btn19")

        # Orange button 20 settings - Digit 3
        self.btn20.setGeometry(QtCore.QRect(90, 220, 55, 25))
        self.btn20.setMinimumSize(QtCore.QSize(55, 25))
        self.btn20.setMaximumSize(QtCore.QSize(55, 25))
        self.btn20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn20.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.btn20.setObjectName("btn20")

        # Orange button 21 settings - Digit 3
        self.btn21.setGeometry(QtCore.QRect(160, 220, 55, 25))
        self.btn21.setMinimumSize(QtCore.QSize(55, 25))
        self.btn21.setMaximumSize(QtCore.QSize(55, 25))
        self.btn21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn21.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.btn21.setObjectName("btn21")

        # Orange button 22 settings - Multiplier x1000
        self.btn22.setGeometry(QtCore.QRect(230, 220, 60, 25))
        self.btn22.setMinimumSize(QtCore.QSize(60, 25))
        self.btn22.setMaximumSize(QtCore.QSize(60, 25))
        self.btn22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn22.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.btn22.setObjectName("btn22")

        # Gold button 23 settings - Tolerance 5%
        self.btn23.setGeometry(QtCore.QRect(300, 190, 80, 25))
        self.btn23.setMinimumSize(QtCore.QSize(80, 25))
        self.btn23.setMaximumSize(QtCore.QSize(80, 25))
        self.btn23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn23.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.btn23.setObjectName("btn23")

        # Red button 24 settings - Temperature 15ppm/°C
        self.btn24.setGeometry(QtCore.QRect(390, 220, 85, 25))
        self.btn24.setMinimumSize(QtCore.QSize(85, 25))
        self.btn24.setMaximumSize(QtCore.QSize(85, 25))
        self.btn24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn24.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.btn24.setObjectName("btn24")

        # Yellow button 25 settings - Digit 4
        self.btn25.setGeometry(QtCore.QRect(20, 250, 55, 25))
        self.btn25.setMinimumSize(QtCore.QSize(55, 25))
        self.btn25.setMaximumSize(QtCore.QSize(55, 25))
        self.btn25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn25.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.btn25.setObjectName("btn25")

        # Yellow button 26 settings - Digit 4
        self.btn26.setGeometry(QtCore.QRect(90, 250, 55, 25))
        self.btn26.setMinimumSize(QtCore.QSize(55, 25))
        self.btn26.setMaximumSize(QtCore.QSize(55, 25))
        self.btn26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn26.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.btn26.setObjectName("btn26")

        # Yellow button 27 settings - Digit 4
        self.btn27.setGeometry(QtCore.QRect(160, 250, 55, 25))
        self.btn27.setMinimumSize(QtCore.QSize(55, 25))
        self.btn27.setMaximumSize(QtCore.QSize(55, 25))
        self.btn27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn27.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.btn27.setObjectName("btn27")

        # Yellow button 28 settings - Multiplier x10000
        self.btn28.setGeometry(QtCore.QRect(230, 250, 60, 25))
        self.btn28.setMinimumSize(QtCore.QSize(60, 25))
        self.btn28.setMaximumSize(QtCore.QSize(60, 25))
        self.btn28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn28.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.btn28.setObjectName("btn28")

        # Silver button 29 settings - Tolerance 10%
        self.btn29.setGeometry(QtCore.QRect(300, 220, 80, 25))
        self.btn29.setMinimumSize(QtCore.QSize(80, 25))
        self.btn29.setMaximumSize(QtCore.QSize(80, 25))
        self.btn29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn29.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.btn29.setObjectName("btn29")

        # Yellow button 20 settings - Temperature 25ppm/°C
        self.btn30.setGeometry(QtCore.QRect(390, 250, 85, 25))
        self.btn30.setMinimumSize(QtCore.QSize(85, 25))
        self.btn30.setMaximumSize(QtCore.QSize(85, 25))
        self.btn30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn30.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.btn30.setObjectName("btn30")

        # Green button 31 settings - Digit 5
        self.btn31.setGeometry(QtCore.QRect(20, 280, 55, 25))
        self.btn31.setMinimumSize(QtCore.QSize(55, 25))
        self.btn31.setMaximumSize(QtCore.QSize(55, 25))
        self.btn31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn31.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn31.setObjectName("btn31")

        # Green button 32 settings - Digit 5
        self.btn32.setGeometry(QtCore.QRect(90, 280, 55, 25))
        self.btn32.setMinimumSize(QtCore.QSize(55, 25))
        self.btn32.setMaximumSize(QtCore.QSize(55, 25))
        self.btn32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn32.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn32.setObjectName("btn32")

        # Green button 36 settings - Digit 5
        self.btn33.setGeometry(QtCore.QRect(160, 280, 55, 25))
        self.btn33.setMinimumSize(QtCore.QSize(55, 25))
        self.btn33.setMaximumSize(QtCore.QSize(55, 25))
        self.btn33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn33.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn33.setObjectName("btn33")

        # Green button 34 settings - Multiplier x100000
        self.btn34.setGeometry(QtCore.QRect(230, 280, 60, 25))
        self.btn34.setMinimumSize(QtCore.QSize(60, 25))
        self.btn34.setMaximumSize(QtCore.QSize(60, 25))
        self.btn34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn34.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn34.setObjectName("btn34")

        # Green button 35 settings - Tolerance 0.50%
        self.btn35.setGeometry(QtCore.QRect(300, 250, 80, 25))
        self.btn35.setMinimumSize(QtCore.QSize(80, 25))
        self.btn35.setMaximumSize(QtCore.QSize(80, 25))
        self.btn35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn35.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn35.setObjectName("btn35")

        # Green button 36 settings - Temperature 20ppm/°C
        self.btn36.setGeometry(QtCore.QRect(390, 280, 85, 25))
        self.btn36.setMinimumSize(QtCore.QSize(85, 25))
        self.btn36.setMaximumSize(QtCore.QSize(85, 25))
        self.btn36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn36.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.btn36.setObjectName("btn36")

        # Blue button 37 settings - Digit 6
        self.btn37.setGeometry(QtCore.QRect(20, 310, 55, 25))
        self.btn37.setMinimumSize(QtCore.QSize(55, 25))
        self.btn37.setMaximumSize(QtCore.QSize(55, 25))
        self.btn37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn37.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn37.setObjectName("btn37")

        # Blue button 38 settings - Digit 6
        self.btn38.setGeometry(QtCore.QRect(90, 310, 55, 25))
        self.btn38.setMinimumSize(QtCore.QSize(55, 25))
        self.btn38.setMaximumSize(QtCore.QSize(55, 25))
        self.btn38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn38.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn38.setObjectName("btn38")

        # Blue button 39 settings - Digit 6
        self.btn39.setGeometry(QtCore.QRect(160, 310, 55, 25))
        self.btn39.setMinimumSize(QtCore.QSize(55, 25))
        self.btn39.setMaximumSize(QtCore.QSize(55, 25))
        self.btn39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn39.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn39.setObjectName("btn39")

        # Green button 41 settings - Multiplier x1000000
        self.btn40.setGeometry(QtCore.QRect(230, 310, 60, 25))
        self.btn40.setMinimumSize(QtCore.QSize(60, 25))
        self.btn40.setMaximumSize(QtCore.QSize(60, 25))
        self.btn40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn40.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn40.setObjectName("btn40")

        # Blue button 41 settings - Tolerance 0.25%
        self.btn41.setGeometry(QtCore.QRect(300, 280, 80, 25))
        self.btn41.setMinimumSize(QtCore.QSize(80, 25))
        self.btn41.setMaximumSize(QtCore.QSize(80, 25))
        self.btn41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn41.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn41.setObjectName("btn41")

        # Green button 42 settings - Temperature 10ppm/°C
        self.btn42.setGeometry(QtCore.QRect(390, 310, 85, 25))
        self.btn42.setMinimumSize(QtCore.QSize(85, 25))
        self.btn42.setMaximumSize(QtCore.QSize(85, 25))
        self.btn42.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn42.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btn42.setObjectName("btn42")

        # Purple/Lilac button 43 settings - Digit 7
        self.btn43.setGeometry(QtCore.QRect(20, 340, 55, 25))
        self.btn43.setMinimumSize(QtCore.QSize(55, 25))
        self.btn43.setMaximumSize(QtCore.QSize(55, 25))
        self.btn43.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn43.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn43.setObjectName("btn43")

        # Purple/Lilac button 44  settings - Digit 7
        self.btn44.setGeometry(QtCore.QRect(90, 340, 55, 25))
        self.btn44.setMinimumSize(QtCore.QSize(55, 25))
        self.btn44.setMaximumSize(QtCore.QSize(55, 25))
        self.btn44.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn44.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn44.setObjectName("btn44")

        # Purple/Lilac button 45 settings - Digit 7
        self.btn45.setGeometry(QtCore.QRect(160, 340, 55, 25))
        self.btn45.setMinimumSize(QtCore.QSize(55, 25))
        self.btn45.setMaximumSize(QtCore.QSize(55, 25))
        self.btn45.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn45.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn45.setObjectName("btn45")

        # Purple/Lilac button 46 settings - Multiplier x10000000
        self.btn46.setGeometry(QtCore.QRect(230, 340, 60, 25))
        self.btn46.setMinimumSize(QtCore.QSize(60, 25))
        self.btn46.setMaximumSize(QtCore.QSize(60, 25))
        self.btn46.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn46.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn46.setObjectName("btn46")

        # Purple/Lilac button 47 settings - Tolerance 0.10%
        self.btn47.setGeometry(QtCore.QRect(300, 310, 80, 25))
        self.btn47.setMinimumSize(QtCore.QSize(80, 25))
        self.btn47.setMaximumSize(QtCore.QSize(80, 25))
        self.btn47.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn47.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn47.setObjectName("btn47")

        # Purple/Lilac button 48 settings - Temperature 5ppm/°C
        self.btn48.setGeometry(QtCore.QRect(390, 340, 85, 25))
        self.btn48.setMinimumSize(QtCore.QSize(85, 25))
        self.btn48.setMaximumSize(QtCore.QSize(85, 25))
        self.btn48.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn48.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.btn48.setObjectName("btn48")

        # Grey button 49 settings - Digit 8
        self.btn49.setGeometry(QtCore.QRect(20, 370, 55, 25))
        self.btn49.setMinimumSize(QtCore.QSize(55, 25))
        self.btn49.setMaximumSize(QtCore.QSize(55, 25))
        self.btn49.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn49.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.btn49.setObjectName("btn49")

        # Grey button 50 settings - Digit 8
        self.btn50.setGeometry(QtCore.QRect(90, 370, 55, 25))
        self.btn50.setMinimumSize(QtCore.QSize(55, 25))
        self.btn50.setMaximumSize(QtCore.QSize(55, 25))
        self.btn50.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn50.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.btn50.setObjectName("btn50")

        # Grey button 51 settings - Digit 8
        self.btn51.setGeometry(QtCore.QRect(160, 370, 55, 25))
        self.btn51.setMinimumSize(QtCore.QSize(55, 25))
        self.btn51.setMaximumSize(QtCore.QSize(55, 25))
        self.btn51.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn51.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.btn51.setObjectName("btn51")

        # Grey button 46 settings - Multiplier x100000000
        self.btn52.setGeometry(QtCore.QRect(230, 370, 60, 25))
        self.btn52.setMinimumSize(QtCore.QSize(60, 25))
        self.btn52.setMaximumSize(QtCore.QSize(60, 25))
        self.btn52.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn52.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.btn52.setObjectName("btn52")

        # Grey button N/A
        # self.btn53.setGeometry(QtCore.QRect(300, 370, 80, 25))
        # self.btn53.setMinimumSize(QtCore.QSize(80, 25))
        # self.btn53.setMaximumSize(QtCore.QSize(80, 25))
        # self.btn53.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn53.setStyleSheet("background-color: rgb(46, 52, 54);")
        # self.btn53.setObjectName("btn53")

        # Grey button 54 settings - Temperature 1ppm/°C
        self.btn54.setGeometry(QtCore.QRect(390, 370, 85, 25))
        self.btn54.setMinimumSize(QtCore.QSize(85, 25))
        self.btn54.setMaximumSize(QtCore.QSize(85, 25))
        self.btn54.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn54.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.btn54.setObjectName("btn54")

        # White button 55 settings - Digit 9
        self.btn55.setGeometry(QtCore.QRect(20, 400, 55, 25))
        self.btn55.setMinimumSize(QtCore.QSize(55, 25))
        self.btn55.setMaximumSize(QtCore.QSize(55, 25))
        self.btn55.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn55.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn55.setObjectName("btn55")

        # White button 56 settings - Digit 9
        self.btn56.setGeometry(QtCore.QRect(90, 400, 55, 25))
        self.btn56.setMinimumSize(QtCore.QSize(55, 25))
        self.btn56.setMaximumSize(QtCore.QSize(55, 25))
        self.btn56.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn56.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn56.setObjectName("btn56")

        # White button 57 settings - Digit 9
        self.btn57.setGeometry(QtCore.QRect(160, 400, 55, 25))
        self.btn57.setMinimumSize(QtCore.QSize(55, 25))
        self.btn57.setMaximumSize(QtCore.QSize(55, 25))
        self.btn57.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn57.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn57.setObjectName("btn57")

        # White button 58 settings - Multiplier x1000000000
        self.btn58.setGeometry(QtCore.QRect(230, 400, 60, 25))
        self.btn58.setMinimumSize(QtCore.QSize(60, 25))
        self.btn58.setMaximumSize(QtCore.QSize(60, 25))
        self.btn58.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn58.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn58.setObjectName("btn58")

        # self.btn59.setGeometry(QtCore.QRect(300, 400, 80, 25))
        # self.btn59.setMinimumSize(QtCore.QSize(80, 25))
        # self.btn59.setMaximumSize(QtCore.QSize(80, 25))
        # self.btn59.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn59.setStyleSheet(" background-color: rgb(243, 243, 243);")
        # self.btn59.setObjectName("btn59")

        # self.btn60.setGeometry(QtCore.QRect(390, 400, 85, 25))
        # self.btn60.setMinimumSize(QtCore.QSize(85, 25))
        # self.btn60.setMaximumSize(QtCore.QSize(85, 25))
        # self.btn60.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.btn60.setStyleSheet("background-color: rgb(243, 243, 243);")
        # self.btn60.setObjectName("btn60")

        self.btn_clear.setGeometry(QtCore.QRect(500, 400, 80, 25))
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_clear.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setObjectName("btn_clear")

        self.btn_calculator.setGeometry(QtCore.QRect(610, 400, 80, 25))
        self.btn_calculator.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_calculator.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_calculator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_calculator.setObjectName("btn_calculator")

        self.btn_exit.setGeometry(QtCore.QRect(720, 400, 80, 25))
        self.btn_exit.setMinimumSize(QtCore.QSize(80, 25))
        self.btn_exit.setMaximumSize(QtCore.QSize(80, 25))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setObjectName("btn_exit")

        self.retranslateUi(resistor)
        self.btn_clear.clicked.connect(self.le01.clear)
        self.btn_clear.clicked.connect(self.le02.clear)
        self.btn_clear.clicked.connect(self.le03.clear)
        self.btn_clear.clicked.connect(self.le04.clear)
        self.btn_clear.clicked.connect(self.le05.clear)
        self.btn_clear.clicked.connect(self.le06.clear)
        self.btn_clear.clicked.connect(self.le07.clear)
        self.btn_clear.clicked.connect(self.le08.clear)
        self.btn_clear.clicked.connect(self.le09.clear)
        self.btn_exit.clicked.connect(resistor.close)
        QtCore.QMetaObject.connectSlotsByName(resistor)

        self.le01.setGeometry(QtCore.QRect(670, 100, 20, 22))
        self.le01.setMinimumSize(QtCore.QSize(20, 22))
        self.le01.setMaximumSize(QtCore.QSize(20, 22))
        self.le01.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le01.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.le01.setObjectName("le01")

        self.le02.setGeometry(QtCore.QRect(670, 130, 20, 22))
        self.le02.setMinimumSize(QtCore.QSize(20, 22))
        self.le02.setMaximumSize(QtCore.QSize(20, 22))
        self.le02.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le02.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.le02.setObjectName("le02")

        self.le03.setGeometry(QtCore.QRect(670, 160, 20, 22))
        self.le03.setMinimumSize(QtCore.QSize(20, 22))
        self.le03.setMaximumSize(QtCore.QSize(20, 22))
        self.le03.setMaxLength(13)

        self.le03.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le03.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.le03.setObjectName("le03")

        self.le04.setGeometry(QtCore.QRect(670, 190, 90, 22))
        self.le04.setMinimumSize(QtCore.QSize(90, 22))
        self.le04.setMaximumSize(QtCore.QSize(90, 22))
        self.le03.setMaxLength(13)
        self.le04.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le04.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.le04.setObjectName("le04")

        self.le05.setGeometry(QtCore.QRect(670, 220, 45, 22))
        self.le05.setMinimumSize(QtCore.QSize(45, 22))
        self.le05.setMaximumSize(QtCore.QSize(45, 22))
        self.le05.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le05.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le05.setInputMask("")
        self.le05.setMaxLength(5)
        self.le05.setObjectName("le05")

        self.le06.setGeometry(QtCore.QRect(670, 250, 90, 22))
        self.le06.setMinimumSize(QtCore.QSize(90, 22))
        self.le06.setMaximumSize(QtCore.QSize(90, 22))
        self.le06.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le06.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.le06.setInputMask("")
        self.le06.setObjectName("le06")

        self.le07.setGeometry(QtCore.QRect(670, 280, 130, 22))
        self.le07.setMinimumSize(QtCore.QSize(130, 22))
        self.le07.setMaximumSize(QtCore.QSize(130, 22))
        self.le07.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le07.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le07.setInputMask("")
        self.le07.setMaxLength(15)
        self.le07.setObjectName("le07")

        self.le08.setGeometry(QtCore.QRect(670, 310, 130, 22))
        self.le08.setMinimumSize(QtCore.QSize(130, 22))
        self.le08.setMaximumSize(QtCore.QSize(130, 22))
        self.le08.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le08.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le08.setInputMask("")
        self.le08.setMaxLength(15)
        self.le08.setObjectName("le08")

        self.le09.setGeometry(QtCore.QRect(670, 340, 130, 22))
        self.le09.setMinimumSize(QtCore.QSize(130, 22))
        self.le09.setMaximumSize(QtCore.QSize(130, 22))
        self.le09.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le09.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le09.setInputMask("")
        self.le09.setMaxLength(15)
        self.le09.setObjectName("le09")

    def retranslateUi(self, resistor):
        _translate = QtCore.QCoreApplication.translate
        resistor.setWindowTitle(_translate("Resistor", "ResisThor"))

        # Texto e configuração das labels
        self.lbl01.setText("")

        self.lbl01.setPixmap(QtGui.QPixmap("../Eletronica/images/Logotipo.png"))
        self.lbl02.setText(_translate("Resistor", "Calculadora de Código de Cores Para Resistores"))
        self.lbl03.setText(_translate("Resistor", " 1ª Faixa       2ª Faixa     3ª Faixa     4ª  Faixa       5ª  Faixa           6ª  Faixa"))
        self.lbl04.setText(_translate("Resistor", "1ª Faixa"))
        self.lbl05.setText(_translate("Resistor", "2ª Faixa"))
        self.lbl06.setText(_translate("Resistor", "3ª Faixa"))
        self.lbl07.setText(_translate("Resistor", "4ª Faixa/Multiplicador"))
        self.lbl08.setText(_translate("Resistor", "5ª Faixa/Tolerancia"))
        self.lbl09.setText(_translate("Resistor", "6ª Faixa/Temperatura °C"))
        self.lbl10.setText(_translate("Resistor", "Valor"))
        self.lbl11.setText(_translate("Resistor", "Valor Max."))
        self.lbl12.setText(_translate("Resistor", "Valor Min."))

        # Texto e configuração dos botões
        # self.btn01.setText(_translate("Resistor", "N/A"))
        self.btn01.setToolTip("Não se aplica")
        self.btn01.setStyleSheet('QPushButton {background-color: rgb(0, 0, 0); font-size: 12px; color: rgb(255, 255, 255)}')
        self.btn01.setText(_translate("Resistor", "0"))
        # self.btn01.setEnabled(False)
        self.btn02.setText(_translate("Resistor", "0"))
        self.btn03.setText(_translate("Resistor", "0"))
        self.btn04.setText(_translate("Resistor", "10⁰"))
        # self.btn05.setText(_translate("Resistor", "N/A"))
        # self.btn05.setToolTip("Não se aplica")
        # self.btn05.setStyleSheet('QPushButton {background-color: rgb(0, 0, 0); font-size: 12px; color: rgb(255, 255, 255)}')
        # self.btn05.setText(_translate("Resistor", "N/A"))
        # self.btn05.setEnabled(False)
        self.btn06.setText(_translate("Resistor", "250ppm/°C"))
        self.btn07.setText(_translate("Resistor", "1"))
        self.btn08.setText(_translate("Resistor", "1"))
        self.btn09.setText(_translate("Resistor", "1"))
        self.btn10.setText(_translate("Resistor", "10¹"))
        self.btn11.setText(_translate("Resistor", "± 1%"))
        self.btn12.setText(_translate("Resistor", "100ppm/°C"))
        self.btn13.setText(_translate("Resistor", "2"))
        self.btn14.setText(_translate("Resistor", "2"))
        self.btn15.setText(_translate("Resistor", "2"))
        self.btn16.setText(_translate("Resistor", "10²"))
        self.btn17.setText(_translate("Resistor", "± 2%"))
        self.btn18.setText(_translate("Resistor", "50ppm/°C"))
        self.btn19.setText(_translate("Resistor", "3"))
        self.btn20.setText(_translate("Resistor", "3"))
        self.btn21.setText(_translate("Resistor", "3"))
        self.btn22.setText(_translate("Resistor", "10³"))
        # self.btn23.setToolTip(_translate("Resistor", "<html><head/><body><p>Ouro</p></body></html>"))
        # self.btn23.setText(_translate("Resistor", "±  5%"))
        self.btn23.setToolTip("Ouro")
        self.btn23.setStyleSheet('QPushButton {background-color: rgb(196, 160, 0); font-size: 12px; color: rgb(0, 0, 0)}')
        self.btn23.setText(_translate("Resistor", "±  5%"))
        self.btn24.setText(_translate("Resistor", "15ppm/°C"))
        self.btn25.setText(_translate("Resistor", "4"))
        self.btn26.setText(_translate("Resistor", "4"))
        self.btn27.setText(_translate("Resistor", "4"))
        self.btn28.setText(_translate("Resistor", "10⁴"))
        # self.btn29.setText(_translate("Resistor", "±  10%"))
        # self.btn29.setToolTip(_translate("Resistor", "<html><head/><body><p>Prata</p></body></html>"))
        self.btn29.setToolTip("Prata")
        self.btn29.setStyleSheet('QPushButton {background-color: rgb(186, 189, 182); font-size: 12px; color: rgb(0, 0, 0)}')
        self.btn29.setText(_translate("Resistor", "±  10%"))
        self.btn30.setText(_translate("Resistor", "25ppm/°C"))
        self.btn31.setText(_translate("Resistor", "5"))
        self.btn32.setText(_translate("Resistor", "5"))
        self.btn33.setText(_translate("Resistor", "5"))
        self.btn34.setText(_translate("Resistor", "10⁵"))
        self.btn35.setText(_translate("Resistor", "±  0.50%"))
        self.btn36.setText(_translate("Resistor", "20ppm/°C"))
        self.btn37.setText(_translate("Resistor", "6"))
        self.btn38.setText(_translate("Resistor", "6"))
        self.btn39.setText(_translate("Resistor", "6"))
        self.btn40.setText(_translate("Resistor", "10⁶"))
        self.btn41.setText(_translate("Resistor", "±  0.25%"))
        self.btn42.setText(_translate("Resistor", "10ppm/°C"))
        self.btn43.setText(_translate("Resistor", "7"))
        self.btn44.setText(_translate("Resistor", "7"))
        self.btn45.setText(_translate("Resistor", "7"))
        self.btn46.setText(_translate("Resistor", "10⁷"))
        self.btn47.setText(_translate("Resistor", "± 0.10%"))
        self.btn48.setText(_translate("Resistor", "5ppm/°C"))
        self.btn49.setText(_translate("Resistor", "8"))
        self.btn50.setText(_translate("Resistor", "8"))
        self.btn51.setText(_translate("Resistor", "8"))
        self.btn52.setText(_translate("Resistor", "10⁸"))
        # self.btn53.setText(_translate("Resistor", "N/A"))
        # self.btn53.setToolTip("Não se aplica para a faixa")
        # self.btn53.setStyleSheet('QPushButton {background-color: rgb(46, 52, 54); font-size: 12px; color:#000000}')
        # self.btn53.setText(_translate("Resistor", "N/A"))
        # self.btn53.setEnabled(False)
        self.btn54.setText(_translate("Resistor", "1ppm/°C"))
        self.btn55.setText(_translate("Resistor", "9"))
        self.btn56.setText(_translate("Resistor", "9"))
        self.btn57.setText(_translate("Resistor", "9"))
        self.btn58.setText(_translate("Resistor", "10⁹"))
        # self.btn59.setText(_translate("Resistor", "N/A"))
        # self.btn60.setText(_translate("Resistor", "N/A"))
        # self.btn59.setToolTip("Não se aplica")
        # self.btn59.setStyleSheet('QPushButton {background-color: rgb(238, 238, 236); font-size: 12px; color: rgb(0, 0, 0)}')
        # self.btn59.setText(_translate("Resistor", "N/A"))
        # self.btn59.setEnabled(False)
        # self.btn60.setToolTip("Não se aplica")
        # self.btn60.setStyleSheet('QPushButton {background-color: rgb(238, 238, 236); font-size: 12px; color: rgb(0, 0, 0)}')
        # self.btn60.setText(_translate("Resistor", "N/A"))
        # self.btn60.setEnabled(False)
        self.btn_clear.setText(_translate("Resistor", "Limpar"))
        self.btn_calculator.setText(_translate("Resistor", "Calcular"))
        self.btn_exit.setText(_translate("Resistor", "Sair"))

        # Texto e configurações de máscara das lineEdits
        self.le01.setInputMask(_translate("Resistor", "9"))
        self.le02.setInputMask(_translate("Resistor", "9"))
        self.le03.setInputMask(_translate("Resistor", "9"))
        self.le04.setInputMask(_translate("Resistor", "999999999999"))

        # Ação dos botões
        # Botões 1 a 6 Band - preto
        self.btn01.clicked.connect(lambda: self.clk1(self.btn01))
        self.btn02.clicked.connect(lambda: self.clk2(self.btn02))
        self.btn03.clicked.connect(lambda: self.clk3(self.btn03))
        self.btn04.clicked.connect(lambda: self.clk4(self.btn04))
        # Button 5 - N/A
        self.btn06.clicked.connect(lambda: self.clk6(self.btn06))

        # Botões 7 a 12 Band marrom
        self.btn07.clicked.connect(lambda: self.clk7(self.btn07))
        self.btn08.clicked.connect(lambda: self.clk8(self.btn08))
        self.btn09.clicked.connect(lambda: self.clk9(self.btn09))
        self.btn10.clicked.connect(lambda: self.clk10(self.btn10))
        self.btn11.clicked.connect(lambda: self.clk11(self.btn11))
        self.btn12.clicked.connect(lambda: self.clk12(self.btn12))

        # Botões 13 a 18 Band vermelho
        self.btn13.clicked.connect(lambda: self.clk13(self.btn13))
        self.btn14.clicked.connect(lambda: self.clk14(self.btn14))
        self.btn15.clicked.connect(lambda: self.clk15(self.btn15))
        self.btn16.clicked.connect(lambda: self.clk16(self.btn16))
        self.btn17.clicked.connect(lambda: self.clk17(self.btn17))
        self.btn18.clicked.connect(lambda: self.clk18(self.btn18))

        # Botões 19 a 24 Band laranja
        self.btn19.clicked.connect(lambda: self.clk19(self.btn19))
        self.btn20.clicked.connect(lambda: self.clk20(self.btn20))
        self.btn21.clicked.connect(lambda: self.clk21(self.btn21))
        self.btn22.clicked.connect(lambda: self.clk22(self.btn22))
        self.btn23.clicked.connect(lambda: self.clk23(self.btn23))
        self.btn24.clicked.connect(lambda: self.clk24(self.btn24))

        # Botões 25 a 30 Band amarelo
        self.btn25.clicked.connect(lambda: self.clk25(self.btn25))
        self.btn26.clicked.connect(lambda: self.clk26(self.btn26))
        self.btn27.clicked.connect(lambda: self.clk27(self.btn27))
        self.btn28.clicked.connect(lambda: self.clk28(self.btn28))
        self.btn29.clicked.connect(lambda: self.clk29(self.btn29))
        self.btn30.clicked.connect(lambda: self.clk30(self.btn30))

        # Botões 31 a 36 Band verde
        self.btn31.clicked.connect(lambda: self.clk31(self.btn31))
        self.btn32.clicked.connect(lambda: self.clk32(self.btn32))
        self.btn33.clicked.connect(lambda: self.clk33(self.btn33))
        self.btn34.clicked.connect(lambda: self.clk34(self.btn34))
        self.btn35.clicked.connect(lambda: self.clk35(self.btn35))
        self.btn36.clicked.connect(lambda: self.clk36(self.btn36))

        # Botões 37 a 42 Band azul
        self.btn37.clicked.connect(lambda: self.clk37(self.btn37))
        self.btn38.clicked.connect(lambda: self.clk38(self.btn38))
        self.btn39.clicked.connect(lambda: self.clk39(self.btn39))
        self.btn40.clicked.connect(lambda: self.clk40(self.btn40))
        self.btn41.clicked.connect(lambda: self.clk41(self.btn41))
        self.btn42.clicked.connect(lambda: self.clk42(self.btn42))

        # Botões 43 a 48 Band lilás/roxo
        self.btn43.clicked.connect(lambda: self.clk43(self.btn43))
        self.btn44.clicked.connect(lambda: self.clk44(self.btn44))
        self.btn45.clicked.connect(lambda: self.clk45(self.btn45))
        self.btn46.clicked.connect(lambda: self.clk46(self.btn46))
        self.btn47.clicked.connect(lambda: self.clk47(self.btn47))
        self.btn48.clicked.connect(lambda: self.clk48(self.btn48))

        # Botões 49 a 54 Band cinza
        self.btn49.clicked.connect(lambda: self.clk49(self.btn49))
        self.btn50.clicked.connect(lambda: self.clk50(self.btn50))
        self.btn51.clicked.connect(lambda: self.clk51(self.btn51))
        self.btn52.clicked.connect(lambda: self.clk52(self.btn52))
        # Button 53 N/A
        self.btn54.clicked.connect(lambda: self.clk54(self.btn54))

        # Botões 55 a 58 Band branco
        self.btn55.clicked.connect(lambda: self.clk55(self.btn55))
        self.btn56.clicked.connect(lambda: self.clk56(self.btn56))
        self.btn57.clicked.connect(lambda: self.clk57(self.btn57))
        self.btn58.clicked.connect(lambda: self.clk58(self.btn58))

    # Disables the calculate button if all fields are not filled
        self.le06.textChanged[str].connect(lambda: self.btn_calculator.setEnabled(self.le06.text() != ""))

    # Enables the calculate button if all fields are filled
        self.btn_calculator.setDisabled(True)
        self.le01.textChanged.connect(self.disableButton)

    # Function enables / disables calculation button
    def disableButton(self):
        if len(self.le05.text()) > 0:
            self.btn_calculator.setDisabled(False)

        # Calculation button
        self.btn_calculator.clicked.connect(self.calculo)

    # Black and
    # Button 1 - Band 1 - Digit 0
    def clk1(self, string):
        self.le01.setText('0')
        return string

    # Button 2 - Band 2 - Digit 0
    def clk2(self, string):
        self.le02.setText('0')
        # print(string)
        return string

    # Button 3 - Band 3 - Digit 0
    def clk3(self, string):
        self.le03.setText('0')
        return string

    # Button 4 - Band 4 - Multiplier x1
    def clk4(self, string):
        self.le04.setText('1')
        return string

    # Button 5 - N/A

    # Button 6 - Band 6 - Temperature 50ppm/°C
    def clk6(self, string):
        self.le06.setText('250ppm/°C')
        return string

    # Brown band
    # Button 7 - Band 1 - Digit 1
    def clk7(self, string):
        self.le01.setText('1')
        # print(string)
        return string

    # Button 8 - Band 2 - Digit 1
    def clk8(self, string):
        self.le02.setText('1')
        return string

    # Button 9 - Band 3 - Digit 1
    def clk9(self, string):
        self.le03.setText('1')
        return string

    # Button 10 - Band 4- Multiplier x10
    def clk10(self, string):
        self.le04.setText('10')
        return string

    # Button 11 - Band 5- Tolerance/Percentage 1%
    def clk11(self, string):
        self.le05.setText('1')
        return string

    # Button 12 - Band 6 - Temperature 100ppm/°C
    def clk12(self, string):
        self.le06.setText('100ppm/°C')
        return string

    # Red band
    # Button 13 - Band 1 - Digit 2
    def clk13(self, string):
        self.le01.setText('2')
        return string

    # Button 14 - Band 2 - Digit 2
    def clk14(self, string):
        self.le02.setText('2')
        return string

    # Button 15 - Band 3 - Digit 2
    def clk15(self, string):
        self.le03.setText('2')
        return string

    # Button 16 - Band 4 - Multiplier x100
    def clk16(self, string):
        self.le04.setText('100')
        return string

    # Button 17 - Band 5 - Tolerance/Percentage 2%
    def clk17(self, string):
        self.le05.setText('2')
        return string

    # Button 18 Band 6 - Temperature 50ppm/°C
    def clk18(self, string):
        self.le06.setText('50ppm/°C')
        return string

    # Orange band
    # Button 19 - 1ª Band - Digit 3
    def clk19(self, string):
        self.le01.setText('3')
        return string

    # Button - 20 2ª Band - Digit 3
    def clk20(self, string):
        self.le02.setText('3')
        return string

    # Button - 21 Band 3 - Digit 3
    def clk21(self, string):
        self.le03.setText('3')
        return string

    # Button 22 - Band 4 - Multiplier x1.000
    def clk22(self, string):
        self.le04.setText('1000')
        return string

    # Button 23 - Band 5 -  5%
    def clk23(self, string):
        self.le05.setText('5')
        return string

    # Button 24 - Band 6 - Temperature 15ppm/°C
    def clk24(self, string):
        self.le06.setText('15ppm/°C')
        return string

    # Yellow band
    # Button 25 - 1ª Band - Digit 4
    def clk25(self, string):
        self.le01.setText('4')
        return string

    # Button 26 - 2ª Band - Digit 4
    def clk26(self, string):
        self.le02.setText('4')
        return string

    # Button 27 - Band 3 - Digit 4
    def clk27(self, string):
        self.le03.setText('4')
        return string

    # Button 28 - Band 4 - Multiplier x10.000
    def clk28(self, string):
        self.le04.setText('10000')
        return string

    # Button 29 -  Band 5 - Tolerance/Percentage 10%
    def clk29(self, string):
        self.le05.setText('10')
        return string

    # Button 30 - Band 6 - Temperature 25ppm/°C
    def clk30(self, string):
        self.le06.setText('25ppm/°C')
        return string

    # Green band
    # Button 31 - 1ª Band - Digit 5
    def clk31(self, string):
        self.le01.setText('5')
        return string

    # Button - 32 2ª Band - Digit 5
    def clk32(self, string):
        self.le02.setText('5')
        return string

    # Button 33 - Band 3 - Digit 5
    def clk33(self, string):
        self.le03.setText('5')
        return string

    # Button 34 - Band 4 - Multiplier x100.000
    def clk34(self, string):
        self.le04.setText('100000')
        return string

    # Button 35 - Band 5 - Tolerance/Percentage 0.50%
    def clk35(self, string):
        self.le05.setText('0.50')
        return string

    # Button 36 - Band 6 - Temperature 20ppm/°C
    def clk36(self, string):
        self.le06.setText('20ppm/°C')
        return string

    # Bue band
    # Button 37 - 1ª Band - Digit 6
    def clk37(self, string):
        self.le01.setText('6')
        return string

    # Button 37 - 2ª Band - Digit 6
    def clk38(self, string):
        self.le02.setText('6')
        return string

    # Button 39 - Band 3 - Digit 6
    def clk39(self, string):
        self.le03.setText('6')
        return string

    # Button 40 - Band 4 - Multiplier x1.000.000
    def clk40(self, string):
        self.le04.setText('1000000')
        return string

    # Button 41 - Band 5 - Tolerance/Percentage 0.25%
    def clk41(self, string):
        self.le05.setText('0.25')
        return string

    # Button 42 - Band 6 - Temperature 10ppm/°C
    def clk42(self, string):
        self.le06.setText('10ppm/°C')
        return string

    # Band lilás/roxo
    # Button 43 - 1ª Band - Digit 7
    def clk43(self, string):
        self.le01.setText('7')
        return string

    # Button 44 - 2ª Band - Digit 7
    def clk44(self, string):
        self.le02.setText('7')
        return string

    # Button  46 - Band 3 - Digit 7
    def clk45(self, string):
        self.le03.setText('7')
        return string

    # Button  46 - Band 4 - Multiplier x10.000.000
    def clk46(self, string):
        self.le04.setText('10000000')
        return string

    # Button 47 - Band 5 - Tolerance/Percentage 0.10%
    def clk47(self, string):
        self.le05.setText('0.10')
        return string

    # Button  48 - Band 6 - Temperature 5ppm/°C
    def clk48(self, string):
        self.le06.setText('5ppm/°C')
        return string

    # Grey band
    # Button 49 - 1ª Band - Digit 8
    def clk49(self, string):
        self.le01.setText('8')
        return string

    # Button 50 - 2ª Band - Digit 8
    def clk50(self, string):
        self.le02.setText('8')
        return string

    # Button 51 - Band 3 - Digit 8
    def clk51(self, string):
        self.le03.setText('8')
        return string

    # Button 52 - Band 4 - Multiplier x100.000.000
    def clk52(self, string):
        self.le04.setText('100000000')
        return string

    # Button 53 - Band 5 - Tolerance/Percentage N/A

    # Button 54 - Band 6 - Temperature 1ppm/°C
    def clk54(self, string):
        self.le06.setText('1ppm/°C')
        return string

    # White band
    # Button 55 - 1ª Band - Digit 9
    def clk55(self, string):
        self.le01.setText('9')
        return string

    # Button 56 - 2ª Band - Digit 9
    def clk56(self, string):
        self.le02.setText('9')
        return string

    # Button 57 - Band 3 - Digit 9
    def clk57(self, string):
        self.le03.setText('9')
        return string

    # Button 58 - Band 4 - Multiplier x1.000.000.000
    def clk58(self, string):
        self.le04.setText('1000000000')
        return string

    # Button 59 - Band 5 - Tolerance/Percentage 20%
    def clk59(self, string):
        self.le05.setText('20')
        return string

    # Button 60 - Band 6 - Temperature in °C - N/A
    # LineEdit checked

    # Calculation
    def calculo(self):
        valor = int(((self.le01.text()) + (self.le02.text()) + (self.le03.text())))
        total = valor * float(self.le04.text())
        vmax = total * float(self.le05.text())/100 + total
        vmin = total - (total * float(self.le05.text())/100)

        if total < 1000:
            self.le07.setText(str(f'{total:.2f}') + ' Ω')
            self.le08.setText(str(f'{vmax:.2f}') + ' Ω')
            self.le09.setText(str(f'{vmin:.2f}') + ' Ω')

        elif 1000 <= total < 1000000:
            self.le07.setText(str(f'{total/1000:.2f}') + ' KΩ')
            self.le08.setText(str(f'{vmax/1000:.2f}') + ' KΩ')
            self.le09.setText(str(f'{vmin/1000:.2f}') + ' KΩ')

        elif 1000000 <= total < 1000000000:
            self.le07.setText(str(f'{total/1000000:.2f}') + ' MΩ')
            self.le08.setText(str(f'{vmax/1000000:.2f}') + ' MΩ')
            self.le09.setText(str(f'{vmin/1000000:.2f}') + ' MΩ')

        elif total > 1000000000:
            self.le07.setText(str(f'{total/1000000000:.2f}') + ' GΩ')
            self.le08.setText(str(f'{vmax/1000000000:.2f}') + ' GΩ')
            self.le09.setText(str(f'{vmin/1000000000:.2f}') + ' GΩ')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Resistor = QtWidgets.QWidget()
    ui = Ui_Resistor()
    ui.setupUi(Resistor)
    Resistor.show()
    sys.exit(app.exec_())
