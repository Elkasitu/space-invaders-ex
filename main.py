import argparse
import invaders
import radar


def parse_args():
    parser = argparse.ArgumentParser(description="Locate all possible space invaders in a radar")
    parser.add_argument('-D', '--input-data', default="test_input.txt",
        help="Path to text file representing radar input, rows must be separated by newlines \
                (default: test_input.txt)")
    parser.add_argument('-t', '--threshold', type=float, default=80.0,
        help="Accuracy cutoff point (%%) for data that is considered valid (default: 80)")
    parser.add_argument('-s', '--sort-by', choices=['accuracy', 'position'], default='accuracy',
        help="Sort output data by either accuracy percent or by position on the radar \
                (default: accuracy)")
    return parser.parse_args()


def main():
    args = parse_args()
    matches = []
    try:
        with open(args.input_data, 'r') as f:
            raw = f.read().split()
    except Exception:
        print("Error opening file %s" % args.input_data)
        return
    assert [isinstance(row, str) for row in raw], (
        "Input file must contain strings (rows) separated by newlines")

    factory = invaders.InvaderFactory(radar.Radar(raw))

    cur_invader = factory()
    while cur_invader is not None:
        x, y = factory.radar.pos_x, factory.radar.pos_y
        crab_match = invaders.CRAB.match(cur_invader)
        squid_match = invaders.SQUID.match(cur_invader)

        if crab_match > squid_match:
            candidate = {'type': 'crab', 'accuracy': crab_match * 100, 'position': (x, y)}
        else:
            candidate = {'type': 'squid', 'accuracy': squid_match * 100, 'position': (x, y)}
        if candidate['accuracy'] >= args.threshold:
            matches.append(candidate)

        cur_invader = factory()

    matches = sorted(matches, key=lambda x: x[args.sort_by], reverse=args.sort_by == 'accuracy')
    output = "Here's all the possible invaders:\n"
    for match in matches:
        output += "Possible %s at %s. Accuracy: %.2f%%\n" % (
                match['type'], match['position'], match['accuracy'])
    print(output)



if __name__ == "__main__":
    main()
