import pymysql
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='sample1'
            , charset='utf8')
    if conn:
        print('f 디비 접속 완료')
    return conn

def get_country_list():
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT * FROM worldCity order by No desc'''
    cursor.execute(sql)
    result = cursor.fetchall()
    temp_list = []
    for row in result :
        temp_dic = {}
        temp_dic['No'] = row[0]
        temp_dic['Code'] = row[1]
        temp_dic['Name'] = row[2]
        temp_dic['GNP'] = row[3]
        temp_dic['Population'] = row[4]
        temp_list.append(temp_dic)
    
    conn.close()
    return temp_list


def country(no):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT * FROM worldCity where No = %s'''
    cursor.execute(sql,no)
    result = cursor.fetchone()
    temp_dic = {}
    temp_dic['No'] = result[0]
    temp_dic['Code'] = result[1]
    temp_dic['Name'] = result[2]
    temp_dic['GNP'] = result[3]
    temp_dic['Population'] = result[4]
    conn.close()
    return temp_dic

def search_country_list(name):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT * FROM worldCity where Name like %s'''
    name = '%'+name+'%'
    cursor.execute(sql, name)
    result = cursor.fetchall()
    temp_list = []
    for row in result :
        temp_dic = {}
        temp_dic['No'] = row[0]
        temp_dic['Code'] = row[1]
        temp_dic['Name'] = row[2]
        temp_dic['GNP'] = row[3]
        temp_dic['Population'] = row[4]
        temp_list.append(temp_dic)
    
    conn.close()
    return temp_list

def country_add(c_code, c_name, c_gnp, c_population):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()
    sql = '''insert into worldCity(code, name, gnp, population) values (%s, %s, %s, %s)'''    
    cursor.execute(sql, (c_code, c_name, c_gnp, c_population))
    conn.commit()
    conn.close()

def country_delete(country_no):
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()
    sql = '''Delete from worldCity where no = %s'''    
    cursor.execute(sql, (country_no))
    conn.commit()
    conn.close()
