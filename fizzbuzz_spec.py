from fizzbuzz import fizzBuzz

def test_fizzbuzz_1():
  assert fizzBuzz(1) == 1

def test_fizzbuzz_2():
  assert fizzBuzz(2) == 2

def test_fizzbuzz_3():
  assert fizzBuzz(3) == 'Fizz'

def test_fizzbuzz_5():
  assert fizzBuzz(5) == 'Buzz'

def test_fizzbuzz_6():
  assert fizzBuzz(6) == 'Fizz'

def test_fizzbuzz_10():
  assert fizzBuzz(10) == 'Buzz'

def test_fizzbuzz_15():
  assert fizzBuzz(15) == 'FizzBuzz'

def test_fizzbuzz_30():
  assert fizzBuzz(30) == 'FizzBuzz'


