# -- coding: utf-8 --
# Scenery = Drzewiecki Design - EPKK Kraków

version = "1.1.0"
msfs_mode = 1
icao = "epkk"

main_apron = CustomizedName("Main Apron | Gate #§", 1)
main_apron_stand = CustomizedName("Main Apron | Stand #§", 1)
main_apron_de_ice = CustomizedName("Main Apron (De-ice) | Stand #§", 2)
military = CustomizedName("Military | Stand #§", 3)

@AlternativeStopPositions
def custom_stops_1(aircraftData):
    return Distance.fromMeters(2 if aircraftData.idMajor == 737 or aircraftData.idMajor == 320 else 0)

@AlternativeStopPositions
def custom_stops_3(aircraftData):
    distances = {
        0: 0,
        319: 0,
        320: 0,
        330: 4.7,
        340: 4.7,
        350: 4.7,
        747: 4.7,
        787: 7.6,
        777: 7.6
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 1.9))

@AlternativeStopPositions
def custom_stops_5(aircraftData):
    distances = {
        0: 0,
        330: 7.2,
        340: 7.2,
        747: 10.9,
        350: 10.9,
        777: 12.7,
        787: 12.7
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def custom_stops_9_12(aircraftData):
    distances = {
        0: 0,
        170: 2.5,
        175: 2.5,
        190: 2.5,
        195: 2.5,
        320: 5.3,
        737: 5.3
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))


@AlternativeStopPositions
def custom_stops_main(aircraftData):
    distances = {
        0: 0,
        170: 3,
        175: 3,
        190: 3,
        195: 3,
        320: 7.5,
        737: 7.5
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def custom_stops_22_35(aircraftData):
    distances = {
        0: 0,
        170: 3.3,
        175: 3.3,
        190: 3.3,
        195: 3.3,
        320: 4.5,
        737: 4.5
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def default_stop(aircraftData):
    return Distance.fromMeters(0)

parkings = {
    PARKING : {
        None : (military, )
    },
    W_PARKING : {
        None : (military, )
    },
    GATE : {
        None : (),
        1 : (main_apron_stand, custom_stops_1),
        2 : (main_apron_stand, custom_stops_1),
        3 : (main_apron, custom_stops_3),
        5 : (main_apron, custom_stops_5),
        6 : (main_apron, custom_stops_5),
        7 : (main_apron_stand, default_stop),
        9 : (main_apron_stand, custom_stops_9_12),
        10 : (main_apron_stand, custom_stops_9_12),
        11 : (main_apron_stand, custom_stops_9_12),
        12 : (main_apron_stand, custom_stops_9_12),
        13 : (main_apron_stand, custom_stops_main),
        14 : (main_apron_stand, custom_stops_main),
        15 : (main_apron_stand, custom_stops_main),
        16 : (main_apron_stand, custom_stops_main),
        17 : (main_apron_stand, default_stop),
        18 : (main_apron_stand, custom_stops_main),
        19 : (main_apron_stand, custom_stops_main),
        20 : (main_apron_stand, custom_stops_main),
        21 : (main_apron_stand, custom_stops_main),
        22 : (main_apron_de_ice, ),
        23 : (main_apron_stand, custom_stops_22_35),
        24 : (main_apron_stand, custom_stops_22_35),
        25 : (main_apron_stand, custom_stops_22_35),
        26 : (main_apron_de_ice, ),
        27 : (main_apron_de_ice, ),
        28 : (main_apron_de_ice, ),
        29 : (main_apron_de_ice, ),
        30 : (main_apron_de_ice, ),
        31 : (main_apron_stand, custom_stops_22_35),
        32 : (main_apron_stand, custom_stops_22_35),
        33 : (main_apron_stand, custom_stops_22_35),
        34 : (main_apron_stand, custom_stops_22_35),
        35 : (main_apron_stand, custom_stops_22_35)
    }
}