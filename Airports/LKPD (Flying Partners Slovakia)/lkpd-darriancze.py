# -- coding: utf-8 --
msfs_mode = 1
icao = "lkpd"
version = 1.2

ApronW = CustomizedName("Apron West (Airliners) | Stand #§",1)
ApronWGA = CustomizedName("Apron West (GA & Bizjets) | Stand #§",2)
Shelters = CustomizedName("Aircraft Shelters (Military) | Stand #§",3)
ApronE = CustomizedName("Apron East (Military) | Stand #§",4)

parkings = {
    E_PARKING : {
        None : ( ),
        11 : (ApronE, ) 
    },
    GATE : {
        None : ( ),
        4 : (ApronW, ),
        5 : (ApronW, ),
        6 : (ApronW, ),
    },
    NE_PARKING : {
        None : ( ),
        10 : (Shelters, )
    },
    PARKING : {
        None : ( ),
        1 : (ApronWGA, ),
        2 : (ApronWGA, ),
        3 : (ApronWGA, ),
    }
}