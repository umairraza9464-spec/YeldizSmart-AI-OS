from datetime import datetime, time
import pytz

IST = pytz.timezone("Asia/Kolkata")

def is_work_time() -> bool:
    """Check if current time is within work window (4 AM - 12 PM IST)"""
    now = datetime.now(IST).time()
    start = time(4, 0)
    end = time(12, 0)
    return start <= now <= end

def pause_outside_work_window(pause_flag: bool) -> bool:
    """Return True if should pause (not in work window)"""
    return not is_work_time()

class WorkScheduler:
    def __init__(self):
        self.paused = False

    def should_continue(self) -> bool:
        """Check if scheduler should continue running"""
        if not is_work_time():
            self.paused = True
            return False
        self.paused = False
        return True
