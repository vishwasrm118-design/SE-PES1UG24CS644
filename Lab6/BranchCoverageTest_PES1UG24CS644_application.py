
import pytest
from highway_toll import toll_for, toll_charge, pass_advice


# 1. Invalid axle count
def test_invalid_axle_count():
    with pytest.raises(ValueError):
        toll_for(1, False, False)


# 2. Known axle count, non-peak, no FASTag
def test_known_axle_no_fastag():
    assert toll_for(2, False, False) == 100


# 3. Unknown axle count
def test_unknown_axle_count():
    assert toll_for(5, False, False) == 400


# 4. Peak hour condition
def test_peak_hour():
    assert toll_for(2, True, False) == 125


# 5. FASTag with 2 axles
def test_fastag_two_axles():
    assert toll_for(2, False, True) == 90


# 6. FASTag with more than 2 axles
def test_fastag_other_axles():
    assert toll_for(3, False, True) == 142.5


# 7. Exempt vehicle
def test_exempt_vehicle():
    assert toll_charge("ambulance", 2, False, False) == 0


# 8. Non-exempt vehicle
def test_non_exempt_vehicle():
    assert toll_charge("car", 2, False, False) == 100


# 9. Buy pass condition
def test_buy_pass():
    assert pass_advice([(False, False)], 2, 50) == "buy_pass"


# 10. Exact pass price condition
def test_either_option():
    assert pass_advice([(False, False)], 2, 100) == "either"


# 11. Pay per trip condition
def test_pay_per_trip():
    assert pass_advice([(False, False)], 2, 150) == "pay_per_trip"


# 12. Empty trips condition
def test_empty_trips():
    assert pass_advice([], 2, 0) == "either"
