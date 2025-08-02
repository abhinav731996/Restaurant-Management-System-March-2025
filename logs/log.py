import datetime
import os
import traceback

def error_logs(data, error_type="Exception", extra_info=None):
    # Ensure logs folder exists
    os.makedirs("logs", exist_ok=True)

    # Current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Header for each log entry
    log_entry = [
        "\n" + "=" * 80,
        f"🕒 TIMESTAMP : {timestamp}",
        f"❌ ERROR TYPE: {error_type}",
        f"📄 MESSAGE    : {data}",
    ]

    if extra_info:
        log_entry.append(f"🧾 EXTRA INFO : {extra_info}")

    # Add traceback if available
    if isinstance(data, BaseException):
        log_entry.append("🔍 TRACEBACK  :")
        log_entry.append(traceback.format_exc())

    log_entry.append("=" * 80 + "\n")

    # Write to file
    with open("logs/log.txt", "a") as file:
        file.write("\n".join(log_entry))