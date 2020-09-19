class User:
    ranking = [i for i in range(-8, 9) if i != 0]
    level_progress = 100

    def __init__(self):
        self.rank_position = 0
        self.progress = 0

    @property
    def rank(self):
        return self.ranking[self.rank_position]

    def inc_progress(self, kata_rank):
        delta_rank = self.ranking.index(kata_rank) - self.rank_position
        if -2 < delta_rank < 0:
            self.progress += 1
        elif delta_rank == 0:
            self.progress += 3
        elif delta_rank > 0:
            self.progress += 10 * delta_rank ** 2
        self.level_update()

    def level_update(self):
        l = len(self.ranking)
        self.rank_position += self.progress // self.level_progress
        if self.rank_position > l - 1:
            self.rank_position %= l
            raise IndexError("Rank out")
        else:
            self.progress = self.progress % self.level_progress if self.rank_position < len(self.ranking) - 1 else 0
