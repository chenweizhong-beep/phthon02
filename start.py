# 定义一个start.py ，启动文件展示最终存款金额
import yaml

import send_money
import select_money

if __name__ == '__main__':
    with open(yaml.safe_load('data.yml'),encoding= 'utf-8') as f:
        dates = yaml.safe_load(f)
        print(dates['sal'])
        a = dates['sal']['a']
    send_money.send(a)
    select_money.select()
