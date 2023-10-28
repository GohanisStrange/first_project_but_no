def  check_pos_nums (x,c):
    '''
    >>> x*c(10,13)
    True
    '''
    if x*c:
        print(c*x)
    return False

def check_os_nums(x, y, c):
        '''
        >>> check_os_nums(30,12,43)
        True
        '''
        if x<c:
            return True
        elif x<c:
            return False
import unittest
def check_user(username):
    users = ['Pavel','Fatxullo','Xasan']

    if username in users:
        return 'есть'
    else:
        return 'no founds'

class TestOne(unittest.TestCase):
    def test_check(self):
        self.assertEquals(check_user('Fatxullo'), 'У нас еть Xasan','Нету у нас Fatxullo')





