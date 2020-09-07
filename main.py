import invaders
import radar


def main():
    matches = {'squid': [], 'crab': []}
    with open('test_input.txt', 'r') as f:
        raw = f.read().split()
    factory = invaders.InvaderFactory(radar.Radar(raw))

    cur_invader = factory()
    while cur_invader is not None:
        x, y = factory.radar.pos_x, factory.radar.pos_y
        crab_match = invaders.CRAB.match(cur_invader)
        squid_match = invaders.SQUID.match(cur_invader)
        matches['crab'].append((crab_match, x, y))
        matches['squid'].append((squid_match, x, y))
        cur_invader = factory()

    output = "Here's all the possible invaders:\n"
    for ratio, x, y in matches['crab']:
        if ratio > 0.8:
            output += "Possible crab at (%d, %d). Accuracy: %.2f%%\n" % (x, y, ratio * 100)
    for ratio, x, y in matches['squid']:
        if ratio > 0.8:
            output += "Possible squid at (%d, %d). Accuracy: %.2f%%\n" % (x, y, ratio * 100)

    print(output)



if __name__ == "__main__":
    main()
