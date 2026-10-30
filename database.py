import sqlite3  # Беру библиотеку для работы с базами данных
from models import Team,Conference  # Импортируем класс Team для подсказки типов

DB_NAME = "khl_manager.db"  # Название базы данных


def init_db():
    """
    Создание таблицы команды если таблица еще не существует
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            conference TEXT NOT NULL,
            attack REAL,
            defense REAL,
            power_play REAL,
            penalty_kill REAL,
            points INTEGER DEFAULT 0,
            goals_for INTEGER DEFAULT 0,
            goals_against INTEGER DEFAULT 0,
            matches_played INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()  # Исправлено: con -> conn


def save_team(team: Team, conference_name: str):
    """
    Информация про команду закидывается в таблицу и
    если команда уже есть, то обновляется её стата
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
         INSERT INTO teams (
             name, conference, attack, defense, 
             power_play, penalty_kill, points, 
             goals_for, goals_against, matches_played
         )
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
         ON CONFLICT(name) DO UPDATE SET
             points = excluded.points,
             goals_for = excluded.goals_for,
             goals_against = excluded.goals_against,
             matches_played = excluded.matches_played
    """, (
        team.name,
        conference_name,
        team.attack,
        team.defense,
        team.power_play,
        team.penalty_kill,
        team.points,
        team.goals_for,
        team.goals_against,
        team.matches_played
    ))

    conn.commit()
    conn.close()


def load_conference(conf_name: str):
    """
    Загружает данные команд конкретной конференции из базы данных
    и восстанавливает их в виде объектов классов Conference и Team.
    """
    # Cоздание обьекта конференции
    conf = Conference(conf_name)

    # Подключаемся к базе и берем курсор
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Делаем запрос на выборку команд только для этой конференции
    cursor.execute("""
        SELECT name, attack, defense, power_play, penalty_kill, 
               points, goals_for, goals_against, matches_played 
        FROM teams 
        WHERE conference = ?
    """, (conf_name,))

    #Забираем все данные
    rows = cursor.fetchall()

    # Закрываем соединение
    conn.close()

    # Проходим по каждой строчке и превращаем её в инфу про команду
    for row in rows:
        team = Team(
            name=row[0],
            attack=row[1],
            defense=row[2],
            power_play=row[3],
            penalty_kill=row[4]
        )
        # Восстанавливаем накопленную статистику матчей
        team.points = row[5]
        team.goals_for = row[6]
        team.goals_against = row[7]
        team.matches_played = row[8]

        # Добавляем готовую команду в конференцию
        conf.add_team(team)

    # Возвращаем полностью собранную конференцию с объектами
    return conf