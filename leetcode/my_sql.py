# coding:utf-8
_sql = "SELECT s.user_id, count(distinct t.user_id) Rank FROM user_honor s " \
       "JOIN user_honor t ON s.user_id <= t.user_id GROUP BY s.Id ORDER BY s.user_id desc"

## 给定一个sql表，查询当前表里面user_id的一个排名，user_id越大排名越高。但是排名之间必须是连续的，不能中间有间隔。