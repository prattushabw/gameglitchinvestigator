# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

-> I had to submit guess twice for it to go through to history. First time the old guess was added to history the second time it actually sent my new guess in.
-> It kept saying guess higher even when i put 100. If i guess 100 and its not 100 it should say guess lower. There was also no error message when I guessed above 100. There should be a limit there
-> When I won, and clicked New Game it wouldnt reset. It would just say "You already won. Start a new game to play again." still and only update "Secret" but nothing else.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 - I used Claude throughout this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
 - The AI correctly identified that the hint messages in `check_guess` were swapped — when `guess > secret` the code was returning "Go HIGHER!" instead of "Go LOWER!". It refactored the function into `logic_utils.py` with the messages fixed and generated pytest tests (`test_too_high_message_says_go_lower`) that confirmed the fix. I verified it by running `pytest` and seeing the test go from fail to pass, and also by reading the corrected return values myself in `logic_utils.py`.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 -

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
