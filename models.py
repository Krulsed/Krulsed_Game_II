class Team:
    def __init__(self, name: str, attack: float, defense: float, power_play: float, penalty_kill: float):
        self.name = name  # Название команды
        self.attack = attack  # Сила атаки (0-100)
        self.defense = defense  # Сила защиты (0-100)
        self.power_play = power_play  # Реализация большинства (%)
        self.penalty_kill = penalty_kill  # Нейтрализация меньшинства (%)

        # Статистика для таблицы
        self.points = 0  # Очки
        self.goals_for = 0  # Забитые шайбы
        self.goals_against = 0  # Пропущенные шайбы

    def results_of_game(self, goals_scored: int, goals_conceded: int, win: bool, ended_in_ot: bool):
        """Обновление статистики после матча с учетом правил КХЛ"""
        self.goals_for += goals_scored
        self.goals_against += goals_conceded

        if win:
            self.points += 2  # Победа в основное или ОТ/Б
        else:
            if ended_in_ot:
                self.points += 1  # Очко за поражение в ОТ/Б

    def __str__(self):
        return f"{self.name} (Ат: {self.attack}, Защ: {self.defense}, Очки: {self.points})"