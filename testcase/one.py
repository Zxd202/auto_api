import pytest

class TestDemo:
    data_list = [("xiaoming","123"),("xiaohong","345")]
    @pytest.mark.parametrize(('name','password'),data_list)
    def test_a(self,name,password):
        print('test_a')
        print(name,password)
        assert 1

if __name__ == '__main__':
    pytest.main(["one.py"])