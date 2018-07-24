from defer_defaults import deferrable_args, deferred


def test_deferral():

    @deferrable_args
    def subfunction_1(a=2, b=3, c=4):
        return a+b*c

    @deferrable_args
    def subfunction_2(d=5, e=6, f=7):
        return d*e+f

    def main_function(a=deferred, b=deferred, c=deferred, d=deferred, e=deferred, f=deferred):
        return subfunction_1(a=a, b=b, c=c) + subfunction_2(d=d, e=e, f=f)

    assert main_function() == (2+3*4)+(5*6+7)
    assert main_function(a=8) == (8+3*4)+(5*6+7)


if __name__ == '__main__':
    test_deferral()
