# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Game purpose:** A number guessing game where the player tries to guess a secret number within a limited number of attempts. After each guess the game gives a hint (Go Higher / Go Lower) to help narrow it down. Points are awarded based on how quickly you guess correctly.

**Bugs found:**
- Hint messages were backwards — guessing too high said "Go HIGHER!" and guessing too low said "Go LOWER!".
- No range validation, so entering 101 or 0 was silently accepted instead of showing an error.
- Clicking New Game after winning didn't fully reset — `status` and `history` were never cleared, so the game immediately froze on "You already won" again.
- Guess history in the debug panel was always one submit behind due to Streamlit render order.

**Fixes applied:**
- Swapped the "Go HIGHER!" and "Go LOWER!" messages in `check_guess` in `logic_utils.py`.
- Added range validation in `parse_guess` to reject any value outside 1–100.
- Added `st.session_state.status = "playing"` and `st.session_state.history = []` to the New Game block in `app.py`.
- Refactored all game logic out of `app.py` into `logic_utils.py`.
- Fixed and expanded the pytest suite from 3 broken tests to 8 passing tests.

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]


## 🚀 Stretch Features

- [x] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
![image of passed test cases](image.png)