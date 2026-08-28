# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: HealthTrack
import argparse

def main():
    parser = argparse.ArgumentParser(description="HealthTrack: Личный журнал самочувствия")
    sub = parser.add_subparsers(dest="command", help="Доступные команды")

    cmd_add = sub.add_parser("add", help="Добавить запись")
    cmd_add.add_argument("--type", choices=["measurement", "habit", "note", "weekly_report"], required=True)
    cmd_add.add_argument("--title", help="Название записи")
    cmd_add.add_argument("--body", help="Текст записи")
    cmd_add.add_argument("--date", help="Дата записи (YYYY-MM-DD)")

    cmd_show = sub.add_parser("show", help="Показать записи")
    cmd_show.add_argument("--filter", choices=["all", "measurement", "habit", "note", "weekly_report"], default="all")
    cmd_show.add_argument("--count", type=int, help="Количество записей для вывода")

    cmd_report = sub.add_parser("report", help="Недельный отчёт")
    cmd_report.add_argument("--from_date", help="Дата начала недели (YYYY-MM-DD)")
    cmd_report.add_argument("--to_date", help="Дата конца недели (YYYY-MM-DD)")

    args = parser.parse_args()

    if args.command == "add":
        from healthtrack_app import add_entry
        add_entry(args.type, args.title or "", args.body or "", args.date or "")
    elif args.command == "show":
        from healthtrack_app import get_entries
        entries = get_entries()
        filtered = entries if args.filter == "all" else [e for e in entries if e["type"] == args.filter]
        for entry in filtered[:args.count or len(filtered)]:
            print(f"[{entry['type']}] {entry['title']}: {entry['body']}")
    elif args.command == "report":
        from healthtrack_app import generate_weekly_report
        if args.from_date and args.to_date:
            report = generate_weekly_report(args.from_date, args.to_date)
        else:
            report = generate_weekly_report()
        print(report)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
