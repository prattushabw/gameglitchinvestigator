from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_go_lower():
    # Bug fix: when guess is too high, hint must say Go LOWER, not Go HIGHER
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # Bug fix: when guess is too low, hint must say Go HIGHER, not Go LOWER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- Bug: no error when guess is above 100 ---
# These tests currently FAIL because parse_guess has no range validation.
# They will go green once parse_guess rejects out-of-range values.

def test_guess_above_max_is_rejected():
    # Guessing 101 should fail with an error — not silently accepted
    ok, _, err = parse_guess("101")
    assert ok is False
    assert err is not None

def test_guess_at_exactly_100_is_accepted():
    # 100 is a valid guess and must not be rejected
    ok, value, _ = parse_guess("100")
    assert ok is True
    assert value == 100

def test_guess_below_min_is_rejected():
    # Guessing 0 or negative should also fail
    ok, _, err = parse_guess("0")
    assert ok is False
    assert err is not None

# --- Bug: double-submit before guess appears in history ---
# This is a Streamlit render-order issue (st.write on line 120 of app.py runs
# before the submit block on line 149 appends to history, so the debug panel
# is always one render behind). It cannot be caught by a pure unit test —
# it requires a Streamlit integration test or manual verification in the app.
