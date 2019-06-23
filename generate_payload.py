import argparse
import random
import string

parser = argparse.ArgumentParser()
parser.add_argument('--payload', '-p', required=True, help='payload path to randomize')
parser.add_argument('--output', '-o', required=True, help='output python file')
parser.add_argument('--seed', '-s', default=random.randint(0, 999999), type=int, help='random seed')

args = parser.parse_args()
payload_path = args.payload
output_path = args.output
seed = args.seed

alpha_num = string.printable

payload = ""
try:
    f = open(payload_path)
except IOError as e:
    print('Can\'t find payload!')
    print('Exiting...')
    exit(1)
else:
    with f:
        payload = f.read()


letters_to_pos = {}
letter_to_gen = set(payload)

random.seed(seed)

random_chars = []
random_count = 0
while len(letter_to_gen) > 0:
    char = random.choice(alpha_num)
    random_chars.append(char)
    if char in letter_to_gen:
        letter_to_gen.remove(char)
        letters_to_pos[char] = random_count
    random_count += 1

letter_indexes = []
for p in payload:
    letter_indexes.append(letters_to_pos[p])

try:
    f = open('runner_template.py')
except IOError as e:
    print('Template was not found!')
    print('Exiting...')
    exit(1)
else:
    with f:
        template = f.read()
        template = template.replace('L', str(letter_indexes))
        template = template.replace('S', str(seed))
        with open(output_path, 'w') as output:
            output.write(template)
