class Human:
    name: str
    weight: float
    age: int
    is_has_couple: bool
    friends: list

    def __init__(self,
    name: str,
    weight: float,
    age: int,
    is_has_couple: bool,
    *friends,) -> None:
        self.name = name
        self.weight = weight
        self.age = age
        self.is_has_couple = is_has_couple
        self.friends = []
        for friend in friends:
            self.friends.append(friend)

    def __str__(self) -> str:
        return (f'Человек по имени {self.name} имеет вес {self.weight}, возраст {self.age}, {"не " if not self.is_has_couple else ""}состоит в отношениях, дружит с {", ".join(self.friends)}')

    def make_new_friend(self, friend: str) -> None:        
        self.friends.append(friend)        
        print(f"теперь {friend} новый друг {self.name}!")
    
    def remove_friend(self, friend: str) -> None:
        try:
            self.friends.remove(friend)
        except ValueError:
            print(f"{self.name} не имел друга по имени {friend}!")
            return None
        print(f"{self.name} больше не дружит с {friend}!")
    
    def enumerate_friends(self) -> None:
        print(f'{self.name} дружит с {", ".join(self.friends)}')

    def change_name(self, new_name: str) -> None:
        if new_name != self.name:
            print(f"теперь {self.name} зовут {new_name}!")
            self.name = new_name 
        else:
            print(f"новое имя не отличается от старого, изменения не произошло")

    def break_up(self) -> None:
        if self.is_has_couple:
            print(f"{self.name} больше не состоит в отношениях")
            self.is_has_couple = False
        else:
            print(f"{self.name} и так не состоит в отношениях, расставаться не с кем")

    def start_relationship(self) -> None:
        if self.is_has_couple:
            print(f"{self.name} уже состоит в отношениях, нельзя создать новые")
        else:
            print(f"{self.name} теперь состоит в отношениях!")
            self.is_has_couple = True
    
    def grow(self) -> None:
        self.age += 1
        print(f"теперь {self.name} на год старше! ({self.age})")

    def eat(self) -> None:
        self.weight = round(self.weight + 0.5, 3)
        print(f"теперь {self.name} весит на 0,5 кг больше! ({self.weight})")

    def eat_a_lot(self) -> None:
        self.weight = round(self.weight + 1, 3)
        print(f"{self.name} объелся, теперь {self.name} весит на 1 кг больше! ({self.weight})")

    def sport(self) -> None:
        self.weight = round(self.weight - 0.3, 3)
        print(f"{self.name} занялся спортом, теперь {self.name} похудел на 0,3 кг! ({self.weight})")
    

    