
import pytest

#pytestmark = [pytest.mark.smoke, pytest.mark.str]

@pytest.mark.skip("skip all")
#@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'


@pytest.mark.skip("skip all")
#@pytest.mark.str
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26
