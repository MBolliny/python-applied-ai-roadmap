def update_session_data(sessions: dict[str, dict], session_id: str, temp: float, ph: float) -> None:

	# inizializzazione
    if session_id not in sessions:
        sessions[session_id] = {
            "valid_sample": 1,
            "max_temp_celsius": float('-inf'),
            "min_temp_celsius": float('inf'),
            "avg_temp_celsius": 0.0,
            "ph": 0.0
        }

    else:
        sessions[session_id]["valid_sample"] += 1
        sessions[session_id]["max_temp_celsius"] = max(sessions[session_id]["max_temp_celsius"], temp)
        sessions[session_id]["min_temp_celsius"] = min(sessions[session_id]["min_temp_celsius"], temp)
        sessions[session_id]["avg_temp_celsius"] = (sessions[session_id]["avg_temp_celsius"] * (sessions[session_id]["valid_sample"] - 1) + temp) / sessions[session_id]["valid_sample"]
        sessions[session_id]["ph"] = ph


if __name__ == "__main__":
    session_data = {}

    test_runs = [
        ("RUN-01", 1700000000, 37.0, 7.2),
        ("RUN-01", 1700000010, 39.5, 7.4),
        ("RUN-02", 1700000000, 36.8, 6.9),
    ]

    for run_id, _ts, temp, ph in test_runs:
        update_session_data(session_data, run_id, temp, ph)

    print(session_data)