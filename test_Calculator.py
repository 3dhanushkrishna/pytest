import Calculator
def test_add2no():
    x=10
    y=20
    res=Calculator.add2no(x,y)
    assert res == x+y
def test_sub2no():
    x=10
    y=20
    res=Calculator.sub2no(x,y)
    assert res == x-y
def test_mul2no():
    x=10
    y=20
    res=Calculator.mul2no(x,y)
    assert res == x*y
def test_div2no():
    x=10
    y=20
    res=Calculator.div2no(x,y)
    assert res == x/y