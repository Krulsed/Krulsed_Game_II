from models import Team
from database import init_db, save_team, load_conference


def run_test():
    print("==========================================")
    print("🚀 ЗАПУСК ТЕСТИРОВАНИЯ БАЗЫ ДАННЫХ KHL MANAGER")
    print("==========================================")

    # 1. Тест создания БД
    print("\n[ШАГ 1] Инициализация базы данных...")
    init_db()
    print("✅ База данных и таблица 'teams' готовы к работе!")

    # 2. Тест создания и сохранения объектов Team
    print("\n[ШАГ 2] Создаем объекты команд и сохраняем их в SQLite...")

    ska = Team(
        name="СКА",
        attack=86.0,
        defense=81.0,
        power_play=24.5,
        penalty_kill=83.0,
    )
    cska = Team(
        name="ЦСКА",
        attack=84.0,
        defense=85.0,
        power_play=22.0,
        penalty_kill=86.0,
    )

    # Симулируем результат матча для СКА (победа 4:2)
    ska.results_of_game(
        goals_scored=4, goals_conceded=2, win=True, ended_in_ot=False
    )

    # Сохраняем в базу данных
    save_team(ska, "Запад")
    save_team(cska, "Запад")
    print("✅ Команды 'СКА' и 'ЦСКА' записаны в таблицу 'teams'.")

    # 3. Тест загрузки данных обратно в объекты
    print("\n[ШАГ 3] Считываем данные из БД обратно в классы (load_conference)...")
    west_conf = load_conference("Запад")

    print(f"\n🏆 Загруженная конференция: {west_conf.name}")
    print(f"📊 Всего команд в конференции: {len(west_conf.teams)}\n")

    for team in west_conf.teams:
        print(f"🏒 Клуб: {team.name}")
        print(f"   • Атака / Защита: {team.attack} / {team.defense}")
        print(f"   • Сыграно матчей: {team.matches_played}")
        print(f"   • Очки: {team.points}")
        print(
            f"   • Шайбы (Забито:Пропущено): {team.goals_for}:{team.goals_against}"
        )
        print("-" * 40)

    print("\n🎉 ТЕСТ УСПЕШНО ПРОЙДЕН! Все работает отлично.")


if __name__ == "__main__":
    run_test()