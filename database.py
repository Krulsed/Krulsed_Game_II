import sqlite3

DB_NAME = "khl_manager.db"


def init_db():
    """Создает базу данных и таблицы, если их еще нет"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Таблица команд
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
    conn.close()


def save_team(team, conference_name):
    """Сохраняет или обновляет команду в базе данных"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO teams (name, conference, attack, defense, power_play, penalty_kill, points, goals_for, goals_against, matches_played)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(name) DO UPDATE SET
        points=excluded.points,
        goals_for=excluded.goals_for,
        goals_against=excluded.goals_against,
        matches_played=excluded.matches_played
    """, (
        team.name, conference_name, team.attack, team.defense,
        team.power_play, team.penalty_kill, team.points,
        team.goals_for, team.goals_against, team.matches_played
    ))

    conn.commit()
    conn.close()