def conta_tipo(registro: list) -> dict:

    # inizializzazione
    dict_tipo: dict = {}

    # elaborazione
    for allarme in registro:
        dict_tipo[allarme] = dict_tipo.get(allarme, 0) + 1

    return dict_tipo


def conta_priorita(registro: list) -> dict:

    # inizializzazione
    priorita = {
        "saturazione": "alta",
        "frequenza": "alta",
        "sensore staccato": "media",
        "batteria": "bassa"
    }

    dict_conta_priorita: dict = {}

    # elaborazione
    for allarme in registro:
        # leggo priorita di appartenenza
        key_count_priorita = priorita.get(allarme, "sconosciuta")
        # aggiorno/creo conteggio
        dict_conta_priorita[key_count_priorita] = dict_conta_priorita.get(key_count_priorita, 0) + 1

    return dict_conta_priorita


if __name__ == "__main__":

    # inizializzazione
    # ALLARMI_NOTTE = ["saturazione", "sensore staccato", "saturazione", "batteria", "saturazione", "frequenza"]
    ALLARMI_NOTTE = ["saturazione", "sensore staccato", "porta aperta", "batteria", "saturazione", "frequenza"]
    # ALLARMI_NOTTE = []
    # ALLARMI_NOTTE = ["saturazione", "batteria", "saturazione", "frequenza"]

    # elaborazione
    print(conta_tipo(ALLARMI_NOTTE))
    print(conta_priorita(ALLARMI_NOTTE))
