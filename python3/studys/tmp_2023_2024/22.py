import time

d1 = {'name': 'alex'}

d1.update(age=200)
print(d1)
d1.update(sex='male')
print(d1)

d1.update(good='formal')
print(d1)


def yest():
    print('start...')
    time.sleep(1)
    print('stop...')


def show_time(func):
    def innner():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(f'total cost time: {stop_time - start_time}s')
    return innner

@show_time
def yest1():
    print('start...yest1')
    time.sleep(1)
    print('stop...yest1')

if __name__ == '__main__':
    test = show_time(yest)
    yest()
    yest1()