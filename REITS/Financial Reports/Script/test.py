from yahoofinancials import YahooFinancials
import pandas as pd

ticker = 'S59.SI'
yahoo_financials = YahooFinancials(ticker)

incomeStatement = yahoo_financials.get_financial_stmts('annual', 'income')
print(incomeStatement)

incomeStatement_df = pd.DataFrame(incomeStatement['incomeStatementHistory'][ticker][0])

# result = pd.concat([incomeStatement_df_0, incomeStatement_df_1], axis=1)

for dic in incomeStatement['incomeStatementHistory'][ticker][1:]:
    incomeStatement_df = pd.concat([incomeStatement_df,  pd.DataFrame(dic)], axis=1)


print(incomeStatement_df)