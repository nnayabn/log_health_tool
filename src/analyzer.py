def summarize_logs(logs):
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for log in logs:
        level = log.get("level")
        if level in summary:
            summary[level] += 1
    return summary

# Feature: group logs by hour
def group_logs_by_hour(logs):
    grouped = {}
    for log in logs:
        hour = log["timestamp"][:13]  # YYYY-MM-DD HH
        grouped.setdefault(hour, []).append(log)
    return grouped

if __name__ == "__main__":
    from loader import load_logs
    logs = load_logs()

    # Existing summary
    summary = summarize_logs(logs)
    print("Log Summary:")
    for level, count in summary.items():
        print(f"{level}: {count}")

    # Time-based grouping
    grouped = group_logs_by_hour(logs)
    print("\nLogs grouped by hour:")
    for hour, group in grouped.items():
        print(f"{hour}: {len(group)} logs")
