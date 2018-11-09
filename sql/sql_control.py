# coding:utf-8
# 对系统里面的Seconds_Behind_Master进行监控。
import MySQLdb
import logging
HOST = "0.0.0.0"
USER = "XXXXXX"
PASSWD = "XXXXXX"
DB = "XXXXXX"


def execute_sql_fetchall(sql):
    """数据库连接操作,返回fetchall的数据"""
    data = []
    try:
        # print sql, "------------------------sql-----------------------------"
        conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, charset="utf8")
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cur.execute(sql)
            data = cur.fetchall()
            cur.close()
            conn.commit()
        except:
            data = "fail"
            conn.rollback()
        finally:
            conn.close()
    except MySQLdb.Error, e:
        logging.info(e.args)
        # print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return data

_sql = "show slave status"

a = execute_sql_fetchall(_sql)
print(a)

