import count

#def test_count_zeros():
 #   assert count.count([0,0,0], 0) == 3

#def test_count_string():
 #   assert count.count(["a","a","a"], "a") == 3

def test_count_fact():
    assert count.fact(0) == 1
    assert count.fact(1) == 1
    assert count.fact(5) == 120

def test_squares():
    assert count.list_of_squares(2) == {1: 1, 2: 4}
    assert count.list_of_squares(4) == {1: 1, 2: 4, 3: 9, 4: 16}

def test_vowels():
    assert count.vowels("space") == 2
    assert count.vowels("BorisIsHavingAPartyBringYourVodkaAndYourCharlie") == 18
