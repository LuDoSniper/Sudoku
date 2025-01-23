class Char:
    def __init__(self, char: str, fore: str = None, back: str = None) -> None:
        self.char = char
        self.fore = fore
        self.back = back
    
    def __str__(self) -> str:
        return f"{self.fore if self.fore else ''}{self.back if self.back else ''}{self.char}"