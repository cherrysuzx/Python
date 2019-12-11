import numpy as np
import pandas as pd

def hello(name):
    strHello='Hello,'+name
    return strHello;
print (hello("python"))
order_list = [
    {'order_id': 1, 'price': 100, 'date': '2018-01-01'},
    {'order_id': 2, 'price': 200, 'date': '2018-01-02'},
    {'order_id': 3, 'price': 300, 'date': '2018-01-05'},
    {'order_id': 4, 'price': 400, 'date': '2018-01-01'},
]

df = pd.DataFrame(order_list)
print(df)

result = np.sqrt(16)
print(result)
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.cumsum(0))
print(a.cumsum(1))
print(a.cumprod(0))
print(a.cumprod(1))




