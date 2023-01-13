from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = "5877249040:AAEUVCkLpfF6zRSufwFk6reuGMWMsjlyu10"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




illneses = {
    'Альтернариоз и сухая пятнистость' : ['Коричневые пятна на листьях или темнеют их края'],
    'Антракноз' : ['Коричневые пятна на листьях или темнеют их края','Желтеют листья'],
    'Аскохитоз' : ['Коричневые пятна на листьях или темнеют их края','Хризантемы'],
    'Мучнистая роса': ['Мучнистые пятна на листьях'],
    'Серая гниль': ['Пушистый сероватый налет'],
    'Ржавчина листьев': ['Желтые пятна'],
    'Филлостикоз': ['Желтеют листья','Коричневые пятна на листьях или темнеют их края']
}


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    global chosen_symps
    chosen_symps = []
    global buttons_global
    buttons_global = buttons_global = ['Сансевьера','Фиалка','Гиппераструм','Калла','Бегония','Кактус','Фикус','Гибискус','Алоэ']
    global symptoms_global
    symptoms_global = ['Желтые пятна','Коричневые пятна на листьях или темнеют их края','Скрученные листья','Желтеют листья','Мучнистые пятна на листьях','Пушистый сероватый налет','Закончить выбор']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    buttons = ['Орхидея','Сансевьера','Фиалка','Гиппераструм','Калла','Бегония','Кактус','Фикус','Гибискус','Алоэ','Хризантемы','Другое']
    keyboard.add(*buttons)
    await message.answer("Выберите ваше домашнее растение", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in buttons_global or message.text in symptoms_global and message.text != 'Закончить выбор')
async def button_reply(message: types.Message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    buttons1 = symptoms_global
    keyboard1.add(*buttons1)
    '''for k in range(len(symptoms_global)-1):
        if symptoms_global[k] == message.text:
            symptoms_global.pop(k)
            time.sleep(0.1)
            print(symptoms_global)'''
    if message.text in chosen_symps:
        chosen_symps.remove(message.text)
    elif message.text in symptoms_global and message.text != 'Закончить выбор':
        chosen_symps.append(str(message.text))
        print("Выбранные симптомы",chosen_symps)
    await message.answer("Выберите симптомы \n \n Выбранные симптомы: {0} \n \n (Чтобы убрать симптом из списка, выберите его еще раз)".format(', '.join(chosen_symps)), reply_markup=keyboard1)

@dp.message_handler(lambda message: message.text == 'Закончить выбор')
async def end_choice_reply(message: types.Message):
    global schet
    schet = [0] * len(illneses.keys())
    keyboard_finale = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons1 = []
    keyboard_finale.add(*buttons1)
    for k in chosen_symps:
        for l in illneses.values():
            if k in l:
                schet[list(illneses.values()).index(l)] += 1
    bolezni = []
    final_bolezni = []
    max_symptoms = -1
    for i in range(len(schet)):
        if schet[i] > max_symptoms:
            bolezni = []
            max_symptoms = schet[i]
            bolezni.append(i)
            print(bolezni,"типо победители")
        elif schet[i] == max_symptoms:
            bolezni.append(i)
            print(bolezni,"типо победители")
    print(schet)
    for m in range(len(bolezni)):
        final_bolezni.append(list(illneses.keys())[bolezni[m]])
    print(final_bolezni,"Болезни")
    await message.answer('Скорее всего, у вас что-то из этого: \n \n{0}'.format(', '.join(final_bolezni)), reply_markup=types.ReplyKeyboardRemove())





if __name__ == '__main__':
    executor.start_polling(dp)