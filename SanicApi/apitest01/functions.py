import datetime


def get_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sum_x_y(x, y):
    return x+y


if __name__ == '__main__':
    print(get_datetime())
    print(sum_x_y(12,13))
