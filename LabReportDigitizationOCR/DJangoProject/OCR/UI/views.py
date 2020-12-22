from django.shortcuts import render, redirect
import pytesseract
import PIL
from .forms import *
from PIL import Image
from django.http import HttpResponse
from .models import User
import pymysql
# Create your views here.
def home(request):
    return render(request, 'img_upload.html');

def uploadImage(request):
    p = request.FILES['image']
    user = User(pic=p)
    user.save()
    return verify(request, p)

def verify(request,p):

    #converting image to string using tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(p))

    #string operations to extract numbers
    lst = text.split()
    index = []
    for i in range(len(lst)):
        if lst[i] == 'mg/dl':
            index.append(i)

    #saving data in list
    data = []
    for i in index:
        data.append(lst[i - 1])

    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    sql = """INSERT INTO ui_thyrocare(BUN, CS, UA, Ca) VALUES (%s,%s,%s,%s)"""
    try:
        cursor.execute(sql, data)
        db.commit()
    except:
        db.rollback()

    return render(request, 'verify.html', {'d0': data[0], 'd1': data[1], 'd2': data[2], 'd3': data[3]});



def update(request):

    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    id = max_id()

    if request.GET['de0'] != "":
        de0 = str(request.GET['de0'])
        sql = """UPDATE ui_thyrocare set BUN = %s where id = %s"""
        try:
            cursor.execute(sql, (de0, id))
            db.commit()
        except:
            db.rollback()

    else:
        sql = "SELECT BUN FROM ui_thyrocare where id = %s"
        try:
            cursor.execute(sql,id)
            results = cursor.fetchall()
        except:
            print("Error: unable to fecth data")

        de0 = results[0][0]

    if request.GET['de1'] != "":
        de1 = str(request.GET['de1'])
        sql = """UPDATE ui_thyrocare set CS = %s where id = %s"""
        try:
            cursor.execute(sql, (de1, id))
            db.commit()
        except:
            db.rollback()

    else:
        sql = "SELECT CS FROM ui_thyrocare where id = %s"
        try:
            cursor.execute(sql, id)
            results = cursor.fetchall()
        except:
            print("Error: unable to fecth data")

        de1 = results[0][0]


    if request.GET['de2'] != "":
        de2 = str(request.GET['de2'])
        sql = """UPDATE ui_thyrocare set UA = %s where id = %s"""
        try:
            cursor.execute(sql, (de2, id))
            db.commit()
        except:
            db.rollback()

    else:
        sql = "SELECT UA FROM ui_thyrocare where id = %s"
        try:
            cursor.execute(sql, id)
            results = cursor.fetchall()
        except:
            print("Error: unable to fecth data")

        de2 = results[0][0]

    if request.GET['de3'] != "":
        de3 = str(request.GET['de3'])
        sql = """UPDATE ui_thyrocare set Ca = %s where id = %s"""
        try:
            cursor.execute(sql, (de3, id))
            db.commit()
        except:
            db.rollback()

    else:
        sql = "SELECT Ca FROM ui_thyrocare where id = %s"
        try:
            cursor.execute(sql, id)
            results = cursor.fetchall()
        except:
            print("Error: unable to fecth data")

        de3 = results[0][0]

    return render(request, 'verify.html', {'d0': de0, 'd1': de1, 'd2': de2, 'd3': de3});



def max_id():

    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    sql = "SELECT max(id) FROM ui_thyrocare"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        print("Error: unable to fecth data")

    return results[0][0]