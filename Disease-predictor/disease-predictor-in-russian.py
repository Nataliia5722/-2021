from tkinter import *
import numpy as np
import pandas as pd
from tkinter.messagebox import showinfo
# from gui_stuff import *


l1=['боль в спине','констипация(запор)','боль в животе','диарея','слабая лихорадка','урина желтого цвета',
'желтые глаза','острая печеночная недостаточность','гиповолемия','вздутие живота',
'увеличенные лимфатические узлы','усталость','туман в глазах','мокрота','раздражение в горле',
'красные глаза','гайморит','насморк','заложенность носа','боль в груди','слабость в руках и ногах',
'учащенное сердцебиение','боль при дефекации','боль в заднем проходе','кровь в стуле',
'раздражение в анусе','боль в шее','головокружение','судороги','синяки','ожирение','опухшие ноги',
'васкулит(воспаленные сосуды)','опухшее лицо','увеличенная щитовидная железа','ломкие ногти',
'отек рук и ног','повышенное чувство голода','сухость и покалывание губ',
'невнятная речь','боль в колене','боль в тазобедренном суставе','мышечная слабость','зажатость мышц шеи','опухшие суставы',
'cкованность движений (мышечная ригидность)','головокружение', 'потеря равновесия', 'неустойчивость',
'слабость на одной стороне тела', 'потеря обоняния', 'дискомфорт в мочевом пузыре', 'неприятный запах мочи',
'постоянное ощущение мочи', 'метеоризм', 'внутренний зуд', 'сыпь',
'депрессия', 'раздражительность', 'мышечная боль', 'нарушение чувствительности', 'красные пятна по всему телу', 'боль в животе',
'ненормальные менструации', 'дисхромные пятна','слезотечение глаз','повышенный аппетит','полиурия','семейный анамнез','слизистая мокрота',
'ржавая мокрота', 'отсутствие концентрации', 'нарушение зрения', 'переливание крови',
'получение нестерильных инъекций', 'кома', 'желудочное кровотечение', 'вздутие живота',
'употребление алкоголя в анамнезе', 'перегрузка жидкостью', 'кровь в мокроте', 'выступающие вены на икре',
'сердцебиение', 'болезненная ходьба', 'гнойные прыщи', 'черные точки', 'шелушение', 'шелушение кожи',
'серебристая пыль', 'небольшие вмятины на ногтях', 'воспалительные процессы в ногтях', 'волдыри', 'красная рана вокруг носа',
'желтая корка']

disease=['Грибковые инфекции','Аллергия','Гастроэзофагеальный рефлюкс','Хронический холестаз','Реакция на лекарства',
'Язвенная болезнь','ВИЧ','Сахарный диабет','Гастроэнтерит','Бронхиальная астма','Гипертония',
' Мигрень','Шейный спондилез',
'Паралич (кровоизлияние в мозг)','Желтуха','Малярия','Ветряная оспа','Тропическая лихорадка','Брюшной тиф','Гепатит A',
'Гепатит B','Гепатит C','Гепатит D','Гепатит E','Алкогольный гепатит','Туберкулез',
'Простуда','Пневмония','Геморрой',
'Острое сердечно-сосудистое заболевание','Варикозное расширение вен','Гипотиреоз','Гипотиреоз2','Гипогликемия','Остеоартроз',
'Артрит','(головокружение) Пароксизмальное позиционное головокружение','Угревая сыпь','Инфекция мочевыводящих путей','Псориаз',
'Импетиго']
#

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27, 'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)
# df.replace({'prognosis':{'Грибковые инфекции':0,'Аллергия':1,'Гастроэзофагеальный рефлюкс':2,'Хронический холестаз':3,'Реакция на лекарства':4,
# 'Язвенная болезнь':5,'ВИЧ':6,'Сахарный диабет':7,'Гастроэнтерит':8,'Бронхиальная астма':9,'Гипертония':10,
# 'Мигрень':11,'Шейный спондилез':12,
# 'Паралич (кровоизлияние в мозг)':13,'Желтуха':14,'Малярия':15,'Ветряная оспа':16,'Тропическая лихорадка':17,'Брюшной тиф':18,'Гепатит A':19,
# 'Гепатит B':20,'Гепатит C':21,'Гепатит D':22,'Гепатит E':23,'Алкогольный гепатит':24,'Туберкулез':25,
# 'Простуда':26,'Пневмония':27,'Геморрой':28,'Острое сердечно-сосудистое заболевание':29,'Варикозное расширение вен':30,'Гипотиреоз':31,
# 'Гипотиреоз2':32,'Гипогликемия':33,'Остеоартроз':34,'Артрит':35,
# '(головокружение) Пароксизмальное позиционное головокружение':36,'Угревая сыпь':37,'Инфекция мочевыводящих путей':38,'Псориаз':39,
# 'Импетиго':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
#y=y.astype('int')
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------


