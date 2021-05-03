import telebot
import pandas as pd
from  sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

s=[]

bot = telebot.TeleBot("1705764199:AAEw-ErNuDJU5kEy0JitwFo6lKwqAEqovtk")
l1 =['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain',
     'acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
     'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
     'irregular_sugar_level','cough,high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache'
    ,'yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','боль в спине','констипация(запор)',
     'боль в животе','диарея','слабая лихорадка','урина желтого цвета','желтые глаза','острая печеночная недостаточность'
    ,'гиповолемия','вздутие живота','увеличенные лимфатические узлы','усталость','туман в глазах','мокрота','раздражение в горле',
     'красные глаза','гайморит','насморк','заложенность носа','боль в груди','слабость в руках и ногах','учащенное сердцебиение'
    ,'боль при дефекации','боль в заднем проходе','кровь в стуле','раздражение в анусе','боль в шее','головокружение',
     'судороги','синяки','ожирение','опухшие ноги','васкулит(воспаленные сосуды)','опухшее лицо','увеличенная щитовидная железа'
    ,'ломкие ногти','отек рук и ног','повышенное чувство голода','extra_marital_contacts','сухость и покалывание губ',
     'невнятная речь','боль в колене','боль в тазобедренном суставе','мышечная слабость','зажатость мышц шеи','опухшие суставы',
     'cкованность движений (мышечная ригидность)','головокружение','потеря равновесия','неустойчивость','слабость на одной стороне тела',
     'потеря обоняния','дискомфорт в мочевом пузыре','неприятный запах мочи','постоянное ощущение мочи','метеоризм','внутренний зуд',
     'сыпь','депрессия','раздражительность','мышечная боль','нарушение чувствительности','красные пятна по всему телу',
     'боль в животе','ненормальные менструации','дисхромные пятна','слезотечение глаз','повышенный аппетит','полиурия','семейный анамнез',
     'слизистая мокрота','ржавая мокрота','отсутствие концентрации','нарушение зрения','переливание крови','получение нестерильных инъекций',
     'кома','желудочное кровотечение','вздутие живота','употребление алкоголя в анамнезе','перегрузка жидкостью','кровь в мокроте',
     'выступающие вены на икре','сердцебиение','болезненная ходьба','гнойные прыщи','черные точки','шелушение','шелушение кожи',
     'серебристая пыль','небольшие вмятины на ногтях','воспалительные процессы в ногтях','волдыри','красная рана вокруг носа',
     'желтая корка','prognosis']
l3=['боль в спине','констипация(запор)','боль в животе','диарея','слабая лихорадка','урина желтого цвета',
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
'желтая корка', 'itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering,chills','joint_pain','stomach_pain',
'acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever',
'sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea,loss_of_appetite',
'pain_behind_the_eyes','sunken_eyes','breathlessness','sweating']


l2=[]
for x in range(0,len(l1)):
    l2.append(0)

print("Ready")

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/start', '/stop')
    for i in range(38, 84, 3):
        j = i
        user_markup.row(l1[j-2], l1[j-1], l1[j])
    #bot.send_message(message.from_user.id, 'Hi! This is a disease predictor. You can choose one or few symptoms and get the diagnose that you may have. WARNING! This is not a diagnose of a doctor, this bot is created using machine learning algorithms. You will have to visit a doctor anyway!', reply_markup=user_markup)
    bot.send_message(message.from_user.id, 'Привет! Этот бот создан для предварительного определения диагноза по симптомам. Выбери симптомы и нажми "stop" для получения диагноза. Внимание! Данное приложение использует алгоритмы машинного обучения для определения диагноза. Для точного диагноза Вам необходимо обратиться к врачу!', reply_markup=user_markup)

#def send_welcome(message):
#    bot.reply_to(message, "Hi! This is a disease predictor. You can choose one or few symptoms and get the diagnose that you may have. WARNING! This is not a diagnose of a doctor, this bot is created using machine learning algorithms. You will have to visit doctor anyway!")

def prediction():
    STrain_Data = pd.read_csv('Training.csv')

    STest_Data = pd.read_csv('Testing.csv')

    X = STrain_Data.drop(columns=["prognosis"]).dropna(axis=1, how='any', thresh=None, subset=None, inplace=False)
    y = STrain_Data["prognosis"]

    X_test = STest_Data.drop(columns=["prognosis"])
    y_test = STest_Data["prognosis"]

    # Model train
    model = DecisionTreeClassifier()
    model.fit(X, y)

    # Prediction
    Prediction = model.predict(X_test)
    #print(X_test)

    # Accuracy
    accuracy = accuracy_score(Prediction, y_test)
    print("accuracy: " + format(accuracy))
    return model

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    if s==[]:
        print('Empty')

    # Read data
    else:
        print(s)
        model = prediction()

        for k in range(0, len(l1)):
            # print (k,)
            for z in s:
                if (z == l1[k]):
                    l2[k] = 1
        inputtest = [l2]
        predict = model.predict(inputtest)
        predicted = predict[0]
        s.clear()
        print(predicted)
        bot.reply_to(message, predicted)


@bot.message_handler(func=lambda m: True)
def get_symptoms(message):
    s.append(message.text)
    print(s)
    #bot.reply_to(message, message.text)


bot.polling()

