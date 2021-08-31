# yahoo_fin library
import numpy as np
import pandas as pd
      
def checkData(i, b, c):
    gp = (i.index == 'grossProfit').any()
    tr = (i.index == 'totalRevenue').any()
    sga = (i.index == 'sellingGeneralAdministrative').any()
    ie = (i.index == 'interestExpense').any()
    oi = (i.index == 'operatingIncome').any()
    ni = (i.index == 'netIncome').any()
    
    
    return
    
def financialStatementCheck(i, b, c):

    # INCOME STATEMENT
    grossProfitMargin = (i.loc['grossProfit'] / i.loc['totalRevenue']) * 100
    averageGPM = grossProfitMargin.mean()

    sgaExpense = (i.loc['sellingGeneralAdministrative'] / i.loc['grossProfit']) * 100
    averageSGA = sgaExpense.mean()

    # rndExpense = (i.loc['researchDevelopment'] / i.loc['grossProfit']) * 100
    # print("\nResearch and Development Expense as Percentage of Gross Profit: \nlower the better")
    # print(rndExpense)

    # depreciationExpense= (i.loc['effectOfAccountingCharges'] / i.loc['grossProfit']) * 100
    # print("\nDepreciation Expense as a Percentage of Gross Profit: \nlower is better ")
    # print(depreciationExpense)

    iExpense = (i.loc['interestExpense'] / i.loc['operatingIncome']) * 100
    averageIE = iExpense.mean()

    # #increasing earnings trend
    # netEarningsArray = [i.loc['netIncome'][0], i.loc['netIncome'][1], i.loc['netIncome'][2], i.loc['netIncome'][3]]
    # print("\nNet Earnings: \nShowing an upward trend is best")
    # print(netEarningsArray)

    netEarningsToRevenue = (i.loc['netIncome'] / i.loc['totalRevenue'])*100
    averageNETR = netEarningsToRevenue.mean()
 
    if averageGPM > 40 and averageSGA < 80 and averageIE < 15 and averageNETR > 10:
        incomeStatement = 1
    else:
        incomeStatement = 0

    #BALANCE SHEET
    '''
    TOO ADD
    -------------------
    current asset cycle
    short term debt
    long term debt
    compare debt to the companies earnings avoid highly leveraged operations
    no preffered stock could be somewhere in other stockholder equity
    '''

    #should be less than .8 we want companies not financed by debt
    debtToShareholdersEquity = b.loc['totalLiab']/(b.loc['totalStockholderEquity']-b.loc['treasuryStock'])
    averageDTSE = debtToShareholdersEquity.mean()
    
    #average of retained earnings growth past 3 years
    reSum = 0
    for x in range(3):
        retainedEarningsGrowth = ((b.loc['retainedEarnings'][x]-b.loc['retainedEarnings'][x+1])/b.loc['retainedEarnings'][x+1])*100
        reSum += retainedEarningsGrowth
    averageREG = reSum / 3
    
    #ROE minus financial engineering higher is better
    adjustedROE = (i.loc['netIncome']/(b.loc['totalStockholderEquity']-b.loc['treasuryStock']))*100
    averageAROE = adjustedROE.mean()
    
    if averageDTSE < .8 and averageAROE > 8 and averageREG > 10:
        balanceSheet = 1
    else:
        balanceSheet = 0

    # #CASH FLOW STATEMENT
    #historically less than 50% (maybe average this)
    netEarningsUsedInCapEx = (c.loc['capitalExpenditures']/c.loc['netIncome'])*100
    averageNETUICE = netEarningsUsedInCapEx.mean()

    #company should regularly buy back shares
    buybacks = c.loc['repurchaseOfStock']
    bb = buybacks.sum()

    if averageNETUICE < 50 and bb != 0:
        cashflowStatement = 1
    else:
        cashflowStatement = 0
        
    #check all statements return if desired
    if incomeStatement == 1 and balanceSheet == 1 and cashflowStatement == 1:
        return 1 
    else:
        return 0
    
    '''
    for now i'm just haing this check if the companies meet dca threshold but in the future I'm going to 
    go a step futher do a regression on all of the variables and weight them accordingly 
    '''
    
    
        