import yahoo_fin.stock_info as si
import DCA_Fundamentals as dca

#selecting the company
#also find a way to add lists of companies
tickers = ["NWC.TO"]

for x in tickers: 
    
    #returning financial statements
    iStatement = si.get_income_statement(x)
    bSheet = si.get_balance_sheet(x)
    cfStatement = si.get_cash_flow(x)

    #if company doesn't have necessary data skip the dca check 
    dca.checkData(iStatement, bSheet, cfStatement)
    
    # #return 1 or 0 if it meets criteria
    # check = dca.financialStatementCheck(iStatement, bSheet, cfStatement)
    # print(check)
    # if check == 1:
    #     print(x)
    #     print("Possible DCA")
    # else:
    #     print(x)
    #     print("No DCA")
        


