import random
from enum import Enum
from random import randint, choice


class Ability(Enum):
    BOOST = 1
    HEAL = 2
    CRITICAL_DAMAGE = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    FREEZE_BOSS = 5
    INVISIBILITY = 6
    THE_SIZE = 7
    REVIVE = 8
    ANGEL = 9


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} Health: {self.__health} Damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        self.__defence = random.choice(heroes).super_ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' Defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if isinstance(super_ability, Ability):
            self.__super_ability = super_ability
        else:
            raise ValueError('Wrong value for super_ability')

    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 6)  # 2,3,4,5,6
        if boss.health > 0:
            boss.health -= self.damage * coefficient
            print(f'Warrior hits critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
       pass

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        pass


class Thor(Hero):

    def __init__(self, name, hp, damage):
        Hero.__init__(self, name, hp, damage, Ability.FREEZE_BOSS)

    def apply_super_power(self, boss, heroes):
        random_freeze = [1, 2, 3, 4, 5]
        freeze = random.choice(random_freeze)
        if freeze == 3:
            self.health += 50


class Avrora(Hero):

    def __init__(self, name, hp, damage, invisibility=1):
        super().__init__(name, hp, damage, Ability.INVISIBILITY)
        self.invisibility = invisibility

    def apply_super_power(self, boss, heroes):
        invisibility = [1, 2, 3]
        if invisibility == 2:
            self.hp += 150
            save_range = [10, 12, 15]
            saved = random.choice(save_range)
            self.hp += saved
            boss.hp -= saved


class AntMan(Hero):

    def __init__(self, name, hp, damage, the_size=1):
        super(). __init__(name, hp, damage, Ability.THE_SIZE)
        self.the_size = the_size

    def apply_super_power(self, boss, heroes):
        random_size = [1, 2, 3, 4, 5]
        if random_size == 5:
            self.hp += 150
            self.damage += 8


class Witcher(Hero):

    def __init__(self, name, hp, damage, revive_point):
        Hero.__init__(self, name, hp, damage, Ability.REVIVE)
        self.revive_point = revive_point

    def apply_super_power(self, boss, heroes):
        health = 1
        self.damage = 0
        for hero in heroes:
            if health >= 0 and hero.health >= 0:
                if hero.health == 0 and self != hero:
                    self.health += hero.health


class Druid(Hero):

    def __init__(self, name, hp, damage, angel):
        super().__init__(name, hp, damage, Ability.ANGEL)
        self.angel = angel

    def apply_super_power(self, boss, heroes):
        random_assistant = [1, 2, 3, 4, 5]
        for i in heroes:
            if random_assistant == 3:
                i.hp += 3
                i.damage += 3





round_number = 0


def start():
    boss = Boss('Dantes', 1000, 50)
    warrior = Warrior('Ahiles', 290, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    magic = Magic('Hendolf', 280, 15)
    berserk = Berserk('Valkiria', 270, 10)
    assistant = Medic('Strange', 280, 5, 5)
    thor = Thor('Tor', 270, 50)
    avrora = Avrora('Sirena', 250, 15)
    antman = AntMan('Муравей', 240, 15)
    witcher = Witcher('Ведьмак', 260, 15, 20)
    druid = Druid('Shrek', 240, 15, 5)
    heroes_list = [warrior, doc, magic, berserk, assistant, thor, avrora, antman, witcher, druid]

    show_stats(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


def show_stats(boss, heroes):
    print(f'---------- ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 \
                and hero.super_ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


start()
