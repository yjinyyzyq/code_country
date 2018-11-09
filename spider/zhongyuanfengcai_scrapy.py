# coding:utf-8
from lxml import etree
import requests
# 对当前页面进行抓取，获取当前猜中的开奖结果。最终拼接成如下的格式。
# src是抓取网页的地址。这个按默认的来，中奖情况直接按开奖情况进行拼接。一等奖，二等奖，三等奖。销售额，


def get_latest_url():
    # 河南福彩官方网址。
    url = "http://www.henanfucai.com/"
    req = requests.get(url)
    html = etree.HTML(req.content)
    ret = html.xpath('//*[@id="kai"]/div[4]/div[2]/p[5]/a/@href')[0]
    return url + ret


# get_latest_url()


def get_lottery_result(url):
    ret = {}
    req = requests.get(url)
    html = etree.HTML(req.content)
    left = html.xpath('//*[@id="kais_ll"]/table/tr')
    # lottery and number
    lottery_name = left[0].xpath("./td[1]/text()")[0]
    if lottery_name == "22选5开奖号码":
        print("彩种正确")
        key = "henan_zhongyuanfengcai22x5"
        ret["key"] = key
        src = "http://www.cp2y.com/"
        ret['src'] = src
        name = "中原风采22选5"
        ret['name'] = name
        # 全国销售金额。
        number = ",".join(left[0].xpath("./td[2]/span/text()"))
        ret["result"] = number
        sales = left[1].xpath('./td[2]/span/text()')[0]
        ret['sales'] = int(sales)

        # 奖池累计金额
        balance = int(left[4].xpath('./td[2]/span/text()')[0])
        ret['balance'] = balance
        ret['detail'] = []
        right = html.xpath('//*[@id="kais_r"]/table/tr')
        # 一等奖
        count, _, money = right[1].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "一等奖"})
        # 二等奖
        count, _, money = right[2].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "二等奖"})
        # 三等奖
        count, _, money = right[3].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "三等奖"})
        # 好运二
        count, _, money = right[4].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "好运二"})
        # 好运三
        count, _, money = right[5].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "好运三"})
        # 好运四
        count, _, money = right[6].xpath('./td/span/text()')
        ret['detail'].append({"count": count, "money": money, "name": "好运四"})

        # issue and date
        issue, date = html.xpath('//*[@id="kuang_gg"]/div[2]/span/text()')
        ret["issue"] = issue
        ret['date'] = date + " 00:00"
        return ret
    else:
        return False

# url = "http://www.henanfucai.com/Html/Gonggao/11342.html"
a = get_latest_url()
# print(a)
print(get_lottery_result(a))
