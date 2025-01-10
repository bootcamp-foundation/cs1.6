class Weapon:
    
    def __init__(self, model: str, demage: int, ammo: int) -> None:
        self.model = model
        self.demage = demage
        self.ammo = ammo

    def fire(self) -> None:
        if self.ammo != 0:
            self.ammo -= 1


class Player:
    health = 100

    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name = name
        self.weapon = weapon

    def shoot(self, player) -> None:
        if self.weapon.ammo > 0 and player.health > 0:
            self.weapon.fire()
            player.health -= self.weapon.demage
            if player.health <= 0:
                print(f"{self.name} killed {player.name} by {self.weapon.model}")
            return
        if self.weapon.ammo == 0:
            print("No Ammo")


class Counter(Player):
    team = "Counter-Terrorist"
    equipment = True

    def defuse(self) ->None:
        """Terrorist tomonidan qo'yilgan bombani zararsizlantirish harakatini bajaradi."""
        print(f"{self.team}: {self.name} defused the bomb")


class Terror(Player):
    team = "Terror"
    bomb = True

    def plant(self) -> None:
        """Bombani xaritaning belgilangan joyida qo'yadi."""
        print(f"{self.team}: {self.name} has planted bomb")
