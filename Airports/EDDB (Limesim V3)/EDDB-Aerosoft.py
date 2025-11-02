# -- coding: utf-8 --

msfs_mode = 1
icao = "eddb"
version = 1.2

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
    major_id = aircraftData.idMajor
    minor_id = aircraftData.idMinor

    if major_id in specificTables:
        specific_table, fallback_key = specificTables[major_id]
        result = specific_table.get(minor_id)
        if result is None:
            result = specific_table.get(fallback_key)
    else:
        result = genericTable.get(major_id, 0)

    return result

@AlternativeStopPositions
def MyCustomOffsetsA01to10(aircraftData):

    table = {
        0: 0,
        318: -1.9,
        319: -1.9,
        321: 2.9,
        717: 2.9,
        87: 2.9,
        80: 7.9,
        90: 7.9,
        700: 2.9,
        900: 2.9,
        146: -1.9
        
        }

    table737 = {
        0: 0,
        400: 2.9,
        500: -1.9,
        600: -1.9,
        800: 2.9,
        900: 2.9,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsB(aircraftData):

    table = {
        0: 0,
        318: -1.5,
        319: -1.5,

        146: -1.5,
        80: -1.5,
        90: -1.5,
        
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {

        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsBa(aircraftData):

    table = {
        0: 0,
        300: -6.1,
        310: -6.1,

        
    }
    
    table330 = {
        0: 0,
        200: -4.3,
    }

    table340 = {
        0: 0,
        600: 7.6,
    }

    table350 = {
        0: 1.6,
        1000: 7.6,
    }

    table767 = {
        0: 0,
        200: -4.3,
        400: 7.6,
    }

    table747 = {
        0: 0,
        400: 1.5,
        800: 7.6,
    }

    table777 = {
        0: 0,
        300: 7.6,
    }

    table787 = {
        0: 0,
        9: 1.5,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            350 : (table350, 0),
            767 : (table767, 0),
            747 : (table747, 0),
            777 : (table777, 0),
            787 : (table787, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsB08(aircraftData):

    table = {
        0: 0,
        300: 7,
        310: 5.3,
        318: -1.7,
        319: -1.7,
        321: 3.5,
        757: 5.3,
        787: 11.9,

        
    }
    
    table737 = {
        0: 0,
        400: 3.5,
        500: -1.7,
        600: -1.7,
        800: 3.5,
        900: 3.5,
    }

    table767 = {
        0: 0,
        200: 7,
        300: 11.9,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
            767 : (table767, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC01to02(aircraftData):

    table = {
        0: 0,
        318: -2.1,
        319: -2.1,
        321: 1.5,
        717: 1.5,
        87: 1.5,
        80: 6.4,
        90: 6.4,
        700: 1.5,
        900: 1.5,
        146: -2.1
        
        }

    table737 = {
        0: 0,
        400: 1.5,
        500: -2.1,
        600: -2.1,
        800: 1.5,
        900: 1.5,
        }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC3(aircraftData):

    table = {
        0: 0,
        318: -1.5,
        319: -1.5,
        321: 1.5,
        717: 1.9,
        87: 1.9,

        80: 6.2,
        90: 6.2,

        300: 15.3,
        310: 15.3,

        350: 21.4,

        747: 25.7,
        777: 22.7,
    }
    
    table330 = {
        0: 0,
        200: 18.4,
        300: 21.4,
    }

    table340 = {
        0: 0,
        200: 18.4,
        300: 21.4,
    }

    table757 = {
        0: 0,
        200: 6.2,
        300: 15.3,
    }

    table767 = {
        0: 0,
        200: 18.4,
        300: 21.4,
        400: 22.7,
    }

    table787 = {
        0: 0,
        8: 21.4,
        9: 22.7,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            330 : (table330, 0),
            340 : (table340, 0),
            757 : (table757, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsCbig(aircraftData):

    table = {
        0: 0,
        318: -1.4,
        319: -1.4,
        145: -1.5,
        146: -1.4,
        700: -1.4,
        900: -1.4,
        1000: -1.4,

        310: 2.6,
        80: 2.6,
        90: 2.6,

        300: 5.8,
        }
    
    table757 = {
        0: 0,
        200: 2.6,
        300: 8.8,
    }

    table767 = {
        0: 0,
        200: 5.8,
        300: 8.8,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            757 : (table757, 0),
            767 : (table767, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC05to11(aircraftData):

    table = {
        0: 0,
        318: -2.2,
        319: -2.2,
        145: -2.2,
        146: -2.2,
        700: -2.2,
        900: -2.2,
        1000: -2.2,

        170: -0.7,
        175: -0.7,
        190: -0.7,
        195: -0.7,
        }
    
    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {

        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC14A(aircraftData):

    table = {
        0: 0,
        300: -6.2,
        310: -6.2,
        350: 3,
        747: 3,
        777: 1.2,
        }
    
    table340 = {
        0: 0,
        500: 5.4,
    }

    table757 = {
        0: 0,
        200: -6.2,
    }

    table767 = {
        0: 0,
        200: -6.2,
        300: 1.2,
        400: 3,
    }

    table787 = {
        0: 0,
        9: 1.2,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            340 : (table340, 0),
            757 : (table757, 0),
            767 : (table767, 0),
            787 : (table787, 0),
        },
        table) )

@AlternativeStopPositions
def MyCustomOffsetsC15(aircraftData):

    table = {
        0: 0,
        318: -1.4,
        319: -1.4,
        146: -1.4,

        310: 2.6,
        321: 2.6,
        717: 2.6,
        80: 2.6,
        90: 2.6,

        300: 5.7,
        }
    
    table737 = {
        0: 0,
        400: 2.6,
        800: 2.6,
        900: 2.6,
    }

    table757 = {
        0: 0,
        200: 5.7,
        300: 8.7,
    }

    table767 = {
        0: 0,
        200: 5.7,
        300: 8.7,
    }

    global HandleAircraftOffsets
    return Distance.fromMeters(HandleAircraftOffsets( aircraftData,
        {
            737 : (table737, 0),
            757 : (table757, 0),
            767 : (table767, 0),
        },
        table) )


ApronAnames = CustomizedName("Apron A [A01-A18] | A#", 1)
ApronBnames = CustomizedName("Apron B [B01-B16] | B#§", 2)
ApronCnames = CustomizedName("Apron C [C01-C15] | C#§", 3)
ApronDnames = CustomizedName("Apron D [D01-D22] | D#§", 4)
ApronEnames = CustomizedName("Apron E [E01-E35] | E#§", 5)
Apron2names = CustomizedName("Apron 2 [19-27] | #", 6)
Apron3Bnames = CustomizedName("Apron 3B [70-74] | #", 7)

ApronA01names = CustomizedName("Apron A [A01-A18] | A0#", 1)
ApronB01names = CustomizedName("Apron B [B01-B16] | B0#§", 2)
ApronC01names = CustomizedName("Apron C [C01-C15] | C0#§", 3)
ApronD01names = CustomizedName("Apron D [D01-D22] | D0#§", 4)
ApronE01names = CustomizedName("Apron E [E01-E35] | E0#§", 5)

parkings = {

    GATE : {
        None : ( ),

        21: (Apron2names, ),
        22: (Apron2names, ),
        24: (Apron2names, ),
        25: (Apron2names, ),
        27: (Apron2names, ),

        70: (Apron3Bnames, ),
        71: (Apron3Bnames, ),
        72: (Apron3Bnames, ),
        73: (Apron3Bnames, ),
        74: (Apron3Bnames, ),
    },

    GATE_A : {
        None : ( ),

        1 : (ApronA01names, MyCustomOffsetsA01to10, ),
        2 : (ApronA01names, MyCustomOffsetsA01to10, ),
        3 : (ApronA01names, MyCustomOffsetsA01to10, ),
        4 : (ApronA01names, MyCustomOffsetsA01to10, ),
        5 : (ApronA01names, MyCustomOffsetsA01to10, ),
        6 : (ApronA01names, MyCustomOffsetsA01to10, ),
        7 : (ApronA01names, MyCustomOffsetsA01to10, ),
        8 : (ApronA01names, MyCustomOffsetsA01to10, ),
        9 : (ApronA01names, MyCustomOffsetsA01to10, ),
        10 : (ApronAnames, MyCustomOffsetsA01to10, ),
        11 : (ApronAnames, MyCustomOffsetsA01to10,),
        12 : (ApronAnames, MyCustomOffsetsA01to10, ),
        13 : (ApronAnames, ),
        14 : (ApronAnames, ),
        15 : (ApronAnames, ),
        16 : (ApronAnames, ),
        17 : (ApronAnames, ),
        18 : (ApronAnames, ),
        19 : (ApronAnames, ),

    },

    GATE_B : {
        None : ( ),

        1 : (ApronB01names, MyCustomOffsetsB, ),
        2 : (ApronB01names, MyCustomOffsetsB, ),
        3 : (ApronB01names, MyCustomOffsetsB, ),
        4 : (ApronB01names, MyCustomOffsetsB, ),
        5 : (ApronB01names, MyCustomOffsetsB, ),
        6 : (ApronB01names, MyCustomOffsetsB, ),
        "7A" : (ApronB01names, MyCustomOffsetsBa, ),
        8 : (ApronB01names, MyCustomOffsetsB08, ),
        9 : (ApronB01names, MyCustomOffsetsB, ),
        10 : (ApronBnames, MyCustomOffsetsB, ),
        11 : (ApronBnames, MyCustomOffsetsB, ),
        12 : (ApronBnames, MyCustomOffsetsB, ),
        13 : (ApronBnames, MyCustomOffsetsB, ),
        14 : (ApronBnames, MyCustomOffsetsB, ),
        "15A" : (ApronBnames, MyCustomOffsetsBa, ),
        16 : (ApronBnames, MyCustomOffsetsC05to11, ),
    },

    GATE_C : {
        None : ( ),

        1 : (ApronC01names, MyCustomOffsetsC01to02, ),
        2 : (ApronC01names, MyCustomOffsetsC01to02, ),
        3 : (ApronC01names, MyCustomOffsetsC3, ),
        4 : (ApronC01names, MyCustomOffsetsCbig, ),
        5 : (ApronC01names, MyCustomOffsetsC05to11, ),
        6 : (ApronC01names, MyCustomOffsetsC05to11, ),
        7 : (ApronC01names, MyCustomOffsetsC05to11, ),
        8 : (ApronC01names, MyCustomOffsetsC05to11, ),
        9 : (ApronC01names, MyCustomOffsetsC05to11, ),
        10 : (ApronCnames, MyCustomOffsetsC05to11, ),
        11 : (ApronCnames, MyCustomOffsetsC05to11, ),
        12 : (ApronCnames, MyCustomOffsetsCbig, ),
        13 : (ApronCnames, MyCustomOffsetsCbig, ),
        14 : (ApronCnames, MyCustomOffsetsC05to11, ),
        "14A" : (ApronCnames, MyCustomOffsetsC14A, ),
        15 : (ApronCnames, MyCustomOffsetsC15, ),
    },

    GATE_D : {
        None : ( ),

        1 : (ApronD01names, MyCustomOffsetsBa, ),
        2 : (ApronD01names, MyCustomOffsetsB, ),
        "3A" : (ApronD01names, MyCustomOffsetsBa, ),
        3 : (ApronD01names, MyCustomOffsetsB, ),
        4 : (ApronD01names, MyCustomOffsetsB, ),
        "5A" : (ApronD01names, MyCustomOffsetsBa, ),
        5 : (ApronD01names, MyCustomOffsetsB, ),
        "5B" : (ApronD01names, ),
        6 : (ApronD01names, MyCustomOffsetsB, ),
        "7A" : (ApronD01names, MyCustomOffsetsBa, ),
        7 : (ApronD01names, MyCustomOffsetsB, ),
        8 : (ApronD01names, MyCustomOffsetsB, ),
        "9A" : (ApronD01names, MyCustomOffsetsBa, ),
        9 : (ApronD01names, MyCustomOffsetsB, ),
        10 : (ApronDnames, MyCustomOffsetsB, ),
        "11A" : (ApronDnames, MyCustomOffsetsBa, ),
        11 : (ApronDnames, MyCustomOffsetsB, ),
        12 : (ApronDnames, MyCustomOffsetsB08, ),
        "13A" : (ApronDnames, MyCustomOffsetsBa, ),
        "13B" : (ApronDnames, ),
        13 : (ApronDnames, MyCustomOffsetsB, ),
        14 : (ApronDnames, MyCustomOffsetsB, ),
        "15A" : (ApronDnames, MyCustomOffsetsBa, ),
        15 : (ApronDnames, MyCustomOffsetsB, ),
        16 : (ApronDnames, MyCustomOffsetsB, ),
        "17A" : (ApronDnames, MyCustomOffsetsBa, ),
        17 : (ApronDnames, MyCustomOffsetsB, ),
        18 : (ApronDnames, MyCustomOffsetsB, ),
        "19A" : (ApronDnames, MyCustomOffsetsBa, ),
        19 : (ApronDnames, MyCustomOffsetsB, ),
        20 : (ApronDnames, MyCustomOffsetsB, ),
        "21A" : (ApronDnames, MyCustomOffsetsBa, ),
        21 : (ApronDnames, MyCustomOffsetsB, ),
        22 : (ApronDnames, MyCustomOffsetsBa, ),
    },

    GATE_E : {
        None : ( ),

        1 : (ApronE01names, ),
        2 : (ApronE01names, ),
        3 : (ApronE01names, ),
        4 : (ApronE01names, ),
        5 : (ApronE01names, ),
        6 : (ApronE01names, ),
        7 : (ApronE01names, ),
        8 : (ApronE01names, ),
        9 : (ApronE01names, ),
        10 : (ApronEnames, ),
        11 : (ApronEnames, ),
        12 : (ApronEnames, ),
        13 : (ApronEnames, ),
        14 : (ApronEnames, ),
        15 : (ApronEnames, ),
        16 : (ApronEnames, ),
        17 : (ApronEnames, ),
        18 : (ApronEnames, ),
        19 : (ApronEnames, ),
        21 : (ApronEnames, ),
        22 : (ApronEnames, ),
        23 : (ApronEnames, ),
        24 : (ApronEnames, ),
        25 : (ApronEnames, ),
        26 : (ApronEnames, ),
        27 : (ApronEnames, ),
        28 : (ApronEnames, ),
        29 : (ApronEnames, ),
        30 : (ApronEnames, ),
        31 : (ApronEnames, ),
        32 : (ApronEnames, ),
        33 : (ApronEnames, ),
        34 : (ApronEnames, ),
        35 : (ApronEnames, ),
    }

    }