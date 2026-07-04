from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def long(ch):
    i=0
    for _ in ch:
        i+=1
    return i

def Horner(Z):
    M = 0
    while Z != "" :
        CH = Z[0]
        M = (M * 2 + int(CH)) % 7
        Z = Z[1:]
    return M
    
def Etape1(X):
    Y=""
    for i in range(long(X)-1, -1, -1):
        Y=str(int(X[i])%7) + Y
    return Y

def Etape2(Y):
    Z=""
    for i in range(long(Y)-1, -1, -2):
        Z= str(int(Y[i])%7) + Z
    return Z

def play():
    X = windows.X.setText()
    if not X.isdigit() or not (5 <= len(X) <= 20):
        windows.msg.setText("Veuillez saisir un nombre de 5 à 20 chiffres")
        return
    
    Y=Etape1(X)
    Z=Etape2(Y)
    h=Horner(Z)
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def long(ch):
    i=0
    for _ in ch:
        i+=1
    return i

def Horner(Z):
    M = 0
    while Z != "" :
        CH = Z[0]
        M = (M * 2 + int(CH)) % 7
        Z = Z[1:]
    return M
    
def Etape1(X):
    Y=""
    for i in range(long(X)-1, -1, -1):
        Y=str(int(X[i])%7) + Y
    return Y

def Etape2(Y):
    Z=""
    for i in range(long(Y)-1, -1, -2):
        Z= str(int(Y[i])%7) + Z
    return Z

def play():
    X = windows.X.toPlainText()
    if not X.isdigit() or not (5 <= len(X) <= 20):
        windows.msg.setText("Veuillez saisir un nombre de 5 à 20 chiffres")
        return
    
    Y=Etape1(X)
    Z=Etape2(Y)
    h=Horner(Z)
    if h == 0:
        windows.msg.setText(f"{X} est divisible par 7")
    else:
        windows.msg.setText(f"{X} n'est pas divisible par 7")
        
        
app = QApplication([])
windows = loadUi("InterfaceHorner.ui")
windows.show()
windows.bt1.clicked.connect(play)
app.exec_()