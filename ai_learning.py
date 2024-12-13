class AILearning:
    def __init__(self):
        self.move_history = []
        self.winning_patterns = {}
        
    def record_move(self, board_state, move, result):
        self.move_history.append({
            'board': board_state,
            'move': move,
            'result': result
        })
        
    def learn_from_game(self):
        if self.move_history[-1]['result'] == 'win':
            for move in self.move_history:
                board_key = str(move['board'])
                if board_key not in self.winning_patterns:
                    self.winning_patterns[board_key] = []
                self.winning_patterns[board_key].append(move['move']) 