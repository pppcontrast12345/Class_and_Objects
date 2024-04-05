from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("hero", 1, 100, 100)
        self.enemy = Hero("enemy", 1, 50, 50)

    def test_correct_init_for_hero(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_enemy_username_has_the_same_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.enemy.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_equals_to_zero_raise_value_error(self):
        self.hero.health = 0
        expected_string = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ve.exception))

    def test_battle_enemy_health_fight_with_zero_hp_raise_value_error(self):
        self.enemy.health = 0
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ve.exception))

    def test_battle_with_result_draw_returns_draw_decrease_health_on_both_players(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_battle_fight_enemy_and_win_expect_stats_increase(self):
        expected_level = self.hero.level + 1
        expected_damage = self.hero.damage + 5
        expected_health = self.hero.health - self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_fight_hero_and_lose_expect_and_stats_increase(self):
        self.hero, self.enemy = self.enemy, self.hero

        expected_level = self.enemy.level + 1
        expected_damage = self.enemy.damage + 5
        expected_health = self.enemy.health - self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct__str__method(self):
        expected_string = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_string, self.hero.__str__())



if __name__ == "__name__":
    main()