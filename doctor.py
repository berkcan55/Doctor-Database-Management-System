from PyQt5 import QtWidgets
from DoctorOfficeMainWindow import Ui_MainWindow
import sys
import mysql.connector
from datetime import datetime
from PyQt5.QtCore import QDate
import calendar


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.registerPatient)
        self.ui.pushButton_2.clicked.connect(self.searchPatient)
        self.ui.pushButton_4.clicked.connect(self.searchforupdate)
        self.ui.pushButton_3.clicked.connect(self.updatePatient)
        self.ui.pushButton_5.clicked.connect(self.save)

    
    def registerPatient(self):
        def insertpatient(id,name,surname,age,gender,phone,address,chronic,drug):
            connection = mysql.connector.connect(host="localhost",user="root",password="12345678",database="doctor_db")
            mycursor=connection.cursor()
            sql="INSERT INTO patient(id,name,surname,age,gender,phone,address,chronic,drug) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (id,name,surname,age,gender,phone,address,chronic,drug)
            mycursor.execute(sql,values)
            try:
                connection.commit()
                print(f'{mycursor.rowcount} tane kayıt eklendi')
            except mysql.connector.Error as err:
                print("hata",err)
            finally:
                connection.close()
                print("database baglantısı tamamlandı")

        id=self.ui.lineEdit.text()
        name=self.ui.lineEdit_2.text()
        surname=self.ui.lineEdit_3.text()
        age=self.ui.Age.text()
        if(self.ui.radioButton.isChecked()==True):
            gender="M"
        elif(self.ui.radioButton_2.isChecked()==True):
            gender="F"
        else:
            gender="O"        
        phone=self.ui.lineEdit_4.text()
        address=self.ui.textEdit.toPlainText()
        chronic=""
        drug=""
        for i in range(20):
            try:
                chronic+=self.ui.tableWidget_3.takeItem(i,0).text() + ","
                drug+=self.ui.tableWidget_5.takeItem(i,0).text() + ","
            except:
                pass
        chronic=chronic[:-1]
        drug=drug[:-1]
        insertpatient(id,name,surname,age,gender,phone,address,chronic,drug)   
    

    def searchPatient(self):
        def getproduct(id):
            connection = mysql.connector.connect(host="localhost",user="root",password="12345678",database="doctor_db")
            mycursor=connection.cursor()
            sql ="SELECT * from patient join prescription on prescription.patientid=patient.id where prescription.patientid=%s"
            params = (id,)
            mycursor.execute(sql,params)
            #cursor.execute('SELECT * from node_app where id=3')
            result=mycursor.fetchone()
            id=result[0]
            name=result[1]
            surname=result[2]
            age=result[3]
            gender=result[4]
            phone=result[5]
            address=result[6]
            chronic=result[7].split(',')
            drug=result[8].split(',')
            drugid=result[9]
            sickness=result[10].split(',')
            drugname=result[11].split(',')
            date=result[15]
            note=result[16]
            for i in range(0,7):
                item=QtWidgets.QTableWidgetItem(str(result[i]))
                self.ui.tableWidget.setItem(i-1,1,item)
            for i in range(0,20):
                try:
                    c=QtWidgets.QTableWidgetItem(str(chronic[i]))
                    self.ui.tableWidget_7.setItem(i,0,c)
                except:
                    pass    
                try:    
                    d=QtWidgets.QTableWidgetItem(str(drug[i]))
                    self.ui.tableWidget_8.setItem(i,0,d)
                except:
                    pass
                try:
                    s=QtWidgets.QTableWidgetItem(str(sickness[i]))
                    g=QtWidgets.QTableWidgetItem(str(drugname[i]))
                    e=QtWidgets.QTableWidgetItem(str(date))
                    self.ui.tableWidget_2.setItem(i,0,s)
                    self.ui.tableWidget_2.setItem(i,1,g)
                    self.ui.tableWidget_2.setItem(i,2,e)

                except:
                    pass 
            self.ui.textEdit_2.setText(note)





        a=self.ui.lineEdit_10.text()
        getproduct(a)



    def searchforupdate(self):
        def getproduct(id):
            connection = mysql.connector.connect(host="localhost",user="root",password="12345678",database="doctor_db")
            mycursor=connection.cursor()
            sql ="SELECT * from patient join prescription on prescription.patientid=patient.id where prescription.patientid=%s"
            params = (id,)
            mycursor.execute(sql,params)
            #cursor.execute('SELECT * from node_app where id=3')
            result=mycursor.fetchone()
            id=result[0]
            name=result[1]
            surname=result[2]
            age=result[3]
            gender=result[4]
            phone=result[5]
            address=result[6]
            chronic=result[7].split(',')
            drug=result[8].split(',')
            note=result[16]
            for i in range(0,7):
                item=QtWidgets.QTableWidgetItem(str(result[i]))
                self.ui.tableWidget_6.setItem(i-1,1,item)
            for i in range(0,20):
                try:
                    c=QtWidgets.QTableWidgetItem(str(chronic[i]))
                    self.ui.tableWidget_9.setItem(i,0,c)
                except:
                    pass    
                try:    
                    d=QtWidgets.QTableWidgetItem(str(drug[i]))
                    self.ui.tableWidget_10.setItem(i,0,d)
                except:
                    pass
            self.ui.textEdit_3.setText(note)





        a=self.ui.lineEdit_11.text()
        getproduct(a)


        
    def updatePatient(self):
        def getupdate(id,name,surname,age,gender,phone,adress,chronic,drug):
            connection = mysql.connector.connect(host="localhost",user="root",password="12345678",database="doctor_db")
            mycursor=connection.cursor()
            sql= "UPDATE patient SET name= %s, surname= %s, age= %s, gender= %s, phone= %s, address= %s, chronic= %s, drug= %s WHERE id= %s"
            values= (name,surname,age,gender,phone,adress,chronic,drug,id)
            mycursor.execute(sql, values)
            try:
                connection.commit()
                print(f'{mycursor.rowcount} tane kayıt güncellendi')
            except mysql.connector.Error as err:
                print("hata",err)
            finally:
                connection.close()
                print("database baglantısı tamamlandı")
        try:
            a=self.ui.tableWidget_6.takeItem(-1,1).text()
            name=self.ui.tableWidget_6.takeItem(0,1).text()
            surname=self.ui.tableWidget_6.takeItem(1,1).text()
            age=self.ui.tableWidget_6.takeItem(2,1).text()
            gender=self.ui.tableWidget_6.takeItem(3,1).text()
            phone=self.ui.tableWidget_6.takeItem(4,1).text()
            adress=self.ui.tableWidget_6.takeItem(5,1).text()
        except:
            pass
        chronic=""
        drug=""
        for i in range(20):
            try:
                chronic+=self.ui.tableWidget_7.takeItem(i,0).text() + ","
                drug+=self.ui.tableWidget_8.takeItem(i,0).text() + ","
            except:
                pass
        chronic=chronic[:-1]
        drug=drug[:-1]
        getupdate(a,name,surname,age,gender,phone,adress,chronic,drug)   

    def save(self):

        def insertprescription(sickness,drugname,quantity,frequecy,number,date,note,patientid):
            connection = mysql.connector.connect(host="localhost",user="root",password="12345678",database="doctor_db")
            mycursor=connection.cursor()
            sql="INSERT INTO prescription(sickness,drugName,Quantity,Frequency,Number,Date,Note,Patientid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (sickness,drugname,quantity,frequecy,number,date,note,patientid)
            mycursor.execute(sql,values)
            try:
                connection.commit()
                print(f'{mycursor.rowcount} tane kayıt eklendi')
            except mysql.connector.Error as err:
                print("hata",err)
            finally:
                connection.close()
                print("database baglantısı tamamlandı")

        patientid=self.ui.lineEdit_5.text()
        sickness=''
        drugname=''
        quantity=''
        frequecy=''
        number=''  
        for i in range(10):
            try:
                sickness+=self.ui.tableWidget_4.takeItem(i,0).text() + ','
                drugname+=self.ui.tableWidget_4.takeItem(i,1).text() + ','
                quantity+=self.ui.tableWidget_4.takeItem(i,2).text() + ','
                frequecy+=self.ui.tableWidget_4.takeItem(i,3).text() + ','
                number+=self.ui.tableWidget_4.takeItem(i,4).text() + ','
            except:
                pass
        sickness=sickness[:-1]
        drugname=drugname[:-1]
        quantity=quantity[:-1]
        frequecy=frequecy[:-1]
        number=number[:-1]    
        date=self.ui.calendarWidget.selectedDate().toString('dd-MM-yyyy')
        date=datetime.strptime(date,'%d-%m-%Y')
        note=self.ui.textEdit_5.toPlainText()
        print(date)
        print(note)
        insertprescription(sickness,drugname,quantity,frequecy,number,date,note,patientid)




def app():
    app= QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())


app()