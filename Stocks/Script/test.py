import requests

# url = 'http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XSES:S58&region=sgp&culture=en-US&cur=&reportType=bs&period=12&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=872082&denominatorView=raw&number=3'
# headers = {'Referer': 'http://financials.morningstar.com/balance-sheet/bs.html?t=S58&region=sgp&culture=en-US'}

# url = 'http://financials.morningstar.com/finan/ajax/exportKR2CSV.html?&callback=?&t=XSES:D05&region=sgp&culture=en-US&cur=&order=asc'
# headers = {'Referer': 'http://financials.morningstar.com/ratios/r.html?t=D05&region=sgp&culture=en-US'}

url = 'https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/0P0000A6B4/balancesheet/detail?dataType=A&reportType=A&locale=en&&operation=export&clientId=MDC&benchmarkId=category&version=3.21.1'
headers = {'Referer': 'https://www.morningstar.com/', 'apikey': 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T', 'x-sal-contenttype': 'nNsGdN3REOnPMlKDShOYjlk6VYiEVLSdpfpXAm7o2Tk='}

response = requests.get(url, headers=headers)


with open("premium.xls", "wb") as f:
    f.write(response.content)

# free: "e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU=",
# premium: "nNsGdN3REOnPMlKDShOYjlk6VYiEVLSdpfpXAm7o2Tk="

 # e.default = ["0P0000EHTQ", "0P0000AN4M", "0P0000AQSC", "0P0000C0NS", "0P0000EQGA", "0P000003PE"]