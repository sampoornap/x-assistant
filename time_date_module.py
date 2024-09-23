from datetime import datetime

def get_system_time():
    """Return the current system time as a string."""
    return datetime.now().strftime("%H:%M:%S")

def get_system_date():
    """Return the current system date as a string."""
    return datetime.now().strftime("%Y-%m-%d")
