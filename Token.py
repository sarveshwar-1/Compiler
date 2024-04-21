class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        
    def __repr__(self):
        return f"<{self.type}>{self.value}</{self.type}>"
