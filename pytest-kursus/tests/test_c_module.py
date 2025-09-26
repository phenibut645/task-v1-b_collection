from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

def test_bank_account():
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)

    acc1.deposit(50)
    assert acc1.balance() == 150

    acc1.withdraw(20)
    assert acc1.balance() == 130

    acc1.transfer_to(acc2, 30)
    assert acc1.balance() == 100
    assert acc2.balance() == 80

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_prime_factors():
    assert prime_factors(2) == [2]
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(13) == [13]
    assert prime_factors(100) == [2, 2, 5, 5]

def test_moving_average():
    assert moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert moving_average([1, 2], 3) == []

def test_normalize_scores():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([25, 75]) == [0.25, 0.75]
#da
