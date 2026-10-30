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
        self.matches_played = 0  # Сыгранные матчи (добавлено!)

    def results_of_game(self, goals_scored: int, goals_conceded: int, win: bool, ended_in_ot: bool):
        """
        Обновление статистики после матча с учетом правил КХЛ
        """

        self.goals_for += goals_scored
        self.goals_against += goals_conceded
        self.matches_played += 1  # Увеличиваем счетчик сыгранных матчей на 1

        if win:
            self.points += 2  # Победа в основное или ОТ/Б
        else:
            if ended_in_ot:
                self.points += 1  # Очко за поражение в ОТ/Б

    def __str__(self):
        return f"{self.name} (Нап: {self.attack}, Защ: {self.defense}, Очки: {self.points})"


class Conference:  #
    def __init__(self, name: str):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)