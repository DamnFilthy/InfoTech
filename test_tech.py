import pytest
from dropbox import authorization, put, get
from settings import TOKEN, APP_KEY


class TestSomething:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    # test authorization
    def test_authorization(self):
        assert authorization() == True

    # test put function
    @pytest.mark.parametrize('token, path, dest, result', [
        (TOKEN, 4, 12, False),
        (TOKEN, 'dsfsdf', 'sdhdf', False),
        (TOKEN, 'C:\\Users\\User\\Desktop\\some.jpg', '/test_folder/icon.jpg', False),
        (TOKEN, 'C:\\Users\\User\\Desktop\\dropbox.txt', '/test_folder/dropbox.txt', True),
        (TOKEN, 'C:\\Users\\User\\Desktop\\dropbox.txt', '/test_folder/new.txt', True)
    ])
    def test_put(self, token, path, dest, result):
        assert put(token, path, dest) == result

    # test get function
    @pytest.mark.parametrize('token, path, dest, result', [
        (TOKEN, 'dsfsf', 12, False),
        (TOKEN, '14', 'sdhdf', False),
        (TOKEN, '/test_folder/icon.jpg', 'C:\\Users\\User\\Desktop\\some.jpg', False),
        (TOKEN, '/test_folder/dropbox.txt', 'C:\\Users\\User\\Desktop\\new.txt', True),
        (TOKEN, '/test_folder/new.txt', 'C:\\Users\\User\\Desktop\\some_text.txt', True)
    ])
    def test_get(self, token, path, dest, result):
        assert get(token, path, dest) == result

    def teardown_class(self):
        print('method teardown_class')
