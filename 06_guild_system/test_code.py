expected_level = self.hero.level + 1
expected_health = self.hero.health + 5
expected_damage = self.hero.damage - self.enemy.damage + 5

result = self.hero.battle(self.enemy)

self.assertEqual("You win", result)
self.assertEqual(expected_level, self.hero.level)
self.assertEqual(expected_health, self.hero.health)
self.assertEqual(expected_damage, self.hero.damage)


expected_level = self.hero.level + 1
expected_health = self.hero.health + 5
expected_damage = self.hero.damage - self.enemy.damage + 5

result = self.hero.battle(self.enemy)

self.assertEqual("You win", result)
self.assertEqual(expected_level, self.hero.level)
self.assertEqual(expected_health, self.hero.health)
self.assertEqual(expected_damage, self.hero.damage)