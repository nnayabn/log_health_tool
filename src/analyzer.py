def summarize_logs(logs):
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for log in logs:
        level = log.get("level")
        if level in summary:
            summary[level] += 1
    return summary

if __name__ == "__main__":
    from loader import load_logs
    logs = load_logs()
    summary = summarize_logs(logs)
    print("Log Summary:")
    for level, count in summary.items():
        print(f"{level}: {count}")
