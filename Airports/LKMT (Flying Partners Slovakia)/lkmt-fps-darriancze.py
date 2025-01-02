# -- coding: utf-8 --
msfs_mode = 1
icao = "lkmt"
version = 1.0

ApronCentral = CustomizedName("Apron Central (Airliners) | Stand #§",1)
ApronS = CustomizedName("Apron South (Cargo) | Stand #§",2)
ApronMaint = CustomizedName("Apron North (Aircraft Maintenance) | Stand #§",3)
ApronGA = CustomizedName("Apron Let's Fly & Apron Elmontex (General Aviation) | Stand #§",4)

parkings = {
GATE : {
        None : ( ),
        1 : (ApronCentral, ),
        2 : (ApronCentral, ),
        3 : (ApronCentral, ),
        4 : (ApronCentral, ),
        5 : (ApronCentral, ),
        6 : (ApronCentral, ),
        7 : (ApronCentral, )
},
N_PARKING : {
        None : ( ),
        17 : (ApronMaint, )
},
S_PARKING : {
        None : ( ),
        1 : (ApronS, ),
        3 : (ApronS, )
},
E_PARKING : {
        None : ( ),
        33 : (ApronGA, )
},
DOCK : {
        None : ( ),
        30 : (ApronGA, ),
        31 : (ApronGA, ),
        32 : (ApronGA, )
}
}
