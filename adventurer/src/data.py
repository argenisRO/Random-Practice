# Adventurer
# - Argenis Rodriguez


class Player:
    '''
    Player Class Containing All User Info
    - Player ID :
    - Name      :first|last
    - Sex       :pronoun|class_dialog
    - Height    :TBD
    - Class     :Stats
    '''
    # Global Player ID Counter
    ID = 0

    def __init__(self, name, sex, height, _class):
        self.name = name
        self.sex = sex
        self.height = height
        self._class = _class
        self.playerID = self.ID
        Player.ID += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_height(self):
        return self.height

    def get_class(self):
        return self._class

    def get_class_dialog(self):
        if (self._class).lower() == 'warrior':
            return 'The Fierce Warrior'
        elif (self._class).lower() == 'berserker':
            return 'The Mighty Berserker'
        elif (self._class).lower() == 'archer':
            return 'The Swift Archer'
        elif (self._class).lower() == 'mage':
            return 'The Intelligent Mage'
        elif (self._class).lower() == 'priest':
            return 'The Caring Priest'
        else:
            return '(__INVALID CLASS RETURNED__)'

    def get_id(self):
        return self.playerID

    def get_pronoun(self):
        if (self.sex).lower() in ['male', 'm']:
            return ['he', 'him', 'his']
        elif (self.sex).lower() in ['female', 'f']:
            return ['she', 'her', 'hers']
        else:
            return ['they', 'them', 'theirs']


class Monster:
    '''
    Monster Class Containing Info About Each Monster

    Monster ID
    Name
    Attack Points
    Defense Points
    Monster HP
    '''
    # Global Monster ID Counter
    ID = 0

    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.monsterID = self.ID
        Monster.ID += 1

    def get_name(self):
        return self.name

    def get_ap(self):
        return self.attack

    def get_dp(self):
        return self.defense

    def get_id(self):
        return self.monsterID

    def get_hp(self):
        return self.hp
