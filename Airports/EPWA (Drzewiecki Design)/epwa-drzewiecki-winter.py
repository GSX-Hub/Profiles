# -- coding: utf-8 --
# Scenery = Drzewiecki Design - EPWA Warszawa-Chopin

version = "1.2.1"
msfs_mode = 1
icao = "epwa"

apron_1 = CustomizedName("Apron 1 | Stand #§", 1)
apron_2 = CustomizedName("Apron 2 | Stand #§", 2)
apron_3 = CustomizedName("Apron 3 | Gate #§", 3)
apron_5 = CustomizedName("Apron 5 | Stand #§", 4)
apron_7 = CustomizedName("Apron 7 (Cargo) | Stand #§", 5)
apron_7_de_ice = CustomizedName("Apron 7 (De-ice)| Stand #§", 6)
apron_9 = CustomizedName("Apron 9 | Stand #§", 7)
apron_10 = CustomizedName("Apron 10 | Stand #§", 8)
apron_11 = CustomizedName("Apron 11 | Stand #§", 9)
apron_12 = CustomizedName("Apron 12 (Cargo) | Ramp #§", 10)
apron_13 = CustomizedName("Apron 13 (De-ice) | Stand #§", 12)
cargo = CustomizedName("Cargo Apron | Ramp #§", 13)
military = CustomizedName("Military Apron | Stand #§", 14)

@AlternativeStopPositions
def default_stop(aircraftData):
    return Distance.fromMeters(0)

@AlternativeStopPositions
def custom_stops_2(aircraftData):
    distances = {
        0: 0,
        321: 1.9,
        757: 1.9,
        767: 1.9
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def custom_stops_9(aircraftData):
    distances = {
        0: 0,
        "ARC-D": 2.7,
        "ARC-E": 6.1,
        "ARC-F": 6.1
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_10(aircraftData):
    distances = {
        0: 0,
        "ARC-C": 1.1,
        "ARC-D": 3.2,
        "ARC-E": 6.1,
        "ARC-F": 6.1
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_11(aircraftData):
    distances = {
        0: 0,
        "ARC-D": 4.3,
        "ARC-E": 10.5,
        "ARC-F": 11.8
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_13(aircraftData):
    distances = {
        0: 0,
        "ARC-D": 4.7,
        "ARC-E": 4.7,
        "ARC-F": 4.7
    }

    return Distance.fromMeters(distances.get(aircraftData.aircraftGroup, 0))

@AlternativeStopPositions
def custom_stops_17(aircraftData):
    distances = {
        0: 0,
        321: 2,
        757: 2,
        767: 2
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

parkings = {
    PARKING : {
        None : (military, ),
        61 : (cargo, default_stop),
        63 : (cargo, default_stop),
        80 : (apron_1, ),
        81 : (apron_1, default_stop),
        83 : (apron_1, default_stop),
        84 : (apron_1, ),
        87 : (apron_1, default_stop),
        88 : (apron_1, ),
        201 : (apron_2, ),
        202 : (apron_2, ),
        203 : (apron_2, )
    },
    N_PARKING : {
        None : (apron_11, )
    },
    GATE : {
        None : (),
        1 : (apron_3, default_stop),
        2 : (apron_3, custom_stops_2),
        3 : (apron_3, default_stop),
        4 : (apron_3, default_stop),
        5 : (apron_3, default_stop),
        6 : (apron_3, custom_stops_2),
        7 : (apron_3, custom_stops_2),
        8 : (apron_3, default_stop),
        9 : (apron_3, custom_stops_9),
        10 : (apron_3, custom_stops_10),
        11 : (apron_3, custom_stops_11),
        13 : (apron_3, custom_stops_13),
        14 : (apron_3, custom_stops_13),
        16 : (apron_3, default_stop),
        17 : (apron_3, custom_stops_17),
        18 : (apron_3, custom_stops_17),
        19 : (apron_3, custom_stops_17),
        20 : (apron_3, custom_stops_17),
        21 : (apron_3, custom_stops_17),
        22 : (apron_3, custom_stops_17),
        23 : (apron_3, custom_stops_17),
        24 : (apron_3, custom_stops_17),
        25 : (CustomizedName("Apron 3 | Stand #", 3), default_stop),
        31 : (apron_5, default_stop),
        32 : (apron_5, default_stop),
        33 : (apron_5, default_stop),
        34 : (apron_5, default_stop),
        35 : (apron_5, default_stop),
        36 : (apron_5, default_stop),
        37 : (apron_5, default_stop),
        38 : (apron_5, default_stop),
        39 : (apron_5, default_stop),
        40 : (apron_5, default_stop),
        41 : (apron_5, default_stop),
        42 : (apron_5, default_stop),
        47 : (apron_5, default_stop),
        48 : (apron_5, default_stop),
        "53B" : (apron_10, default_stop),
        "54A" : (apron_10, default_stop),
        "54B" : (apron_10, default_stop),
        "64L" : (apron_12, default_stop),
        "64R" : (apron_12, default_stop),
        65 : (apron_12, default_stop),
        66 : (apron_12, default_stop),
        71 : (apron_7_de_ice, ),
        72 : (apron_7_de_ice, ),
        75 : (apron_7, default_stop),
        76 : (apron_7, default_stop),
        91 : (apron_9, default_stop),
        92 : (apron_9, default_stop),
        93 : (apron_9, default_stop),
        94 : (apron_9, default_stop),
        95 : (apron_9, default_stop),
        96 : (apron_9, default_stop),
        97 : (apron_9, default_stop),
        98 : (apron_9, default_stop),
        101 : (apron_13, ),
        102 : (apron_13, ),
        103 : (apron_13, ),
        104 : (apron_13, ),
        105 : (apron_13, ),
        704 : (apron_7_de_ice, ),
        705 : (apron_7_de_ice, ),
        706 : (apron_7_de_ice, ),
        707 : (apron_7_de_ice, ),
        712 : (apron_7, default_stop)
    },
    GATE_L : {
        None : (CustomizedName("Apron 3 | Gate 15L", 3), default_stop)
    },
    GATE_R : {
        None : (CustomizedName("Apron 3 | Gate 15R", 3), default_stop)
    }
}