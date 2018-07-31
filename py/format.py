

print('{}'.format(42))
print('{:d}'.format(42))

print('{}'.format(3.14))

print('{}'.format('hej'))
print('test {:>10} test'.format('hej')) # minimum 10 
print('test {:<10} test'.format('hej')) # minimum 10 
print('test {:<10} test'.format('0123456789-0123456789')) # minimum 10 
print('test {:.8} test'.format('hej')) # just truncate to not spcae


from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime.now()))

