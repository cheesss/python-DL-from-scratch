import pybithumb

con_key= "3588f3caa5b757bb8071c9a2bd4443c6"
sec_key= "2cff6acf43cf1f68ee7fcecedbc1b588"

bithumb = pybithumb.Bithumb(con_key,sec_key)

balance = bithumb.get_balance("BTC")
print(balance)