from msilib import Table
import mysql.connector
from itemadapter import ItemAdapter

class NaverLandPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '0722',
            database = 'naver_DB',
            charset = 'utf8',
            auth_plugin='mysql_native_password',
            use_unicode=True
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("CREATE TABLE dong_list (dong_Name text, apartment_Name text,type_List text,pyeongName text,year text, month text, date text,price text, montly text)")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        self.curr.execute("INSERT INTO dong_list VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)",(
            item['dong_Name'],
            item['apartment_Name'],
            item['type_List'],
            item['pyeongName'],
            item['year'],
            item['month'],
            item['date'],
            item['price'],
            item['monthly']
        ))

        self.curr.execute("SELECT * FROM dong_list")
        
        self.conn.commit()