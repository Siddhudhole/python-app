from src.operation import add,subtract 

    # Check if the necessary environment variables are set
def test_add():
    assert add(2,3)==5
    assert add(-1,2)==1
    assert add(0,0)==0


def test_subtract():
    assert subtract(5,3)==2
    assert subtract(2,2)==0 
    assert subtract(0,5)==-5 