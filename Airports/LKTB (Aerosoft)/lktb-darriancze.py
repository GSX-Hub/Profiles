# -- coding: utf-8 --
msfs_mode = 1
icao = "lktb"
version = 4.0

ApronM = CustomizedName("Apron Middle (Airliners) | Stand #§",1)
ApronW = CustomizedName("Apron West (Cargo and Heavy) | Stand #§",2)
ApronGA = CustomizedName("General Aviation | Stand #§",3)
Herbst = CustomizedName("Herbst Aero (General Aviation) | Stand #§",4)
ParkingN = CustomizedName("Parking Area North (Aircraft Shelters) | Stand #§",5)
SheltersA = CustomizedName("Aircraft Shelters at Taxiway A | Stand #§",6)

parkings = {
    PARKING : {
        None : ( ),
        1 : (ApronM, ),
        2 : (ApronM, ),
        3 : (ApronM, ),
        4 : (ApronM, ),
        5 : (ApronM, ), 
        6 : (ApronW, ),
        7 : (ApronW, ),
        8 : (ApronW, ),
        9 : (ApronGA, ),
        10 : (ApronGA, ),
        11 : (ApronGA, )  
    },
    0 : {
        None : ( ),
        12 : (ApronGA, ),
        13 : (ApronGA, ),
        14 : (SheltersA, ),
        15 : (SheltersA, ),
        16 : (SheltersA, ),
        17 : (SheltersA, ),
        18 : (SheltersA, ),
        19 : (ParkingN, ),
        20 : (ParkingN, ),
        21 : (ParkingN, ),
        22 : (ParkingN, ),
        23 : (ParkingN, ),
        24 : (ParkingN, ),
        25 : (SheltersA, ),
        26 : (Herbst, ),
        27 : (Herbst, ),
        28 : (Herbst, ),
        29 : (Herbst, ),
        30 : (Herbst, ),
        31 : (Herbst, )
    }
}