from flask import Flask, render_template
from models.users import RegisterForm
import os

app = Flask('__name__')
app.config['SECRET_KEY'] = 'ryslan2003noob'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('index.html', form=form, massege_phone='Некорректный телефон')

        return render_template('index.html', form=form)

    except BaseException:
        print("home/error/try1")
        return render_template('index.html', form=form)


@app.route("/Поиск_фабрик_и_поставщиков", methods=['GET', 'POST'])
def Поиск_фабрик_и_поставщиков():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('public/Поиск_фабрик_и_поставщиков.html', form=form,
                                       massege_phone='Некорректный телефон')

        return render_template('public/Поиск_фабрик_и_поставщиков.html', form=form)

    except BaseException:
        print("public/error/try1")
        return render_template('public/Поиск_фабрик_и_поставщиков.html', form=form)


@app.route("/Доставка_грузов_в_Вашу_страну", methods=['GET', 'POST'])
def Доставка_грузов_в_Вашу_страну():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('public/Доставка_грузов_в_Вашу_страну.html', form=form,
                                       massege_phone='Некорректный телефон')

        return render_template('public/Доставка_грузов_в_Вашу_страну.html', form=form)

    except BaseException:
        print("public/error/try1")
        return render_template('public/Доставка_грузов_в_Вашу_страну.html', form=form)


@app.route("/Контроль_качества", methods=['GET', 'POST'])
def Контроль_качества():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('public/Контроль_качества.html', form=form,
                                       massege_phone='Некорректный телефон')

        return render_template('public/Контроль_качества.html', form=form)

    except BaseException:
        print("public/error/try1")
        return render_template('public/Контроль_качества.html', form=form)


@app.route("/Онлайн_посещение_фабрики", methods=['GET', 'POST'])
def Онлайн_посещение_фабрики():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('public/Онлайн_посещение_фабрики.html', form=form,
                                       massege_phone='Некорректный телефон')

        return render_template('public/Онлайн_посещение_фабрики.html', form=form)

    except BaseException:
        print("public/error/try1")
        return render_template('public/Онлайн_посещение_фабрики.html', form=form)


@app.route("/Производство_в_Китае", methods=['GET', 'POST'])
def Производство_в_Китае():
    form = RegisterForm()
    try:
        if form.validate_on_submit():
            if len(form.phone.data) != 11:
                return render_template('public/Производство_в_Китае.html', form=form,
                                       massege_phone='Некорректный телефон')

        return render_template('public/Производство_в_Китае.html', form=form)

    except BaseException:
        print("public/error/try1")
        return render_template('public/Производство_в_Китае.html', form=form)



@app.errorhandler(400)
def not_found_error(error):
    pass
    # return render_template('Error/400.html'), 400


@app.errorhandler(401)
def not_found_error(error):
    pass
    # return render_template('Error/401.html'), 401


@app.errorhandler(404)
def not_found_error(error):
    print("ЛОЛ ОШИБКА 404, СРОЧНО В ДУРКУ")
    return render_template('404/404.html'), 404


@app.errorhandler(500)
def not_found_error(error):
    pass
    # return render_template('Error/500.html'), 500


@app.errorhandler(502)
def not_found_error(error):
    pass
    # return render_template('Error/502.html'), 502


@app.errorhandler(503)
def not_found_error(error):
    pass
    # return render_template('Error/503.html'), 503


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
