# coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

path = u"C://Users//wenjia//Desktop//1.txt"
date = "2018-11-07"


def draw_pic(path, date):
    ret = []
    with open(path, "r+") as f:
        for i in f:
            _, _, day, second, _, _, _, num = i.split(" ")
            if day == date:
                ret.append([second.rstrip(','), int(num.rstrip())])  # 预计最多有17280刻度线

    label_list, num_list = [i[0] for i in ret], [i[1] for i in ret]
    tick_spacing = 20
    fig, ax = plt.subplots(1, 1)
    a = list(range(len(label_list)))
    plt.bar(left=a, height=num_list, width=0.4, alpha=0.8, color='red')
    # plt.plot(a, num_list)
    plt.xticks(a, label_list, rotation=45, fontsize=5)
    for label in ax.get_xticklabels():
        label.set_visible(False)
    for label in ax.get_xticklabels()[::tick_spacing]:
        label.set_visible(True)
    plt.title(date)
    plt.savefig("{}.jpg".format(date), dpi=500)

    # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    # plt.savefig("1.jpg", dpi=500)
    # plt.ylim(0,150)
    # plt.xticks(x, label_list, rotation=90, fontsize=5)
    # plt.
    # # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    # plt.ylabel("Second_Behind_Master")
    # plt.savefig("1.jpg", dpi=500)


draw_pic(path, date)

