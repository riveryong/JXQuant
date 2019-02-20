import datetime
import tushare as ts
from MysqlHelper import *
import const

# const.FIND_BY_SQL = "findBySql"  # 根据sql查找
# const.COUNT_BY_SQL = "countBySql"  # 自定义sql 统计影响行数
# const.INSERT = "insert"  # 插入
# const.UPDATE_BY_ATTR = "updateByAttr"  # 更新数据
# const.DELETE_BY_ATTR = "deleteByAttr"  # 删除数据
# const.FIND_BY_ATTR = "findByAttr"  # 根据条件查询一条记录
# const.FIND_ALL_BY_ATTR = "findAllByAttr"  # 根据条件查询多条记录
# const.COUNT = "count"  # 统计行
# const.EXIST = "exist"  # 是否存在该记录

if __name__ == '__main__':

    # 设置tushare pro的token并获取连接
    ts.set_token('c1e2a05c71936f78e19e37807638e73fe1a6e32dccd428d5deab8701')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
    start_dt = '20100101'
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')

    # 查询当前所有正常上市交易的股票列表
    data = pro.stock_basic(exchange='', list_status='L',
                           fields='ts_code,symbol,name,area,industry,market,is_hs,list_date')
    print(data)

    try:
        conn = MysqlHelper(host="127.0.0.1", user="root", password="root", charset="utf8", database="youke", port=3306)
        # 根据字段统计count, join>>AND,OR,可以不传，默认为AND
        print(conn.findKeySql(const.COUNT, table="t_company", params={"company_id": "114"}, join="AND"))

        for stock in data:
            print(stock)

    except Exception as e:
        print("执行sql出错:")
        raise e
        conn.close()

