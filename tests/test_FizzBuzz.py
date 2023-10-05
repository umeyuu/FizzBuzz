from src.FizzBuzz import FizzBuzz
import pytest

class TestFizzBuzz:
    @pytest.fixture(scope="function")
    def fizzbuzz(self):
        return FizzBuzz()
    
    class Test_convertメソッドは数を文字列に変換する:
        class Test_3の倍数の場合:
            def test_3を渡すと文字列Fizzを返す(self, fizzbuzz):
                assert fizzbuzz.convert(3) == "Fizz"
        
        class Test_5の倍数の場合:
            def test_5を渡すと文字列Buzzを返す(self, fizzbuzz):
                assert fizzbuzz.convert(5) == "Buzz"
        
        class Test_3と5の倍数の場合:
            def test_15を渡すと文字列FizzBuzzを返す(self, fizzbuzz):
                assert fizzbuzz.convert(15) == "FizzBuzz"
        
        class Test_その他の場合:
            def test_1を渡すと文字列1を返す(self, fizzbuzz):
                assert fizzbuzz.convert(1) == "1"
        
    class Test_get_numbersメソッドは指定した範囲の整数を取得する:
        class Test_1からNまでの整数を取得する:
            def test_1から10までの整数を取得する(self, fizzbuzz):
                assert fizzbuzz.get_numbers(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def test_プリントする(self, capfd):
        print("Hello ! World.")
        out, err = capfd.readouterr()
        assert out == "Hello ! World.\n" \
            and err is ''
    
    class Test_executeソッドはFizzBuzzを実行する:
        def test_1から15までのFizzBuzzを実行する(self, capfd, fizzbuzz):
            fizzbuzz.execute(1, 15)
            out, err = capfd.readouterr()
            assert out == '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n' \
                and err is ''
    