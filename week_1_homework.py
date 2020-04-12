class Person:
    """
    Attrs:
        height (int): in cm
        name (str): First and last
        strength (int): How strong the person is 
        health_points (int): Out of 100 (everyone starts at 100)
    """
    def __init__(self, height: int, name: str, strength: int, health_points = 100):
        """initialized the variables"""

        self.height = height
        self.name = name
        self.strength = strength
        self.health_points = health_points
    
    def __str__(self) -> str:
        """return a text.

        Args: 
            self
        
        Returns: 
            str
        """
        return f"{self.name}: {self.health_points}"
    
    def introduce(self) -> str:
        """display message of the class.

        Args: 
            self

        Returns: 
            str
        """
        return f"Hello, my name is {self.name}"

    def punch(self, person: 'Person') -> None:
        """reduce 10 health point from the person.

        Args: 
            self
            person: Person
        
        Returns: 
            None
        """
        person.health_points -= 10

    def eat(self) -> None:
        """recover the health point to 100.

        Args: 
            self
        
        Returns: 
            None
        """
        self.health_points = 100

Jack = Person(163, "Jack", 50)
Peter = Person(178, "Peter", 70)

print(Jack)
print(Peter)
print(Jack.introduce())
print(Peter.introduce())
Jack.punch(Peter)
Peter.punch(Jack)
print(Jack)
print(Peter)
Jack.eat()
Peter.eat()
print(Jack)
print(Peter)
