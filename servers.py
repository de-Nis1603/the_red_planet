from flask import Flask, url_for, request

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


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars_planet.jpeg')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        Вот она какая, красная планета.
                        <div class="bg-warning text-dark">
                          Человечество вырастает из детства.
                        </div>
                        <div class="bg-success text-dark">
                          Человечеству мала одна планета.
                        </div>
                        <div class="bg-info text-dark">
                           Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="bg-secondary text-dark">
                          И начнем с Марса!
                        </div>
                        <div class='bg-success text-light'>
                          Присоединяйся!
                        </div>
                        <div class='bg-info text-muted'>
                          Для отключения рекламы оформите подписку :)
                        </div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', "GET"])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Отбор астронавтов</title>
                                  </head>
                                  <body>
                                    <h1>Анкета претендента на участие в миссии</h1>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                            <label for='form-control'></label>
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                            <div class="form-group">
                                                <label for="classSelect">Какое у Вас образование?</label>
                                                <select class="form-control" id="classSelect" name="education">
                                                  <option>Нет</option>
                                                  <option>Начальное</option>
                                                  <option>Среднее</option>
                                                  <option>Высшее</option>
                                                </select>
                                            </div>
                                            <label for='form-check'>Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name='job' value="Инженер-исследователь" id="flexCheckDefault">
                                              <label class="form-check-label" for="flexCheckDefault">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-group">
                                                <div class="form-check">
                                                  <input class="form-check-input" type="checkbox" name='job' value="Экзобиолог" id="flexCheckChecked">
                                                  <label class="form-check-label" for="flexCheckChecked">
                                                    Экзобиолог
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="checkbox" name='job' value="Инженер-строитель" id="flexCheckChecked">
                                                  <label class="form-check-label" for="flexCheckChecked">
                                                    Инженер-строитель
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="checkbox" name='job' value="Пилот драконов" id="flexCheckChecked">
                                                  <label class="form-check-label" for="flexCheckChecked">
                                                    Пилот драконов
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="checkbox" name='job' value="Метеоролог" id="flexCheckChecked">
                                                  <label class="form-check-label" for="flexCheckChecked">
                                                    Метеоролог
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="checkbox" name='job' value="Водитель марсохода" id="flexCheckChecked">
                                                  <label class="form-check-label" for="flexCheckChecked">
                                                    Водитель марсохода
                                                  </label>
                                                </div>
                                            </div>
                                            <label for='form-group'></label>
                                            <div class="form-group">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                  <label class="form-check-label" for="male">
                                                    Мужской
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                  <label class="form-check-label" for="female">
                                                    Женский
                                                  </label>
                                                </div>
                                            </div>
                                            <label for='about'></label>
                                            <div class="form-group">
                                                <label for="about">Мотивация</label>
                                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                            </div>
                                            <label for='photo'></label>
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <label for='photo'></label>
                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Готов статься на Марсе</label>
                                            </div>
                                            <button type="submit" class="btn btn-primary">Записаться</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('job'))
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return 'Форма отправлена, вылет завтра:)'
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')