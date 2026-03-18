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
 -The AI generated starter tests that compared `check_guess(...)` against a plain string like `"Too High"`, but the function returns a tuple `("Too High", "Go LOWER!")`. All three tests failed immediately when I ran pytest. The AI caught and fixed this after seeing the output, but it was a reminder that AI-generated tests still need to be ran beacuse it is not always right

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
 - A bug was fixed when a failing pytest test turned green and I confirmed the correct behavior in the running app. For the hint direction fix, `test_too_high_message_says_go_lower` went from failing (`assert "LOWER" in "Go HIGHER!"`) to passing after I corrected the swapped messages. For the New Game reset, I verified manually — clicking New Game after winning now starts a fresh round instead of staying frozen. The AI also wrote the range-validation tests before the fix existed, so they acted as a spec that told me exactly what `parse_guess` needed to do.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
 - Every time you click a button or type something in a Streamlit app, the entire Python script reruns from the top — it's like refreshing the page from scratch each time. That means any normal variable you set would just get reset to its starting value on every click, which is why the game kept forgetting things. Session state is basically a dictionary that Streamlit keeps alive between those reruns, so values like the secret number and your score actually stick around. Once I understood that, the New Game bug made total sense — we were resetting some session state values but forgetting to reset others, so the game remembered it had already been won even after "restarting."

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
 - Writing tests before the fix was something I want to keep doing. The AI wrote the range validation tests when `parse_guess` still had the bug, so the failing tests acted like a checklist — I knew exactly what "done" looked like before I even touched the code. That felt way more structured than just guessing if something worked.

- What is one thing you would do differently next time you work with AI on a coding task?
 - I'd run the AI's output immediately instead of trusting it first. The test file the AI generated looked completely fine but failed the second I ran pytest because it was comparing a tuple to a string. It cost no time to catch once I ran it, but I could have easily missed it if I just skimmed the code and moved on.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
 - I used to assume AI code was basically correct unless something looked obviously wrong. Now I think of it more like code from a teammate who works fast but sometimes makes subtle mistakes — it's a great starting point, but you still have to read it, run it, and test it yourself before trusting it.
