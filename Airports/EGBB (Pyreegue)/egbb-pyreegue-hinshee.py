# -- coding: utf-8 --

version = 1.1
msfs_mode = 1
icao = "egbb"

@AlternativeStopPositions
def customOffset_Stand(aircraftData):
	table = {
		0: 0,
		318: 0,
		319: 0,
		320: 0,
		321: 0,
		737: 0,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate(aircraftData):
	table = {
		0: 0,
		318: 0,
		319: 0,
		320: 0,
		321: 0,
		737: 0,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate42C(aircraftData):
	table = {
		0: 0,
		787: 8.5,
        747: 10.8,
        767: 10.8,
	}

	table777 = {
		200: 10.8,
		300: 13.55,
	}
    
	table330 = {
		2: 8.5,
		3: 10.8,
	}

	try:
		if aircraftData.idMajor == 777:
			return Distance.fromMeters(table777.get(aircraftData.idMinor, 0) - 0.25)
		elif aircraftData.idMajor == 330:
			return Distance.fromMeters(table330.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate54C(aircraftData):
	table = {
		0: 0,
		330: 2.4,
        767: 2.4,
        777: 7.4,
        350: 7.4,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate54L(aircraftData):
	table = {
		0: 0,
		737: 4.6,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate55R(aircraftData):
	table = {
		0: 0,
		737: -1.6,
        320: -1.6,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate55C(aircraftData):
	table = {
		0: 0,
		330: 2.4,
        767: 2.4,
        777: 7.5,
        350: 7.5,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate55L(aircraftData):
	table = {
		0: 0,
		737: -1.6,
        320: -1.6,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate56R(aircraftData):
	table = {
		0: 0,
        170: 1.7,
        175: 1.7,
        190: 2.1,
        195: 2.1,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate56C(aircraftData):
	table = {
		0: 0,
        767: 2.1,
        350: 8.1,
	}
	
	table340 = {
        3: 2.1,
    }
	
	table777 = {
        300: 8.1,
    }
    
	try:
		if aircraftData.idMajor == 777:
			return Distance.fromMeters(table777.get(aircraftData.idMinor, 0) - 0.25)
		elif aircraftData.idMajor == 340:
			return Distance.fromMeters(table340.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate56L(aircraftData):
	table = {
		0: 0,
		737: 1.7,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate57R(aircraftData):
	table = {
		0: 0,
		767: -1.2,
        320: -1.9,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate57C(aircraftData):
	table = {
		0: 0,
		767: 1.8,
        777: 6.8,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate57L(aircraftData):
	table = {
		0: 0,
		737: 1.8,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate58(aircraftData):
	table = {
		0: 0,
		757: 6.6,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate41R(aircraftData):
	table = {
		0: 0,
		737: 2.2,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate41C(aircraftData):
	table = {
		0: 0,
		737: -1.9,
        757: 3.1,
        787: 4.1,
        747: 7.1,
        767: 7.1,
	}

	table777 = {
		200: 7,
		300: 9,
	}

	table330 = {
		2: 4,
		3: 7,
	}

	try:
		if aircraftData.idMajor == 777:
			return Distance.fromMeters(table777.get(aircraftData.idMinor, 0) - 0.25)
		elif aircraftData.idMajor == 330:
			return Distance.fromMeters(table330.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate41L(aircraftData):
	table = {
		0: 0,
		737: 2.1,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate42R(aircraftData):
	table = {
		0: 0,
		737: 2.1,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate42L(aircraftData):
	table = {
		0: 0,
		737: 2.1,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Stand85C(aircraftData):
	table = {
		0: 0,
		787: 2.6,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def customOffset_Stand84C(aircraftData):
	table = {
		0: 0,
		330: 2.5,
        767: 2.5,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()
        
@AlternativeStopPositions
def customOffset_Stand81(aircraftData):
	table = {
		0: 0,
        767: 3.9,
	}

	try:
		return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )

def RemoteStandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§ (Remote)" % (name, letter), priority )
  
def StandNames(name, letter, priority):
    return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
    
SPSN = TerminalNames("South Pier (1-16, 20-25)", "", 1)
SPRSN = RemoteStandNames("South Pier (1-16, 20-25)", "", 1)
NPSN = TerminalNames("North Pier (40-42, 54-60)", "", 2)
WRSN = RemoteStandNames("Western Remote Stands (70-77, 80-86)", "", 3)
EAN = StandNames("Elmdon Apron", "", 4)


parkings = {
    GATE: {
        None: ( ),
			1 : (SPSN, customOffset_Gate),
			2 : (SPSN, customOffset_Gate),
			3 : (SPSN, customOffset_Gate),
			4 : (SPSN, customOffset_Gate),
            5 : (SPSN, customOffset_Gate),
            6 : (SPSN, customOffset_Gate),
            7 : (SPSN, customOffset_Gate),
            8 : (SPSN, customOffset_Gate),
            12 : (SPSN, customOffset_Gate),
            13 : (SPSN, customOffset_Gate),
            14 : (SPSN, customOffset_Gate),
            15 : (SPSN, customOffset_Gate),
            16 : (SPSN, customOffset_Gate),
            20 : (SPRSN, customOffset_Stand),
            21 : (SPRSN, customOffset_Stand),
            22 : (SPRSN, customOffset_Stand),
            23 : (SPRSN, customOffset_Stand),
            24 : (SPRSN, customOffset_Stand),
            25 : (SPRSN, customOffset_Stand),
            40 : (NPSN, customOffset_Gate),
            "41R" : (NPSN, customOffset_Gate41R),
            "41C" : (NPSN, customOffset_Gate41C),
            "41L" : (NPSN, customOffset_Gate41L),
            "42R" : (NPSN, customOffset_Gate42R),
            "42C" : (NPSN, customOffset_Gate42C),
            "42L" : (NPSN, customOffset_Gate42L),
            "54R" : (NPSN, customOffset_Gate),
            "54C" : (NPSN, customOffset_Gate54C),
            "54L" : (NPSN, customOffset_Gate54L),
            "55R" : (NPSN, customOffset_Gate55R),
            "55C" : (NPSN, customOffset_Gate55C),
            "55L" : (NPSN, customOffset_Gate55L),
            "56R" : (NPSN, customOffset_Gate56R),
            "56C" : (NPSN, customOffset_Gate56C),
            "56L" : (NPSN, customOffset_Gate56L),
            "57R" : (NPSN, customOffset_Gate57R),
            "57C" : (NPSN, customOffset_Gate57C),
            "57L" : (NPSN, customOffset_Gate57L),
            58 : (NPSN, customOffset_Gate58),
            59 : (NPSN, customOffset_Gate),
            60 : (NPSN, customOffset_Gate),
    },
    PARKING: {
        None: ( ),
            "1X" : (EAN, customOffset_Stand),
            70 : (WRSN, customOffset_Stand),
            71 : (WRSN, customOffset_Stand),
            72 : (WRSN, customOffset_Stand),
            73 : (WRSN, customOffset_Stand),
            74 : (WRSN, customOffset_Stand),
            75 : (WRSN, customOffset_Stand),
            76 : (WRSN, customOffset_Stand),
            77 : (WRSN, customOffset_Stand),
            81 : (WRSN, customOffset_Stand81),
            82 : (WRSN, customOffset_Stand),
            "83L" : (WRSN, customOffset_Stand),
            "83C" : (WRSN, customOffset_Stand),
            "83R" : (WRSN, customOffset_Stand),
            "84L" : (WRSN, customOffset_Stand),
            "84C" : (WRSN, customOffset_Stand84C),
            "84R" : (WRSN, customOffset_Stand),
            "85L" : (WRSN, customOffset_Stand),
            "85C" : (WRSN, customOffset_Stand85C),
            "85R" : (WRSN, customOffset_Stand),
            "86L" : (WRSN, customOffset_Stand),
            "86C" : (WRSN, customOffset_Stand),
            "86R" : (WRSN, customOffset_Stand),
            "501L" : (EAN, customOffset_Stand),
            "501C" : (EAN, customOffset_Stand),
            "501R" : (EAN, customOffset_Stand),
            "502L" : (EAN, customOffset_Stand),
            "502C" : (EAN, customOffset_Stand),
            "502R" : (EAN, customOffset_Stand),
            "503L" : (EAN, customOffset_Stand),
            "503C" : (EAN, customOffset_Stand),
            "503R" : (EAN, customOffset_Stand),
            "504L" : (EAN, customOffset_Stand),
            "504C" : (EAN, customOffset_Stand),
            "504R" : (EAN, customOffset_Stand),
            505 : (EAN, customOffset_Stand),
            506 : (EAN, customOffset_Stand),
            "601L" : (EAN, customOffset_Stand),
            "601R" : (EAN, customOffset_Stand),
    },
}