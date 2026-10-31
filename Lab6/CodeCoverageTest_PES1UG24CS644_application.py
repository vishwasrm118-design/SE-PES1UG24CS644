
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


def test_known_axle_peak_fastag():
    assert toll_for(2, True, True) == 112.5


def test_unknown_axle_nonpeak_fastag():
    assert toll_for(5, False, True) == 380


def test_no_fastag():
    assert toll_for(3, False, False) == 150


def test_exempt_vehicle():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_non_exempt_vehicle():
    assert toll_charge("car", 2, False, False) == 100


def test_buy_pass():
    assert pass_advice([(False, False)], 2, 50) == "buy_pass"


def test_pay_per_trip():
    assert pass_advice([(False, False)], 2, 150) == "pay_per_trip"
