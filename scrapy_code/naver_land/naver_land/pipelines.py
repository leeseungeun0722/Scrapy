import mysql.connector
from itemadapter import ItemAdapter

class NaverLandPipeline():
    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()

    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'root',
    #         password = 'Tmddms0722@',
    #         database = 'land_DB',
    #         charset = 'utf8',
    #         auth_plugin='mysql_native_password',
    #         use_unicode=True
    #     )
    #     self.curr = self.conn.cursor()
    
    # def create_table(self):
    #     self.curr.execute("CREATE TABLE naver_land (dong_Name text, apartment_Name text,type_List text,pyeongName text,year text, month text, date text,price text, montly text)")

    def process_item(self, item, spider):
        # self.store_db(item)
        return item

    # def store_db(self, item):

    #     self.curr.execute("INSERT INTO naver_land VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)",(
    #         item['dong_Name'],
    #         item['apartment_Name'],
    #         item['type_List'],
    #         item['pyeongName'],
    #         item['year'],
    #         item['month'],
    #         item['date'],
    #         item['price'],
    #         item['monthly']
    #     ))
        
    #     self.conn.commit()