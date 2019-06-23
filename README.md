# RandomPayload

This is a small experiment to obfuscate a program. It uses the fact that a pseudo-random generator will always produce the same sequence when given a specific seed.

The program takes a payload and generate a script that does the same thing but only using randomly generated characters.

## Generate a randomized payload
```bash
python3 generate_payload.py --payload=payload_example.py --output=test.py --seed=123
```
## Execute the payload
```bash
python3 test.py 
```
