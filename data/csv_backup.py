"""CSV backup export for lead data"""
import csv
from datetime import datetime
from pathlib import Path

class CSVBackup:
    def __init__(self, backup_dir: str = "backups"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def export_leads(self, leads: list) -> str:
        """Export leads to CSV file"""
        now = datetime.now()
        filename = f"leads_{now.strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = self.backup_dir / filename

        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                if not leads:
                    return str(filepath)
                
                fieldnames = [
                    'date', 'name', 'mobile', 'reg_no', 'car_model', 'variant',
                    'year', 'km', 'address', 'follow_up', 'source', 'context',
                    'license', 'remark'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead)
            
            return str(filepath)
        except Exception as e:
            print(f"CSV export error: {e}")
            return None

    def weekly_backup(self, conn) -> str:
        """Export all leads for weekly backup"""
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM leads')
            leads = [dict(row) for row in cursor.fetchall()]
            return self.export_leads(leads)
        except Exception as e:
            print(f"Weekly backup error: {e}")
            return None
