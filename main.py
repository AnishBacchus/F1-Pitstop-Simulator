
#Dictionarires for tracks and tire compounds

TRACKS = {
    "Spa": {
        "base_time": 100,
        "pit_stop_cost": 18.5,
        "degradation_rate": 1.20
    },

    "Melbourne": {
        "base_time": 80,
        "pit_stop_cost": 23,
        "degradation_rate": 0.90
    },

     "Suzuka": {
        "base_time": 84,
        "pit_stop_cost": 23.75,
        "degradation_rate": 1.30
    }
}

TIRES = {
    "soft": 1.5,
    "medium": 1.0,
    "hard": 0.7
}

def lap_time(track, tire_compound):
    return TRACKS[track]["base_time"] + actual_degradation_rate(track, tire_compound)


def actual_degradation_rate(track, tire_compound):
    return round(TRACKS[track]["degradation_rate"] * TIRES[tire_compound], 2)

