# -- coding: utf-8 --

msfs_mode = 1
icao = "eglc"
version = 1.0

APRONMAIN=CustomizedName('Main Apron (03-14) | Stand #§', 1)
APRONEAST=CustomizedName('East Apron (21-28) | Stand #§', 2)
APRONWEST=CustomizedName('West Apron (Jet Centre) | Stand #§', 3)

parkings = {
    GATE : {
        3 : (APRONMAIN, ),
        4 : (APRONMAIN, ),
        5 : (APRONMAIN, ),
        6 : (APRONMAIN, ),
        7 : (APRONMAIN, ),
        8 : (APRONMAIN, ),
        9 : (APRONMAIN, ),
        10 : (APRONMAIN, ),
        12 : (APRONMAIN, ),
        13 : (APRONMAIN, ),
        21 : (APRONEAST, ),
        22 : (APRONEAST, ),
        23 : (APRONEAST, ),
        24 : (APRONEAST, ),
        25 : (APRONEAST, ),
        27 : (APRONEAST, ),
        28 : (APRONEAST, ),
    },
    PARKING : {
        29 : (APRONEAST, )
    },
    DOCK : {
        26 : (APRONEAST, )
    },
    W_PARKING : {
        1 : (APRONWEST, ),
        2 : (APRONWEST, ),
        3 : (APRONWEST, ),
        4 : (APRONWEST, )
    },
}
