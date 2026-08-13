# Run instructions

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 TtsTest.py
(Type any sentence and the program will spell it out loud)
deactivate
```

Note: When running TtsTest.py, you may get a warning that says "playsound is relying on another python subprocess. Please use `pip install pygobject` if you want playsound to run more efficiently." This warning can be ignored.
