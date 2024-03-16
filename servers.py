from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def smth():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = []
    promotion_list.append('Человечество вырастает из детства.')
    promotion_list.append("Человечеству мала одна планета.")
    promotion_list.append('Мы сделаем обитаемыми безжизненные пока планеты.')
    promotion_list.append('И начнем с Марса!')
    promotion_list.append('Присоединяйся!')
    promotion_list.append('Я не хотел писать рекламу, меня заставили(')
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return f'''<title>Привет, Марс!</title>
               </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_planet.jpeg')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    Вот она какая, красная планета.
                  </body>
                </html>
               '''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')