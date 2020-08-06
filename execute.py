from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import db


app = Flask(__name__)

# 라우터 주소 함께 사용 : /, /country_list
@app.route('/')
# DB 테이블의 레코드 반환후 html 파일로 레코드 총수와 함께 전달 
@app.route('/country_list')
def country_list() :
    country_list = db.get_country_list()
    return render_template('index_countryList.html', country_list=country_list, totalcount = len(country_list))

@app.route('/country/<no>')
def country(no):
    temp_dic = db.country(no)
    return render_template('country.html', temp_dic = temp_dic)

@app.route('/search_list')
def search_list() :
    country_name = request.args['country_name']
    country_list = db.search_country_list(country_name)
    return render_template('search_country_list.html',country_list=country_list, totalcount = len(country_list), country_name = str(country_name))

@app.route('/country_add')
def country_add():
    return render_template('country_add.html')

@app.route('/country_add_pro', methods=['post'])
def country_add_pro():
    c_code = request.form['c_code']
    c_name = request.form['c_name']
    c_gnp = request.form['c_gnp']
    c_population = request.form['c_population']
    print(c_code, c_name, c_gnp, c_population)
    db.country_add(c_code, c_name, c_gnp, c_population)
    return redirect('/')

@app.route('/country_delete/<country_no>')
def country_delete(country_no):
    temp_dic = db.country(country_no)
    return render_template('country_delete.html',temp_dic = temp_dic)

@app.route('/country_delete_pro/<country_no>')
def country_delete_pro(country_no):
    db.country_delete(country_no)
    return redirect('/')


@app.route('/country_update/<country_no>')
def country_update(country_no):
    temp_dic = db.country(country_no)
    return render_template('country_update.html',temp_dic = temp_dic)

@app.route('/country_update_pro', methods=['post'])
def country_update_pro():
    c_no = request.form['c_no']
    c_gnp = request.form['c_gnp']
    c_population = request.form['c_population']
    db.country_update(c_no, c_gnp, c_population)
    return redirect(url_for('country_list'))
app.run(host='127.0.0.1', port =5000, debug=True)
