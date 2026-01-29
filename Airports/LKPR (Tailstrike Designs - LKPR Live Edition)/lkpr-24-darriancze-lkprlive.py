# -- coding: utf-8 --
msfs_mode = 1
icao = "lkpr"
version = 1.2

Terminal1 = CustomizedName("Terminal 1 (1 - 16) (Non-Schengen) | Gate #§",1)
Terminal1JetwayINOP = CustomizedName("Terminal 1 (1 - 16) (Non-Schengen) | Gate #§ (Jetway INOP)",1)
Terminal2 = CustomizedName("Terminal 2 (17 - 31) (Schengen) | Gate #§",2)
Terminal2JetwayINOP = CustomizedName("Terminal 2 (17 - 31) (Schengen) | Gate #§ (Jetway INOP)",2)
RemoteStands = CustomizedName("Remote Stands (50 - 75) | Stand #§",3)
RemoteStandsTaxiOut = CustomizedName("Remote Stands (50 - 75) | Stand #§ (Taxi Out Stand)",3)
ApronEast = CustomizedName("Apron East (Cargo) (E3 - E7) | Stand E#§",4)
ApronSouth = CustomizedName("Apron South (General Aviation) (S1 - S30) | Stand S#§",5)
ApronSouthTaxiOut = CustomizedName("Apron South (General Aviation) (S1 - S30) | Stand S#§ (Taxi Out Stand)",5)
ApronBell = CustomizedName("Apron Bell (General Aviation) (M1A - M1B) | Stand M#§",6)
HangarF = CustomizedName("Hangar F | Stand In The Hangar",7)

