# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: HealthTrack
import unittest


class TestHealthTrack(unittest.TestCase):
    """Базовые unit-тесты для HealthTrack."""

    def test_weekly_report_creation(self):
        from models import WeeklyReport, DayRecord
        dr1 = DayRecord(day=1, mood='good', energy=80, hydration=2.0)
        dr2 = DayRecord(day=2, mood='ok', energy=75, hydration=1.5)
        dr3 = DayRecord(day=3, mood='bad', energy=60, hydration=1.0)
        report = WeeklyReport(week_start=dr1.day, records=[dr1, dr2, dr3])
        self.assertEqual(report.week_start, 1)
        self.assertEqual(len(report.records), 3)

    def test_record_mood_validation(self):
        from models import DayRecord
        with self.assertRaises(ValueError):
            DayRecord(day=1, mood='invalid', energy=80, hydration=2.0)

    def test_report_average_energy(self):
        from models import WeeklyReport, DayRecord
        dr = [DayRecord(day=i, mood='ok', energy=50 + i * 10, hydration=2.0) for i in range(7)]
        report = WeeklyReport(week_start=1, records=dr)
        self.assertAlmostEqual(report.average_energy(), 65.0)

    def test_add_record_to_report(self):
        from models import WeeklyReport, DayRecord
        dr1 = [DayRecord(day=i, mood='ok', energy=70, hydration=2.0) for i in range(3)]
        report = WeeklyReport(week_start=1, records=dr1)
        self.assertEqual(len(report.records), 3)

    def test_note_addition(self):
        from models import Note
        note = Note(text='Тестовая заметка', timestamp='2024-01-01')
        self.assertIn('Тестовая заметка', str(note))


if __name__ == '__main__':
    unittest.main()
