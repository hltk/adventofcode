def main():
    from aocd import data

    phrases = list(map(lambda x: x.split(), data.split("\n")))

    # part 1
    print(sum(1 for phrase in phrases if len(set(phrase)) == len(phrase)))

    # part 2
    sorted_phrases = map(lambda x: list(map(lambda y: ''.join(sorted(y)), x)), phrases)

    print(sum(1 for phrase in sorted_phrases if len(set(phrase)) == len(phrase)))

main()
