import hashlib
import os
import  sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.deger =  QtWidgets.QLineEdit()
        self.wordlist = QtWidgets.QPushButton("Wordlist Seçiniz")
        self.giris = QtWidgets.QPushButton("Deger Girin")
        self.md5_buton = QtWidgets.QRadioButton("MD5")
        self.md4_buton = QtWidgets.QRadioButton("MD4")
        self.sha1_buton = QtWidgets.QRadioButton("SHA1")
        self.sha256_buton = QtWidgets.QRadioButton("SHA256")
        self.sha512_buton = QtWidgets.QRadioButton("SHA512")
        self.sha3_512_buton = QtWidgets.QRadioButton("SHA3-512")
        self.sayac = 0


        self.yazi_alani = QtWidgets.QLabel("")
        self.wordlist_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.deger)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.wordlist)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.md5_buton)
        v_box.addWidget(self.md4_buton)
        v_box.addWidget(self.sha1_buton)
        v_box.addWidget(self.sha256_buton)
        v_box.addWidget(self.sha512_buton)
        v_box.addWidget(self.sha3_512_buton)



        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Hash_CrackerN")


        self.wordlist.clicked.connect(lambda : self.dosya_ac())
        self.giris.clicked.connect(
            lambda: self.click(self.md5_buton.isChecked(), self.md4_buton.isChecked(), self.sha1_buton.isChecked(), self.sha256_buton.isChecked(),self.sha512_buton.isChecked(),self.sha3_512_buton.isChecked(),self.yazi_alani))

        self.show()



    def dosya_ac(self):
        self.dosya_isim = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        with open("wordlist.txt", "r") as self.file:
            self.yazi_alani.setText("Wordlist Yüklendi")

    def click(self,md5_buton,md4_buton,sha1_buton,sha256_buton,sha512_buton,sha3_512_buton,yazi_alani):

        if md5_buton:
            hash_input = self.deger.text().lower()
            with open(self.dosya_isim[0], "r") as file:

                for i in file.read().split("\n"):
                    print(i)
                    if i == "\n":
                        pass
                    else:
                        hashli_i = hashlib.md5(i.encode('utf-8')).hexdigest()
                        print(hashli_i)
                    if hashli_i == hash_input:
                        self.yazi_alani.setText(
                            "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")

        if md4_buton:
                hash_input = self.deger.text().lower()
                with open(self.dosya_isim[0], "r") as file:

                    for i in file.read().split("\n"):
                        if i == "\n":
                            pass
                        else:
                            hashli_i = hashlib.new('md4', i.encode('utf-8')).hexdigest()
                            print(hashli_i)
                        if hashli_i == hash_input:

                            self.yazi_alani.setText(
                                "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")


        if sha1_buton:
            hash_input = self.deger.text().lower()
            with open(self.dosya_isim[0], "r") as file:

                for i in file.read().split("\n"):
                    if i == "\n":
                        pass
                    else:
                        hashli_i = hashlib.sha1(i.encode("utf-8")).hexdigest()
                        print(hashli_i)
                    if hashli_i == hash_input:
                        self.yazi_alani.setText(
                            "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")
        if sha256_buton:
            hash_input = self.deger.text().lower()
            with open(self.dosya_isim[0], "r") as file:

                for i in file.read().split("\n"):
                    if i == "\n":
                        pass
                    else:
                        hashli_i = hashlib.sha256(i.encode("utf-8")).hexdigest()
                        print(hashli_i)
                    if hashli_i == hash_input:
                        self.yazi_alani.setText(
                            "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")
        if sha512_buton:
            hash_input = self.deger.text().lower()
            with open(self.dosya_isim[0], "r") as file:

                for i in file.read().split("\n"):
                    if i == "\n":
                        pass
                    else:
                        hashli_i = hashlib.sha512(i.encode("utf-8")).hexdigest()

                    if hashli_i == hash_input:
                        self.yazi_alani.setText(
                            "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")
        if sha3_512_buton:
            hash_input = self.deger.text().lower()
            with open(self.dosya_isim[0], "r") as file:

                for i in file.read().split("\n"):
                    if i == "\n":
                        pass
                    else:
                        hashli_i = hashlib.sha3_512(i.encode("utf-8")).hexdigest()
                        print(hashli_i)
                    if hashli_i == hash_input:
                        self.yazi_alani.setText(
                            "******************************\nHash: " + hash_input + "\nSonuç: " + i + "\n******************************")





app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
