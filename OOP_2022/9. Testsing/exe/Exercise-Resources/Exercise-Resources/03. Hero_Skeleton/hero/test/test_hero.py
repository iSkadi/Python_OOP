from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username1 = "first_hero"
    health1 = 100
    damage1 = 30
    level1 = 15

    username2 = "enemy_hero"
    health2 = 90
    damage2 = 60
    level2 = 15


    level_up = 1
    health_up = 5
    damage_up = 5

    def setUp(self) -> None:
        self.first_hero = Hero(self.username1, self.level1, self.health1, self.damage1)
        self.enemy_hero = Hero(self.username2, self.level2, self.health2, self.damage2)

    def test_init(self):

        self.assertEqual(self.username1, self.first_hero.username)
        self.assertEqual(self.health1, self.first_hero.health)
        self.assertEqual(self.damage1, self.first_hero.damage)
        self.assertEqual(self.level1, self.first_hero.level)

    def test_battle_Ex_1(self):

        self.enemy_hero.username = "first_hero"

        with self.assertRaises(Exception) as ex:
            self.enemy_hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_Ex2(self):

        self.first_hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.first_hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_Ex3(self):

        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.first_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))



    def test_first_win(self):
        self.enemy_hero.health = 1
        self.enemy_hero.damage = 1


        result = self.first_hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(self.level1 + self.level_up, self.first_hero.level)
        self.assertEqual(self.health1 + self.health_up - (self.enemy_hero.level * self.enemy_hero.damage),
                         self.first_hero.health)
        self.assertEqual(self.damage1 + self.damage_up, self.first_hero.damage)

    def test_first_lose(self):
        self.first_hero.health = 1
        self.first_hero.damage = 1
        result = self.first_hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual((self.level2 + self.level_up), self.enemy_hero.level)
        self.assertEqual(self.health2 + self.health_up - (self.first_hero.level * self.first_hero.damage),
                         self.enemy_hero.health)
        self.assertEqual(self.damage2 + self.damage_up, self.enemy_hero.damage)

    def test_Draw(self):
        self.first_hero.health = 1
        self.enemy_hero.health = 1
        rerult = self.first_hero.battle(self.enemy_hero)
        expetted_hp = self.first_hero.health - (self.enemy_hero.level * self.enemy_hero.damage)
        self.assertEqual("Draw", rerult)

    def test_str_(self):

        self.assertEqual(f"Hero {self.first_hero.username}: {self.first_hero.level} lvl\n" \
               f"Health: {self.first_hero.health}\n" \
               f"Damage: {self.first_hero.damage}\n", self.first_hero.__str__())





if __name__ == "__main__":
    main()
