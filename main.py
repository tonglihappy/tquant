import tushare as ts
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import datetime

def getql():
    today = dt.now()
    quarter = today.month
    if quarter >= 1 and quarter <= 3 :
        return quarter, dt(today.year,3,31).strftime('%Y%m%d')
    elif quarter >= 4 and quarter <= 6:
        return quarter, dt(today.year,6,30).strftime('%Y%m%d')
    elif quarter >=7 and quarter <= 9:
        return quarter, dt(today.year,9,30).strftime('%Y%m%d')
    else:
        return quarter, dt(today.year,12,31).strftime('%Y%m%d')

def time_delta(quarter, period):
    periods = []

    sdate = datetime.datetime.strptime(period,'%Y%m%d')
    print(sdate.month)
    edate1 = sdate - relativedelta(years=1)
    edate2 = sdate - relativedelta(years=2)
    edate3 = sdate - relativedelta(years=3)
    last_year = edate1.strftime("%Y")

    periods.append(edate1.strftime("%Y") + "1231")
    periods.append(edate2.strftime("%Y") + "1231")
    periods.append(edate3.strftime("%Y") + "1231")

    return periods

if __name__ == "__main__":

    cashflow = []

    ts.set_token('c21631bece923458e470682569cc5998e124a09871666de852cdd439')
    pro = ts.pro_api()

    quarter, period = getql() 

    #print(quarter, type(period))

    df = pro.cashflow(ts_code='300104.SZ', start_date='20190101', end_date='20190907')

    cashflow.append(df[0:1])

    print(cashflow)

    for date in time_delta(quarter, period):
        df = pro.cashflow(ts_code='300104.SZ', period=date)
        



#    print(df)
#    print(df.end_date)
#    print(df['c_fr_sale_sg'])

#    df = pro.income(ts_code='300104.SZ', start_date='20160101', end_date='20180830', period='',fields='ts_code,ann_date,f_ann_date,end_date, report_type,revenue')
#    print(df)

#    ratio_cash_income = df
