def fn1(arg1, **kwargs):
    print(arg1)
    # print(kwargs)
    for key in kwargs.keys():
        print(kwargs[key])
        print(type(kwargs[key]))


fn1(arg1='bar', arg2='foo')

fn1(arg1='bar', arg2=[1.0, 1.2, 0.9])
