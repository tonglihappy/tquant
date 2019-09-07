import tushare as ts
from datetime import datetime as dt

def getql():
    today = dt.now()
    quarter = today.month
    if quarter >= 1 and quarter <= 3 :
        return dt(today.year,3,31).strftime('%Y%m%d')
    elif quarter >= 4 and quarter <= 6:
        return dt(today.year,6,30).strftime('%Y%m%d')
    elif quarter >=7 and quarter <= 9:
        return dt(today.year,9,30).strftime('%Y%m%d')
    else:
        return dt(today.year,12,31).strftime('%Y%m%d')

if __name__ == "__main__":
    ts.set_token('c21631bece923458e470682569cc5998e124a09871666de852cdd439')
    pro = ts.pro_api()

    today = getql() 

    print(today)

    df = pro.cashflow(ts_code='300104.SZ', start_date='20160101', end_date='20180830')

#    print(df.end_date)
#    print(df['c_fr_sale_sg'])

#    df = pro.income(ts_code='300104.SZ', start_date='20160101', end_date='20180830', period='',fields='ts_code,ann_date,f_ann_date,end_date, report_type,revenue')
#    print(df)

#    ratio_cash_income = df
