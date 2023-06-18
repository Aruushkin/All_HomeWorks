from enum import Enum
from random import randint, choice


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    BLOCKED_DAMAGE = 5
    POWER = None
    REVIVE = 1
    BOOM_HEALTH = None
    UPDATE_DAMAGE = None


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
        return f'{self.name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.super_ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS defence: {self.__defence} ' + super().__str__()


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

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
        coeff = randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior hits critically {self.damage * coeff}')


class Magical(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_level):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_level = heal_level

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if self != hero and hero.health > 0:
                hero.health += self.__heal_level


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


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.POWER)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            damage_boss = boss.damage // 1.3
            for i in heroes:
                if i.health > 0:
                    i.health += damage_boss
                    print(f"{self.name} ЗАЩИЩАЕТ: {i.name}, Заблокировав урон на 80%")


class Deku(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.POWER)

    def apply_super_power(self, boss, heroes):
        power = randint(1, 6)
        if self.health >= 0:
            if power == 3:
                print(f"{self.name} СТАЛ СИЛЬНЫМ НА 100%")
                self.damage = self.damage * 2
            elif power == 2:
                print(f"{self.name} СТАЛ СИЛЬНЫМ НА 50%")
                self.damage = self.damage * 1.5
            elif power == 1:
                print(f"{self.name} СТАЛ СИЛЬНЫМ НА 20%")
                self.damage = self.damage * 1.2
            else:
                self.damage = self.damage


class Witcher(Hero):

    def __init__(self, name, health, damage, revive):
        super().__init__(name, health, damage, Ability.REVIVE)
        self.__revive = revive

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for i in heroes:
                if i.health <= 0:
                    print(f"ВЕДЬМАК ОЖИВИЛ {i.name} И ПОМЕР САМ")
                    self.health = 0
                    i.health = 150
                    break


class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOM_HEALTH)

    def apply_super_power(self, boss, heroes):
        if self.health <= 0:
            print("ТОЛСТЯК ВЗОРВАЛСЯ И НАНЕС 100 УРОНА БОССУ")
            boss.health -= 100

        else:
            print("Толсяк все еще жив")


class Reaper(Hero):
    def __init__(self, name, health, damage, updated_damage):
        super().__init__(name, health, damage, Ability.UPDATE_DAMAGE)
        self.__updated_damage = updated_damage

    @property
    def updated_damage(self):
        return self.__updated_damage

    @updated_damage.setter
    def updated_damage(self, value):
        self.__updated_damage += value

    def apply_super_power(self, boss, heroes):
        if self.health < 50 or self.health < 25:
            print("Жнец УВЕЛИЧИЛ УРОН")
            self.damage += 80



round_number = 0


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
        return True

    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)

    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f' ---------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def start_game():
    boss = Boss('Hitler', 2000, 80)

    warrior = Warrior('Arthur', 280, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    magic = Magical('Merlin', 270, 20)
    berserk = Berserk('Varvar', 300, 15)
    assistant = Medic('Aivo', 290, 5, 5)
    golem = Golem('Железный голем', 800, 1)
    deku = Deku("ДЕКЮ", 150, 5)
    witcher = Witcher("Ведьмак", 200, 4, 1)
    boomer = Bomber("Толстяк", 150, 3)
    reaper = Reaper("Жнец", 220, 5, 80)
    heroes_list = [warrior, doc, assistant, golem, deku, witcher, boomer, reaper]

    show_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
