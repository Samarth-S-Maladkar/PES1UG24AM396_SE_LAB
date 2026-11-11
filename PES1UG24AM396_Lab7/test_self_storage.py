from hypothesis import given, strategies as st
from self_storage import parse_rental, duration_average, payable_rent


@given(st.text() | st.none())
def test_parse_rental_no_crash(s):
    try:
        result = parse_rental(s)
        assert isinstance(result, tuple) and len(result) == 2
    except Exception as e:
        assert False, f"parse_rental crashed with: {e}"


@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    try:
        result = duration_average(s)
        assert isinstance(result, int) and result >= 0
    except Exception as e:
        assert False, f"duration_average crashed with: {e}"


@given(st.text() | st.none())
def test_payable_rent_no_crash(s):
    try:
        result = payable_rent(s)
        assert isinstance(result, (int, float)) and result >= 0
    except Exception as e:
        assert False, f"payable_rent crashed with: {e}"
