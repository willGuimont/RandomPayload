import argparse
import random
import string


def generate_payload(seed, letter_indexes):
    return f'''import random as r, string as s
r.seed({seed})
p={letter_indexes}
q=[r.choice(s.printable)for _ in range(max(p)+1)]
exec(''.join([q[x]for x in p]))'''


if __name__ == '__main__':
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

    with open(output_path, 'w') as output:
        output_code = generate_payload(seed, letter_indexes)
        output.write(output_code)
