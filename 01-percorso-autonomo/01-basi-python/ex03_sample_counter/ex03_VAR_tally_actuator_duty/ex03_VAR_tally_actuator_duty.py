"""
tally_actuator_duty_v1.py - Actuator State Duty Distribution Analyzer.
"""

def tally_actuator_duty(
    states_list: list[str], 
    ignore_token: str, 
    relative_rate: bool,
    ) -> dict[str, float]:

    # inizalizzazione
    output_dict: dict[str, float] = {}

    # verifica e elaborazione dei dati
    for state in states_list:
        # e' il dato da togliere? 
        if state == ignore_token:
            continue

        else: 
            output_dict[state] = output_dict.get(state, 0) + 1

    # blocco fianle: calcolo della distribuzione relativa se richiesto
    total_count = sum(output_dict.values())
    if relative_rate:
        for key, value in output_dict.items():
            output_dict[key] = float(value / total_count)

    return output_dict