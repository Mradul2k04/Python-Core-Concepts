import pytest    #import pytest for the function programm

from logic import multiply 
from logic import add 

def test_multiply(): 
    assert multiply(10,0)==0 

def test_multiply_negative(): 
    assert multiply(-2,3)==-6 

def test_add_numbers(): 
    assert add(5,8)==13 

@pytest.mark.parametrize("a,b,expected",[ 
    (2,3,6), 
    (0,5,0), 
    (-2,-3,6), 
    (5,-1,-5) 
]) 
def test_multiply_many(a,b,expected): 
    assert multiply(a,b)==expected
    
@pytest.fixture
def sample_data():
    return{"val1":10,"val2":20}

def test_add_with_fixture(sample_data):
    result=add(sample_data["val1"],sample_data["val2"])  
    assert result ==30  
    
@pytest.fixture
def user_list():
    return ["Alice","Bob"]

def test_user_list_length(user_list):
    assert len(user_list) ==2
    
@pytest.fixture
def user_num():
    return 10
@pytest.mark.parametrize("input_val,expected_result",[
    (5,15),
    (20,30),
    (90,100)
])
def test_add_fixture_and_param(user_num,input_val,expected_result):
    assert add(user_num,input_val)==expected_result


    
    