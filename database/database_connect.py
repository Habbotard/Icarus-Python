"""
Database connection class
Author: Alex (TheAmazingAussie)
"""

import pymysql


class DatabaseConnection():
    def create_connection(self):
        return pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='icarus')