@AlternativeStopPositions
def Gate1_Offset(aircraftData):
    TableIcao = {
        "B763": 0,
        "A332": 3.6,
        "B772": 3.6,
        "A306": 3.6,
        "A310": 3.6,
        "B752": 3.6,
        "B753": 3.6,
        "B762": 3.6,
        "B764": 3.6,
        "B77L": 3.6,
        "B788": 3.6,
        "B789": 3.6,
        "B78X": 3.6,
        "A333": 7.3,
        "A359": 7.3,
        "B773": 7.3,
        "A35K": 7.3,
        "B77W": 7.3,
    }

    TableGroup = {
        "ARC-D" : 3.6,
        "ARC-E" : 7.3,
        "ARC-F" : 7.3,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate3_Offset(aircraftData):
    TableIcao = {
        "A310": 0,
        "B752": 0,
        "B753": 0,
        "B762": 0,
        "DC10": 0,
        "A333": 3.6,
        "A332": 3.6,
        "B772": 3.6,
        "A306": 3.6,
        "A342": 3.6,
        "A343": 3.6,
        "B763": 3.6,
        "B764": 3.6,
        "B77L": 3.6,
        "B788": 3.6,
        "B789": 3.6,
        "B78X": 3.6,
        "MD11": 3.6,
        "A345": 7.2,
        "A359": 7.2,
        "B741": 8.7,
        "B742": 8.7,
        "B743": 8.7,
        "B744": 8.7,
        "B748": 8.7,
        "B773": 8.7,
        "A346": 8.7,
        "A35K": 8.7,
        "B77W": 8.7,
    }

    TableGroup = {
        "ARC-D" : 3.6,
        "ARC-E" : 7.2,
        "ARC-F" : 8.7,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate3A_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "A20N": 0,
        "B734": 0,
        "A318": 0,
        "A319": 0,
        "A19N": 0,
        "B733": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "E190": 0,
        "E290": 0,
        "A321": 3.7,
        "A21N": 3.7,
        "B738": 3.7,
        "B739": 3.7,
        "B38M": 3.7,
        "B39M": 3.7,
        "E195": 3.7,
        "E295": 3.7,
        "BCS1": 3.7,
        "BCS3": 3.7,
        "CRJX": 3.7,
    }

    TableGroup = {
        "ARC-E" : 3.6,
        "ARC-F" : 3.6,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate3B_Offset(aircraftData):
    TableIcao = {
        "A20N": 0,
        "B737": 0,
        "A318": 0,
        "A319": 0,
        "A19N": 0,
        "A320": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "A21N": 2.75,
        "B738": 2.75,
        "B739": 2.75,
        "B38M": 2.75,
        "B39M": 2.75,
        "BCS1": 2.75,
        "BCS3": 2.75,
        "E170": 2.75,
        "E175": 2.75,
        "E190": 2.75,
        "E195": 2.75,
        "E290": 2.75,
        "E295": 2.75,
    }

    TableGroup = {
        "ARC-E" : 2.75,
        "ARC-F" : 2.75,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate4_Offset(aircraftData):
    TableIcao = {
        "A319": 0,
        "A19N": 0,
        "A318": 0,
        "A320": 1.2,
        "A20N": 1.2,
        "B734": 1.2,
        "B733": 1.2,
        "B735": 1.2,
        "B736": 1.2,
        "E170": 1.2,
        "E175": 1.2,
        "E190": 1.2,
        "E290": 1.2,
        "SU95": 1.2,
        "A321": 5.75,
        "A21N": 5.75,
        "B738": 5.75,
        "B739": 5.75,
    }

    TableGroup = {
        "ARC-D" : 1.2,
        "ARC-E" : 5.75,
        "ARC-F" : 5.75,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate5_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "A20N": 0,
        "E195": 0,
        "A318": 0,
        "A319": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E290": 0,
        "E295": 0,
        "SU95": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "A321": 3.75,
        "B739": 3.75,
    }

    TableGroup = {
        "ARC-F" : 3.75,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate7_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "A318": 0,
        "A319": 0,
        "A20N": 0,
        "A19N": 0,
        "E170": 0,
        "E175": 0,
        "B733": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "BCS1": 0,
        "SU95": 0,
        "B736": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "B738": 5.8,
        "E195": 5.8,
        "E295": 5.8,
        "B734": 5.8,
        "B38M": 5.8,
        "E190": 5.8,
        "E290": 5.8,
        "BCS3": 5.8,
        "A321": 8.4,
        "B739": 8.4,
        "A21N": 8.4,
        "B39M": 8.4,
    }

    TableGroup = {
        "ARC-E" : 5.8,
        "ARC-F" : 8.4,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate9_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "B734": 0,
        "A318": 0,
        "A319": 0,
        "A20N": 0,
        "A19N": 0,
        "B733": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "E170": 0,
        "E175": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "E190": 2.7,
        "E290": 2.7,
        "E170": 2.7,
        "E175": 2.7,
        "A321": 5.25,
        "B738": 5.25,
        "A21N": 5.25,
        "B38M": 5.25,
        "B39M": 5.25,
        "B739": 5.25,
        "E195": 5.25,
        "E295": 5.25,
        "BCS1": 5.25,
        "BCS3": 5.25,
    }

    TableGroup = {
        "ARC-D" : 2.7,
        "ARC-E" : 2.7,
        "ARC-F" : 5.25,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate10_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "B738": 0,
        "A318": 0,
        "A319": 0,
        "A20N": 0,
        "A19N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B38M": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E290": 0,
        "BCS1": 0,
        "BCS3": 0,
        "SU95": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "A321": 2.6,
        "A21N": 2.6,
        "B739": 2.6,
        "B39M": 2.6,
        "E195": 2.6,
        "E295": 2.6,
    }

    TableGroup = {
        "ARC-F" : 2.6,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate11_Offset(aircraftData):
    TableIcao = {
        "A320": 0,
        "B738": 0,
        "A318": 0,
        "A319": 0,
        "A20N": 0,
        "A19N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B38M": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "BCS1": 0,
        "BCS3": 0,
        "SU95": 0,
        "E190": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "E190": 0,
        "E290": 0,
        "A321": 2.75,
        "A21N": 2.75,
        "B739": 2.75,
        "B39M": 2.75,
        "E195": 2.75,
        "E295": 2.75,
    }

    TableGroup = {
        "ARC-F" : 2.75,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate12_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "B762": 0,
        "A306": 0,
        "A310": 0,
        "B752": 0,
        "B753": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "E290": 0,
        "E295": 0,
        "BCS1": 0,
        "BCS3": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "A332": 7.65,
        "A333": 7.65,
        "A333": 7.65,
        "A338": 7.65,
        "A339": 7.65,
        "B764": 7.65,
        "B788": 7.65,
        "B789": 7.65,
        "B78X": 7.65,
        "A342": 7.65,
        "A343": 7.65,
        "A345": 7.65,
        "A346": 7.65,
        "A359": 7.65,
        "A35K": 7.65,
        "B741": 7.65,
        "B742": 7.65,
        "B743": 7.65,
        "B744": 7.65,
        "B748": 7.65,
        "B763": 7.65,
        "B772": 7.65,
        "B773": 7.65,
        "B77L": 7.65,
        "B77W": 7.65,
    }

    TableGroup = {
        "ARC-F" : 7.65,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate14_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B763": 3.75,
        "B733": 3.75,
        "B734": 3.75,
        "B735": 3.75,
        "B736": 3.75,
        "B737": 3.75,
        "B738": 3.75,
        "B739": 3.75,
        "B38M": 3.75,
        "B39M": 3.75,
        "E170": 3.75,
        "E175": 3.75,
        "E190": 3.75,
        "E195": 3.75,
        "E290": 3.75,
        "E295": 3.75,
        "A310": 3.75,
        "B712": 3.75,
        "B762": 3.75,
        "BCS1": 3.75,
        "BCS3": 3.75,
        "MD81": 3.75,
        "MD82": 3.75,
        "MD83": 3.75,
        "MD87": 3.75,
        "MD88": 3.75,
        "MD90": 3.75,
        "DC95": 3.75,
        "B752": 7.25,
        "B753": 7.25,
        "A306": 7.25,
        "B772": 11.8,
        "A332": 11.8,
        "A333": 11.8,
        "A338": 11.8,
        "A339": 11.8,
        "A342": 11.8,
        "A343": 11.8,
        "B764": 11.8,
        "B77L": 11.8,
        "B788": 11.8,
        "B77W": 14.5,
        "B773": 14.5,
        "B741": 14.5,
        "B742": 14.5,
        "B743": 14.5,
        "B744": 14.5,
        "B748": 14.5,
        "B789": 14.5,
        "B78X": 14.5,
        "A359": 14.5,
        "A388": 17.5,
    }

    TableGroup = {
        "ARC-C" : 3.75,
        "ARC-D" : 7.25,
        "ARC-E" : 14.5,
        "ARC-F" : 14.5,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate14A_Offset(aircraftData):
    TableIcao = {
        "A388": 0,
        "B748": 0,
        "A345": 0,
        "A346": 1.2,
        "B773": 1.2,
        "A35K": 1.2,
        "B77W": 1.2,
    }

    TableGroup = {
        "ARC-A" : 1.2,
        "ARC-B" : 1.2,
        "ARC-C" : 1.2,
        "ARC-D" : 1.2,
        "ARC-E" : 1.2,
        "ARC-F" : 1.2,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate16_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "B733": 1.7,
        "B734": 1.7,
        "B735": 1.7,
        "B736": 1.7,
        "B737": 1.7,
        "B738": 1.7,
        "B739": 1.7,
        "B38M": 1.7,
        "B39M": 1.7,
        "A310": 1.7,
        "E170": 1.7,
        "E175": 1.7,
        "E190": 1.7,
        "E195": 1.7,
        "E290": 1.7,
        "E295": 1.7,
        "A332": 8.2,
        "A333": 8.2,
        "A338": 8.2,
        "A339": 8.2,
        "B772": 8.2,
        "A306": 8.2,
        "A342": 8.2,
        "A343": 8.2,
        "A359": 8.2,
        "B752": 8.2,
        "B753": 8.2,
        "B762": 8.2,
        "B763": 8.2,
        "B764": 8.2,
        "B77L": 8.2,
        "B788": 8.2,
        "B789": 8.2,
        "B78X": 8.2,
        "BCS1": 8.2,
        "BCS3": 8.2,
        "B77W": 12,
    }

    TableGroup = {
        "ARC-E" : 12,
        "ARC-F" : 12,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate17_18_Offset(aircraftData):
    TableIcao = {
        "MD81": 0,
        "MD82": 0,
        "MD83": 0,
        "MD87": 0,
        "MD88": 0,
        "MD90": 0,
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "E290": 0,
        "E295": 0,
        "BCS1": 0,
        "BCS3": 0,
        "AT43": 0,
        "AT45": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "E135": 0,
        "E145": 0,
        "MD81": 2.8,
        "MD82": 2.8,
        "MD83": 2.8,
        "MD87": 2.8,
        "MD88": 2.8,
        "MD90": 2.8,
        "DC95": 2.8,
    }

    TableGroup = {
        "ARC-F" : 2.8,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate19A_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "E290": 0,
        "E295": 0,
        "BCS1": 0,
        "BCS3": 0,
        "B752": 1.6,
        "B753": 1.6,
    }

    TableGroup = {
        "ARC-D" : 1.6,
        "ARC-E" : 1.6,
        "ARC-F" : 1.6,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate21A_Offset(aircraftData):
    TableIcao = {
        "A310": 0,
        "A318": 2.7,
        "A319": 2.7,
        "A320": 2.7,
        "A321": 2.7,
        "A19N": 2.7,
        "A20N": 2.7,
        "A21N": 2.7,
        "B733": 2.7,
        "B734": 2.7,
        "B735": 2.7,
        "B736": 2.7,
        "B737": 2.7,
        "B738": 2.7,
        "B739": 2.7,
        "B38M": 2.7,
        "B39M": 2.7,
        "E170": 2.7,
        "E175": 2.7,
        "E190": 2.7,
        "E195": 2.7,
        "E290": 2.7,
        "E295": 2.7,
        "BCS1": 2.7,
        "BCS3": 2.7,
        "B752": 5.3,
        "B753": 5.3,
    }

    TableGroup = {
        "ARC-F" : 5.3,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate22_Offset(aircraftData):
    TableIcao = {
        "A310": 0,
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "A342": 0,
        "BCS1": 0,
        "BCS3": 0,
        "A332": 2.8,
        "A333": 2.8,
        "A333": 2.8,
        "A338": 2.8,
        "A339": 2.8,
        "B741": 2.8,
        "B742": 2.8,
        "B743": 2.8,
        "B744": 2.8,
        "B748": 2.8,
        "B752": 2.8,
        "B753": 2.8,
        "A306": 2.8,
        "A343": 2.8,
        "A345": 2.8,
        "A359": 2.8,
        "B762": 2.8,
        "B763": 2.8,
        "B764": 2.8,
        "B788": 2.8,
        "B789": 2.8,
        "B78X": 2.8,
        "MD11": 2.8,
        "DC10": 2.8,
        "A346": 7.4,
        "B772": 7.4,
        "B773": 7.4,
        "B77L": 7.4,
        "B77W": 7.4,
        "A388": 7.4,
        "A35K": 7.4,
    }

    TableGroup = {
        "ARC-D" : 2.8,
        "ARC-E" : 2.8,
        "ARC-F" : 7.4,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate22B_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "E275": 0,
        "E290": 0,
        "E295": 0,
        "E195": 1.6,
        "MD81": 1.6,
        "MD82": 1.6,
        "MD83": 1.6,
        "MD87": 1.6,
        "MD88": 1.6,
        "MD90": 1.6,
        "DC95": 1.6,
        "E170": 1.6,
        "E175": 1.6,
        "E190": 1.6,
        "BCS1": 1.6,
        "BCS3": 1.6,
    }

    TableGroup = {
        "ARC-E" : 1.6,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate26_27_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A19N": 0,
        "B733": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "E275": 0,
        "BCS1": 0,
        "A320": 2.7,
        "B734": 2.7,
        "A20N": 2.7,
        "E170": 2.7,
        "E175": 2.7,
        "E290": 2.7,
        "B738": 6.3,
        "B38M": 6.3,
        "E190": 6.3,
        "E195": 6.3,
        "BCS3": 6.3,
    }

    TableGroup = {
        "ARC-C" : 2.7,
        "ARC-D" : 2.7,
        "ARC-E" : 6.3,
        "ARC-F" : 6.3,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate28__31_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "E290": 0,
        "E295": 0,
        "BCS1": 0,
        "BCS3": 0,
        "MD81": 4.7,
        "MD82": 4.7,
        "MD83": 4.7,
        "MD87": 4.7,
        "MD88": 4.7,
        "MD90": 4.7,
        "DC95": 4.7,
    }

    TableGroup = {
        "ARC-E" : 4.7,
        "ARC-F" : 4.7,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
        
@AlternativeStopPositions
def Gate50_57_Offset(aircraftData):
    TableIcao = {
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "B461": 0,
        "B462": 0,
        "B463": 0,
        "RJ1H": 0,
        "RJ70": 0,
        "RJ85": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "E290": 0,
        "E295": 0,
        "E120": 0,
        "E135": 0,
        "E145": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "F28": 0,
        "F50": 0,
        "F70": 0,
        "F100": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "YK40": 0,
        "SB20": 0,
        "B712": 0,
        "DC95": 0,
        "T134": 0,
        "SF34": 0,
        "BCS1": 0,
        "BCS3": 0,
        "SU95": 0,
        "MD81": 2.7,
        "MD82": 2.7,
        "MD83": 2.7,
        "MD87": 2.7,
        "MD88": 2.7,
        "MD90": 2.7,
        "DC95": 2.7,
    }

    TableGroup = {
        "ARC-A" : 0,
        "ARC-B" : 0,
        "ARC-C" : 2.7,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
        
@AlternativeStopPositions
def Gate50A_Offset(aircraftData):
    TableIcao = {
        "A310": 0,
        "C130": 0,
        "B752": 0,
        "B703": 0,
        "T204": 0,
        "T154": 0,
        "L101": 0,
        "B753": 6.2,
        "B763": 6.2,
        "B762": 6.2,
        "IL62": 6.2,
    }

    TableGroup = {
        "ARC-C" : 0,
        "ARC-D" : 0,
        "ARC-E" : 0,
        "ARC-F" : 6.2,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate60_Offset(aircraftData):
    TableIcao = {
        "A319": 0,
        "A320": 0,
        "A318": 0,
        "A19N": 0,
        "A20N": 0,
        "B733": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "A321": 5.7,
        "B739": 5.7,
        "A21N": 5.7,
        "B738": 5.7,
        "B38M": 5.7,
        "B39M": 5.7,
        "MD87": 5.7,
        "E275": 5.7,
        "E290": 5.7,
        "E295": 5.7,
        "BCS1": 5.7,
        "BCS3": 5.7,
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "B734": 0,
        "E195": 0,
        "F28": 0,
        "F50": 0,
        "F100": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "B461": 0,
        "B462": 0,
        "B463": 0,
        "RJ1H": 0,
        "RJ70": 0,
        "RJ85": 0,
        "YK40": 0,
        "SF34": 0,
        "SB20": 0,
        "RJ85": 0,
        "RJ85": 0,
        "RJ85": 0,
        "RJ85": 0,
        "RJ85": 0,
        "E120": 0,
        "E135": 0,
        "E145": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "B712": 0,
        "B722": 0,
        "DC95": 0,
        "T134": 0,
        "MD81": 0,
        "MD82": 0,
        "MD83": 0,
        "MD87": 0,
        "MD88": 0,
        "AN26": 0,
        "SU95": 0,
    }

    TableGroup = {
        "ARC-C" : 0,
        "ARC-D" : 5.7,
        "ARC-E" : 0,
        "ARC-F" : 0,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate70_71_Offset(aircraftData):
    TableIcao = {
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "CRJ2": 0,
        "DH8A": 0,
        "DH8C": 0,
        "B461": 0,
        "B462": 0,
        "B463": 0,
        "RJ1H": 0,
        "RJ70": 0,
        "RJ85": 0,
        "F28": 0,
        "F50": 0,
        "F70": 0,
        "YK40": 0,
        "SF34": 0,
        "SB20": 0,
        "E120": 0,
        "E135": 0,
        "E145": 0,
        "F100": 5.3,
        "CRJ7": 5.3,
        "CRJ9": 5.3,
        "DH8D": 5.3,
        "T134": 5.3,
    }

    TableGroup = {
        "ARC-C" : 0,
        "ARC-D" : 5.3,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def Gate72_74_Offset(aircraftData):
    TableIcao = {
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "A318": 0,
        "B461": 0,
        "DH8A": 0,
        "DH8C": 0,
        "F28": 0,
        "F50": 0,
        "YK40": 0,
        "SF34": 0,
        "A320": 4,
        "B734": 4,
        "A319": 4,
        "A19N": 4,
        "A20N": 4,
        "B733": 4,
        "B735": 4,
        "B736": 4,
        "B737": 4,
        "F70": 4,
        "F100": 4,
        "E120": 4,
        "E135": 4,
        "E145": 4,
        "E170": 4,
        "E175": 4,
        "E190": 4,
        "E275": 4,
        "E290": 4,
        "B462": 4,
        "B463": 4,
        "SB20": 4,
        "CRJ2": 4,
        "CRJ7": 4,
        "DH8D": 4,
        "BCS1": 4,
        "SU95": 4,
        "B738": 7.1,
        "B38M": 7.1,
    }

    TableGroup = {
        "ARC-C" : 4,
        "ARC-D" : 7.1,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
@AlternativeStopPositions
def Gate75_Offset(aircraftData):
    TableIcao = {
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "A318": 0,
        "B461": 0,
        "DH8A": 0,
        "DH8C": 0,
        "F28": 0,
        "F50": 0,
        "YK40": 0,
        "SF34": 0,
        "A320": 4.3,
        "B734": 4.3,
        "A319": 4.3,
        "A19N": 4.3,
        "A20N": 4.3,
        "B733": 4.3,
        "B735": 4.3,
        "B736": 4.3,
        "B737": 4.3,
        "F70": 4.3,
        "F100": 4.3,
        "E120": 4.3,
        "E135": 4.3,
        "E145": 4.3,
        "E170": 4.3,
        "E175": 4.3,
        "E190": 4.3,
        "E275": 4.3,
        "E290": 4.3,
        "B462": 4.3,
        "B463": 4.3,
        "SB20": 4.3,
        "CRJ2": 4.3,
        "CRJ7": 4.3,
        "DH8D": 4.3,
        "BCS1": 4.3,
        "SU95": 4.3,
        "B738": 6.7,
        "B38M": 6.7,
    }
    TableGroup = {
        "ARC-C" : 4.3,
        "ARC-D" : 6.7,
    }
    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
        
@AlternativeStopPositions
def StandE3_Offset(aircraftData):
    TableIcao = {
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A321": 0,
        "A19N": 0,
        "A20N": 0,
        "A21N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B739": 0,
        "B38M": 0,
        "B39M": 0,
        "SF34": 0,
        "CRJ2": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "B461": 0,
        "B462": 0,
        "B463": 0,
        "RJ1H": 0,
        "RJ70": 0,
        "RJ85": 0,
        "F27": 0,
        "F28": 0,
        "F50": 0,
        "F70": 0,
        "F100": 0,
        "YK40": 0,
        "SB20": 0,
        "SU95": 0,
        "E120": 0,
        "E135": 0,
        "E145": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "T134": 0,
        "BCS1": 0,
        "BCS3": 0,
        "B712": 0,
        "DC95": 0,
        "B752": 2.7,
        "B762": 2.7,
        "A310": 2.7,
        "B703": 2.7,
        "B721": 2.7,
        "B722": 2.7,
        "B37M": 2.7,
        "T204": 2.7,
        "T154": 2.7,
        "L101": 2.7,
        "MD81": 2.7,
        "MD82": 2.7,
        "MD83": 2.7,
        "MD87": 2.7,
        "MD88": 2.7,
        "MD90": 2.7,
        "A306": 5.4,
        "A30B": 5.4,
        "B753": 5.4,
        "A30B": 5.4,
        "IL62": 5.4,
        "B763": 7.5,
    }

    TableGroup = {
        "ARC-D" : 5.4,
        "ARC-E" : 7.5,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
        
@AlternativeStopPositions
def StandE4_Offset(aircraftData):
    TableIcao = {
        "AT43": 0,
        "AT45": 0,
        "AT46": 0,
        "AT72": 0,
        "AT73": 0,
        "AT75": 0,
        "AT76": 0,
        "A318": 0,
        "A319": 0,
        "A320": 0,
        "A19N": 0,
        "A20N": 0,
        "B733": 0,
        "B734": 0,
        "B735": 0,
        "B736": 0,
        "B737": 0,
        "B738": 0,
        "B38M": 0,
        "CRJ7": 0,
        "CRJ9": 0,
        "CRJX": 0,
        "DH8A": 0,
        "DH8B": 0,
        "DH8C": 0,
        "DH8D": 0,
        "B461": 0,
        "B462": 0,
        "B463": 0,
        "RJ1H": 0,
        "RJ70": 0,
        "RJ85": 0,
        "F27": 0,
        "F28": 0,
        "F50": 0,
        "F70": 0,
        "F100": 0,
        "YK40": 0,
        "SB20": 0,
        "SU95": 0,
        "E120": 0,
        "E135": 0,
        "E145": 0,
        "E170": 0,
        "E175": 0,
        "E190": 0,
        "E195": 0,
        "T134": 0,
        "BCS1": 0,
        "BCS3": 0,
        "SF34": 0,
        "A321": 4.2,
        "A21N": 4.2,
        "B739": 4.2,
        "B39M": 4.2,
        "B712": 4.2,
        "MD87": 4.2,
        "DC95": 4.2,
        }

    TableGroup = {
        "ARC-D" : 4.2,
        "ARC-E" : 4.2,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

@AlternativeStopPositions
def StandE5A_Offset(aircraftData):
    TableIcao = {
        "A333": 0,
        "A339": 0,
        "MD11": 0,
        "DC10": 0,
        "L101": 0,
        "A306": 0,
        "A30B": 0,
        "A310": 0,
        "A333": 0,
        "C17": 0,
        "B752": 0,
        "B703": 0,
        "IL86": 0,
        "IL96": 0,
        "A124": 0,
        "B762": 11.3,
        "B763": 11.3,
        "B741": 11.3,
        "B742": 11.3,
        "B743": 11.3,
        "B744": 11.3,
        "B753": 11.3,
        "B788": 11.3,
        "A332": 11.3,
        "A338": 11.3,
        "A342": 11.3,
        "A343": 11.3,
        "A345": 11.3,
        "A359": 11.3,
        "IL62": 11.3,
        "B748": 4.4,
        "B772": 4.4,
        "B773": 4.4,
        "B77L": 4.4,
        "B77W": 4.4,
        "B764": 4.4,
        "B789": 4.4,
        "B78X": 4.4,
        "A388": 7.2,
        "A35K": 7.2,
        "A346": 7.2,
        }

    TableGroup = {
        "ARC-D" : 11.3,
        "ARC-E" : 4.4,
        "ARC-F" : 7.2,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()
        
@AlternativeStopPositions
def StandE7_Offset(aircraftData):
    TableIcao = {
        "A310": 0,
        "C130": 0,
        "C17": 0,
        "IL76": 0,
        "IL96": 0,
        "A124": 0,
        "AN12": 0,
        "B741": 11.3,
        "B742": 11.3,
        "B743": 11.3,
        "B744": 11.3,
        "A332": 11.3,
        "A333": 11.3,
        "A338": 11.3,
        "A339": 11.3,
        "B703": 11.3,
        "B748": 11.3,
        "B752": 11.3,
        "B753": 11.3,
        "B762": 11.3,
        "B763": 11.3,
        "B764": 11.3,
        "B77L": 11.3,
        "B772": 11.3,
        "B788": 11.3,
        "B789": 11.3,
        "A342": 11.3,
        "A343": 11.3,
        "A345": 11.3,
        "A359": 11.3,
        "A306": 11.3,
        "A30B": 11.3,
        "L101": 11.3,
        "DC10": 11.3,
        "IL86": 11.3,
        "IL62": 11.3,
        "MD11": 11.3,
        "A346": 19.5,
        "B77W": 20.5,
        "B773": 20.5,
        "B78X": 20.5,
        "A35K": 20.5,
        }

    TableGroup = {
        "ARC-E" : 11.3,
        "ARC-F" : 20.5,
    }

    try:
        return Distance.fromMeters(TableIcao.get(aircraftData.icaoTypeDesignator,TableGroup.get(aircraftData.aircraftGroup,0)))
    except:
        return Distance()

parkings = {
    GATE : {
        None : ( ),
        "1A" : (Terminal1, ),
        1 : (Terminal1, Gate1_Offset, ),
        3 : (Terminal1, Gate3_Offset, ),
        "3A" : (Terminal1, Gate3A_Offset, ),
        4 : (Terminal1, Gate4_Offset, ),
        5 : (Terminal1, Gate5_Offset, ),
        6 : (Terminal1, ),
        7 : (Terminal1, Gate7_Offset, ),
        9 : (Terminal1, Gate9_Offset, ),
        10 : (Terminal1, Gate10_Offset, ),
        11 : (Terminal1, Gate11_Offset, ),
        12 : (Terminal1, Gate12_Offset, ),
        14 : (Terminal1, Gate14_Offset, ),
        "14A" : (Terminal1JetwayINOP, Gate14A_Offset, ),
        15 : (Terminal1, ),
        16 : (Terminal1, Gate16_Offset, ),
        17 : (Terminal2, Gate17_18_Offset, ),
        18 : (Terminal2, Gate17_18_Offset, ),
        19 : (Terminal2, ),
        "19A" : (Terminal2JetwayINOP, Gate19A_Offset, ),
        20 : (Terminal2, ),
        "21A" : (Terminal2, Gate21A_Offset, ),
        21 : (Terminal2, ),
        "22A" : (Terminal2, ),
        22 : (Terminal2, Gate22_Offset, ),
        "22B" : (Terminal2, Gate22B_Offset, ),
        23 : (Terminal2, ),
        "24A" : (Terminal2, ),
        24 : (Terminal2, ),
        26 : (Terminal2, Gate26_27_Offset, ),
        27 : (Terminal2, Gate26_27_Offset, ),
        28 : (Terminal2, Gate28__31_Offset, ),
        29 : (Terminal2, Gate28__31_Offset, ),
        30 : (Terminal2, Gate28__31_Offset, ),
        31 : (Terminal2, Gate28__31_Offset, )
    },
    PARKING : {
        None : ( ),
        "24B" : (Terminal2JetwayINOP, ),
        "50A" : (RemoteStandsTaxiOut, Gate50A_Offset, ),
        50 : (RemoteStandsTaxiOut, Gate50_57_Offset, ),
        51 : (RemoteStandsTaxiOut, Gate50_57_Offset, ),
        52 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        53 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        54 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        55 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        56 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        57 : (RemoteStandsTaxiOut, Gate50_57_Offset,),
        58 : (RemoteStandsTaxiOut, ),
        "58A" : (RemoteStandsTaxiOut, ),
        60 : (RemoteStandsTaxiOut, Gate60_Offset, ),
        61 : (RemoteStandsTaxiOut, ),
        62 : (RemoteStandsTaxiOut, ),
        63 : (RemoteStandsTaxiOut, ),
        64 : (RemoteStandsTaxiOut, ),
        70 : (RemoteStands, Gate70_71_Offset, ),
        71 : (RemoteStands, Gate70_71_Offset, ),
        72 : (RemoteStands, Gate72_74_Offset, ),
        73 : (RemoteStands, Gate72_74_Offset, ),
        74 : (RemoteStands, Gate72_74_Offset, ),
        75 : (RemoteStands, Gate75_Offset, ),
        999 : (HangarF, ),
    },
    0 : {
        None : ( ),
        "1B" : (Terminal1JetwayINOP, ),
        "3B" : (Terminal1JetwayINOP, Gate3B_Offset, ),
        "4A" : (Terminal1, )
    },
    S_PARKING : {
        None : ( ),
        1 : (ApronSouthTaxiOut, ),
        2 : (ApronSouthTaxiOut, ),
        3 : (ApronSouthTaxiOut, ),
        4 : (ApronSouthTaxiOut, ),
        "5A" : (ApronSouthTaxiOut, ),
        5 : (ApronSouthTaxiOut, ),
        6 : (ApronSouthTaxiOut, ),
        "6A" : (ApronSouthTaxiOut, ),
        7 : (ApronSouthTaxiOut, ),
        "7A" : (ApronSouthTaxiOut, ),
        9 : (ApronSouthTaxiOut, ),
        14 : (ApronSouthTaxiOut, ),
        15 : (ApronSouthTaxiOut, ),
        16 : (ApronSouthTaxiOut, ),
        17 : (ApronSouthTaxiOut, ),
        "20A" : (ApronSouthTaxiOut, ),
        20 : (ApronSouthTaxiOut, ),
        21 : (ApronSouthTaxiOut, ),
        22 : (ApronSouthTaxiOut, ),
        "22A" : (ApronSouthTaxiOut, ),
        "23A" : (ApronSouthTaxiOut, ),
        23 : (ApronSouthTaxiOut, ),
        24 : (ApronSouthTaxiOut, ),
        25 : (ApronSouthTaxiOut, ),
        "25A" : (ApronSouthTaxiOut, ),
        "26B" : (ApronSouth, ),
        26 : (ApronSouth, ),
        "26A" : (ApronSouth, ),
        30 : (ApronSouth, )
    },
    E_PARKING : {
        None : ( ),
        3 : (ApronEast, StandE3_Offset,),
        4 : (ApronEast, StandE4_Offset,),
        "5A" : (ApronEast, StandE5A_Offset,),
        5 : (ApronEast, ),
        7 : (ApronEast, StandE7_Offset,)
    },
    N_PARKING : {
        None : ( ),
        "1A" : (ApronBell, ),
        1 : (ApronBell, ),
        "1B" : (ApronBell, )
    }
}