class ListBoxChoice(object):
    def __init__(self, master=None, title=None, message=None, list=[]):
        self.master = master
        self.value = None
        self.list = list[:]

        self.modalPane = Toplevel(self.master)
        self.modalPane.geometry("%dx%d%+d%+d" % (400, 300, 250, 125))

        self.modalPane.transient(self.master)
        self.modalPane.grab_set()

        self.modalPane.bind("<Return>", self._choose)
        self.modalPane.bind("<Escape>", self._cancel)

        if title:
            self.modalPane.title(title)

        if message:
            Label(self.modalPane, text=message).pack(padx=5, pady=5)

        listFrame = Frame(self.modalPane)
        listFrame.pack(side=TOP, padx=5, pady=5)

        scrollBar = Scrollbar(listFrame)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.listBox = Listbox(listFrame, width=80, selectmode=SINGLE)
        self.listBox.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scrollBar.set)
        self.list.sort()
        for item in self.list:
            self.listBox.insert(END, item)

        buttonFrame = Frame(self.modalPane)
        buttonFrame.pack(side=BOTTOM)

        chooseButton = Button(buttonFrame, text="Выбрать", command=self._choose)
        chooseButton.pack()

        cancelButton = Button(buttonFrame, text="Отмена", command=self._cancel)
        cancelButton.pack(side=RIGHT)

    def _choose(self, event=None):
        try:
            firstIndex = self.listBox.curselection()[0]
            self.value = self.list[int(firstIndex)]
        except IndexError:
            self.value = None
        self.modalPane.destroy()

    def _cancel(self, event=None):
        self.modalPane.destroy()

    def returnValue(self):
        self.master.wait_window(self.modalPane)
        return self.value

def popup_showinfo():
    showinfo("ShowInfo", "Введите имя!")


def choose_symptom1():
    returnValue = ListBoxChoice(root, "Выбор симптома", "Выберите один симптом",
                                    l1).returnValue()
    S1En.config(text=returnValue)
    return returnValue

def choose_symptom2():
    returnValue = ListBoxChoice(root, "Выбор симптома", "Выберите один симптом",
                                    l1).returnValue()
    S2En.config(text=returnValue)
    return returnValue
def choose_symptom3():
    returnValue = ListBoxChoice(root, "Выбор симптома", "Выберите один симптом",
                                    l1).returnValue()
    S3En.config(text=returnValue)
    return returnValue
def choose_symptom4():
    returnValue = ListBoxChoice(root, "Выбор симптома", "Выберите один симптом",
                                    l1).returnValue()
    S4En.config(text=returnValue)
    return returnValue

def choose_symptom5():
    returnValue = ListBoxChoice(root,"Выбор симптома", "Выберите один симптом",
                                    l1).returnValue()
    S5En.config(text=returnValue)
    return returnValue

def DecisionTree():
    if NameEn.get()=="":
        print(NameEn.get()+"Напишите свое имя!")
        popup_showinfo()
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.title("Постановка дивагноза по симптомам пациента")
#root.configure(background='')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

# Heading

w2 = Label(root, justify=CENTER, text="Постановка дивагноза по симптомам пациента")
w2.config(font=("Aharoni", 20))
w2.grid(row=1, column=0, columnspan=2, padx=100)
# labels
NameLb = Label(root, text="Имя пациента")
NameLb.grid(row=6, column=1, pady=15, sticky=W)


S1Lb = Label(root, text="Симптом 1")
S1Lb.grid(row=7, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="Симптом 2")
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="Симптом 3")
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root, text="Симптом 4")
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root, text="Симптом 5")
S5Lb.grid(row=11, column=1, pady=10, sticky=W)


lrLb = Label(root, text="Дерево решений")
lrLb.grid(row=15, column=1, pady=10,sticky=W)

destreeLb = Label(root, text="Случайный лес")
destreeLb.grid(row=17, column=1, pady=10, sticky=W)

ranfLb = Label(root, text="Байес")
ranfLb.grid(row=19, column=1, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)


S1En = Button(root, text="Выбрать", command=choose_symptom1)
S1En.config(width=25)
S1En.grid(row=7, column=1)

S2En = Button(root, text="Выбрать", command=choose_symptom2)
S2En.config(width=25)
S2En.grid(row=8, column=1)

S3En = Button(root, text="Выбрать", command=choose_symptom3)
S3En.config(width=25)
S3En.grid(row=9, column=1)

S4En = Button(root, text="Выбрать", command=choose_symptom4)
S4En.config(width=25)
S4En.grid(row=10, column=1)

S5En = Button(root, text="Выбрать", command=choose_symptom5)
S5En.config(width=25)
S5En.grid(row=11, column=1)

dst = Button(root, text="Дерево решений", command=DecisionTree,bg="green",fg="yellow")
dst.grid(row=8, column=3)

rnf = Button(root, text="Случайный лес", command=randomforest,bg="green",fg="yellow")
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text="Классификатор Байеса", command=NaiveBayes,bg="green",fg="yellow")
lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="orange",fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="orange",fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="orange",fg="black")
t3.grid(row=19, column=1 , padx=10)

root.mainloop()
