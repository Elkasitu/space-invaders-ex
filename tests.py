import invaders
import radar
import unittest


class TestInvaderMatching(unittest.TestCase):

    def test_exact_match(self):
        new_crab = invaders.Crab()
        # Crab() should match Crab(), duh
        self.assertEqual(invaders.CRAB.match(new_crab), 1)

    def test_partial_match(self):
        new_crab = invaders.Crab()
        new_crab.bitmap[0] = 'o' * len(new_crab.bitmap[0])
        # Crab() shouldn't exactly match this newly-modified crab
        self.assertLess(invaders.CRAB.match(new_crab), 1)

    def test_different_species_match(self):
        self.assertLess(invaders.CRAB.match(invaders.SQUID), 1)
        self.assertLess(invaders.SQUID.match(invaders.CRAB), 1)


    def test_partial_match_ratio(self):
        new_crab = invaders.Crab()
        new_crab.bitmap[0] = 'o' * len(new_crab.bitmap[0])
        noise = new_crab.bitmap[0].count('o') - invaders.CRAB.bitmap[0].count('o')
        expected_match_ratio = (invaders.CRAB.max_pixels - noise) / invaders.CRAB.max_pixels
        # Crab should match with new_crab at expected_match_ratio
        self.assertAlmostEqual(invaders.CRAB.match(new_crab), expected_match_ratio)


class TestInvaderGeneration(unittest.TestCase):

    def _create_factory(self, raw):
        r = radar.Radar(raw)
        return invaders.InvaderFactory(r)

    def test_crab_generation(self):
        factory = self._create_factory(invaders.BITMAPS['crab'])
        crab = factory()
        self.assertEqual(invaders.CRAB.match(crab), 1)

    def test_squid_generation(self):
        factory = self._create_factory(invaders.BITMAPS['squid'])
        squid = factory()
        self.assertEqual(invaders.SQUID.match(squid), 1)

    def test_noise_generation(self):
        noise = ['o' * invaders.MAX_SPRITE_WIDTH] * invaders.MAX_SPRITE_LENGTH
        factory = self._create_factory(noise)
        random = factory()
        self.assertLess(invaders.CRAB.match(random), 1)

    def test_generate_past_exhaustion(self):
        factory = self._create_factory(invaders.BITMAPS['squid'])
        for i in range(len(invaders.BITMAPS['squid'][0]) * len(invaders.BITMAPS['squid'])):
            self.assertTrue(isinstance(factory(), invaders.SpaceInvader))
        self.assertIsNone(factory())

    def test_multiple_generations(self):
        bitmap = [r1 + r2 for r1, r2 in zip(invaders.BITMAPS['crab'], invaders.BITMAPS['squid'])]
        factory = self._create_factory(bitmap)
        crab = factory()
        for i in range(invaders.MAX_SPRITE_WIDTH - 1):
            self.assertTrue(isinstance(factory(), invaders.SpaceInvader))
        squid = factory()
        self.assertEqual(invaders.CRAB.match(crab), 1)
        self.assertEqual(invaders.SQUID.match(squid), 1)

if __name__ == '__main__':
    unittest.main()
