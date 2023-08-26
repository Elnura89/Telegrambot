import psycopg2
# .\myVirt\Scripts\activate

# try:
#     connection = psycopg2.connect(host='localhost',dbname='payments',user='postgres',password = '1234')
#     print('Успешно подключено')

#     cursor=connection.cursor()
#     id = input('Введите айди пользователя')
#     query=f'SELECT * FROM users WHERE id={id};'
#     cursor.execute(query)

#     users = cursor.fetchall()

#     for user in users:
#         print(user)


# except Exception as e:
#     print('Возникла ошибка')
#     print (e)
# finally:
#     if connection:
#         connection.close()


# try:
#     connection = psycopg2.connect(host='localhost',dbname='payments',user='postgres',password = '1234')
#     print('Успешно подключено')

#     cursor=connection.cursor()
#     x = input('Введите число')
#     y = input('Введите число') 
#     query=f'SELECT * FROM operations WHERE amount > {x} and amount < {y};'
#     cursor.execute(query)

#     users = cursor.fetchall()

#     for user in users:
#         print(user)


# except Exception as e:
#     print('Возникла ошибка')
#     print (e)
# finally:
#     if connection:
#         connection.close()

# try:
#     connection = psycopg2.connect(host='localhost',dbname='payments',user='postgres',password = '1234')
#     print('Успешно подключено')

#     cursor=connection.cursor()
#     name = input('Введите имя')
#     query='''
#     f"SELECT * from operations as o left join users as u on o.whom_to_send = u.id 
#     where u.fullname like '%{name}%';"
#     '''
#     cursor.execute(query)

#     users = cursor.fetchall()

#     for user in users:
#         print(user)


# except Exception as e:
#     print('Возникла ошибка')
#     print (e)
# finally:
#     if connection:
#         connection.close()

# try:
#     connection = psycopg2.connect(host='localhost',dbname='payments',user='postgres',password = '1234')
#     print('Успешно подключено')

#     cursor=connection.cursor()
#     id = input('Введите id')
#     query=f"SELECT * from operations where whom_to_send = {id};"
    
#     cursor.execute(query)

#     users = cursor.fetchall()

#     for user in users:
#         print(user)


# except Exception as e:
#     print('Возникла ошибка')
#     print (e)
# finally:
#     if connection:
#         connection.close()

import telebot

bot=telebot.TeleBot('6347051671:AAFAnooqolph_5i-7tKN3-WqAEv9oU17ee4')

# @bot.message_handler(commands=['getAll'])
# def start(message):
#     bot.send_message(message.from_user.id, 'Другая команда')

# bot.polling(none_stop=True, interval=0)


@bot.message_handler(commands=['getAll'])
def getAll(message):
    try:
        connection = psycopg2.connect(host = 'localhost',dbname = "chat",user = "postgres",password = "1234")
        print("Успешно подключено")

        cursor = connection.cursor()
        query = f"SELECT * FROM messages;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            bot.send_message(message.from_user.id, f"{row}")

    except Exception as e:
        print(f"Возникла ошибка {e}")
        print(e)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    try:
        connection = psycopg2.connect(host = 'localhost',dbname = "chat",user = "postgres",password = "1234")
        print("Успешно подключено")
    
        cursor = connection.cursor()
        query = f"insert into messages(text, userid) values('{message.text}', '{message.from_user.id}');"
        cursor.execute(query)
        connection.commit()

        cursor.execute("SELECT * FROM messages")
        rows = cursor.fetchall()
        bot.send_message(message.from_user.id, f"успешно сохранено")

        for row in rows:
            pass
    
    except Exception as e:
        print("Возникла ошибка")
        print(e)
    
bot.polling(none_stop=True, interval=0)