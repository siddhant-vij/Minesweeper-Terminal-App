class Cell:
    def __init__(self):
        self.is_revealed = False
        self.is_mine = False        
        self.mine_type = None
        self.is_flagged = False
        self.is_question_marked = False
        self.adjacent_mines = 0
