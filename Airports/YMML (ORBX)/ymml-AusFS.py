# -- coding: utf-8 --

msfs_mode = 1
icao = "ymml"

default_parking_type = "Bay"

# -- UIGrouping Definitions --
#
# (Priority, GroupingName)
# Priority is UI Order (1 is top of list)
# GroupingName is UI Grouping

DomQF = (1, "T1 Qantas Domestic (B/C)")
Intl   = (2, "T2 International (D)")
DomVA = (3, "T3/4 Virgin Australia Domestic (E)")
DomCUT = (4, "T3/4 Common User Domestic (F)")
DomJQ = (5, "T3/4 Jetstar Domestic (G)")
Freight = (6, "Freight Apron (H)")
ParkingNorth   = (7, "Parking North (D)")
ParkingWest   = (8, "Parking West (F/G)")

MJB = (9, "Melbourne Jet Base")
Hangar = (10, "Hangars")

# -- Function Definitions --
#
# ManualNames - Used when scenery naming is incorrect
#    UIGrouping + Position Name
#        UIGrouping can be UIGrouping or manually defined. e.g. (1, "Test Terminal")
#        positionName must be entire name. e.g. "Bay 1L"

def ManualNames(grouping, positionName):
    priority, groupingName = grouping
    return CustomizedName("%s|%s" % (groupingName, positionName), priority)

def PresetNames(grouping, extraSuffix = "", parkingType = default_parking_type):
    priority, groupingName = grouping
    return CustomizedName("%s|%s #§ %s" % (groupingName, parkingType, extraSuffix), priority)

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
	try:
		# Try to get the value using idMinor
		return specificTables[aircraftData.idMajor][0].get(aircraftData.idMinor)
	except:
		try:
			# Fallback to the default key (second item in the tuple) if idMinor lookup fails
			return specificTables[aircraftData.idMajor][0].get(specificTables[aircraftData.idMajor][1])
		except:
			# If both lookups fail, use the generic table with a default value of 0 if idMajor isn't found
			return genericTable.get(aircraftData.idMajor, 0)

def subtract_from_result(result, value_to_subtract):
	if isinstance(result, tuple):
		new_first_element = Distance.fromMeters(result[0] - value_to_subtract)
		new_second_element = Distance.fromMeters(result[1])
		return (new_first_element, new_second_element)
	else:
		return Distance.fromMeters(result - value_to_subtract)

@AlternativeStopPositions
def customOffsetC3(aircraftData):
	table = {
		0: 0,
		747: 4.2,
		330: 4.2,
		787: 9.8,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetC11(aircraftData):
	table = {
		0: 0,
		767: 7.2,
		747: 9.9,
		787: 9.9,
		330: 9.9,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB21(aircraftData):
	table = {
		0: 0,
		11: 4.0,
		747: 8.5,
		787: 10.7,
		330: 13.3,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB22(aircraftData):
	table = {
		0: 0,
		737: 2.4,
		717: 4.1,
		320: 5.2,
		321: 5.2,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB24(aircraftData):
	table = {
		0: 0,
		737: 4.1,
		717: 5.8,
		320: 8.9,
		321: 8.9,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB25(aircraftData):
	table = {
		0: 0,
		320: 2.1,
		190: 6.0,
		737: 6.0,
		321: 6.0,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB26(aircraftData):
	table = {
		0: 0,
		320: 3.2,
		737: 4.3,
		321: 7.5,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB27(aircraftData):
	table = {
		0: 0,
		737: 3.7,
		321: 3.7,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB28(aircraftData):
	table = {
		0: 0,
		320: 4.7,
		737: 6.7,
		321: 8.0,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetB30(aircraftData):
	table = {
		0: 0,
		1008: 6.5,
		737: 10.0,
		320: 10.0,
		321: 12.5,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetD5(aircraftData):
	table = {
		0: 0,
		11: 0,
		10: 0,
		300: 1.2,
		310: 1.2,
		320: 2.5,
		737: 6.6,
		767: 6.6,
		747: 8.7,
		}
	table777 = {
		0: 0.0,
		200: 4.15,
		300: 10.1,
	}
	table350 = {
		0: 0.0,
		900: 4.15,
		1000: 10.1,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0),350 : (table350, 0)},table))

@AlternativeStopPositions
def customOffsetD7(aircraftData):
	table = {
		0: 0,
		340: 0.65,
		300: 3.8,
		767: 3.8,
		380: 6.4,
		11: 6.4,
		777: 7.0,
		350: 7.0,
		}
		
	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetD8(aircraftData):
	table = {
		0: 0,
		320: 0.75,
		321: 1.55,
		300: 3.1,
		787: 3.1,
		747: 7.1,
		}
	table777 = {
		0: 0.0,
		200: 6.1,
		300: 7.1,
	}
	table350 = {
		0: 0.0,
		900: 6.1,
		1000: 7.1,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0),350 : (table350, 0)},table))

@AlternativeStopPositions
def customOffsetD9(aircraftData):
	table = {
		0: 0,
		320: 0,
		310: 3.1,
		300: 7.4,
		747: 12.7,
		11: 12.7,
		380: 18.7,
		777: 18.7,
		350: 18.7,
	}
	table767 = {
		0: 0.0,
		300: 3.1,
		200: 3.1,
		400: 7.4,
	}
	table787 = {
		0: 0.0,
		8: 11.0,
		9: 14.2,
		10: 14.2,
	}
	table330 = {
		0: 0.0,
		200: 11.0,
		300: 12.7,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{
			767 : (table767, 0),
			787 : (table787, 0),
			330 : (table330, 0),
		},
		table))

@AlternativeStopPositions
def customOffsetD10(aircraftData):
	table = {
		0: 0,
		717: 5.75,
		737: 5.75,
		747: 6.8,
		767: 8.35,
		330: 9.65,
		787: 9.65,
		11: 12.7,
		}
	table777 = {
		0: 0.0,
		200: 8.35,
		300: 14.75,
	}
	table350 = {
		0: 0.0,
		900: 8.35,
		1000: 14.75,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0),350 : (table350, 0)},table))

@AlternativeStopPositions
def customOffsetD11(aircraftData):
	table = {
		0: 0,
		787: 9.5,
		11: 9.5,
		747: 10.6,
		340: 11.5,
		330: 12.8,
		}
	table777 = {
		0: 0.0,
		200: 10.6,
		300: 12.8,
	}
	table350 = {
		0: 0.0,
		900: 10.6,
		1000: 12.8,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {777 : (table777, 0),350 : (table350, 0)},table))

@AlternativeStopPositions
def customOffsetD12(aircraftData):
	table = {
		0: 0,
		787: 7.2,
		350: 7.2,
		}
	table330 = {
		0: 0.0,
		200: 5.6,
		300: 3.7,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {330 : (table330, 0)},table))

@AlternativeStopPositions
def customOffsetD14A(aircraftData):
	table = {
		0: 0,
		767: 2.85,
		340: 3.5,
		777: 5.5,
		350: 5.5,
		747: 7.1,
		}
	table787 = {
		0: 0.0,
		8: 0.0,
		9: 0.7,
	}
	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, {787 : (table787, 0)},table))

@AlternativeStopPositions
def customOffsetD16(aircraftData):
	table = {
		0: 0,
		11: 0.0,
		767: 1.3,
		330: 2.7,
		747: 6.1,
		380: 6.9,
	}
	table777 = {
		0: 0.0,
		200: 1.3,
		300: 6.9,
	}
	table350 = {
		0: 0.0,
		900: 1.3,
		1000: 6.9,
	}
	table787 = {
		0: 0.0,
		8: 0.0,
		9: 2.7,
	}

	global HandleAircraftOffsets
	return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{
			777 : (table777, 0),
			787 : (table787, 0),
			350 : (table350, 0),
		},
		table))

@AlternativeStopPositions
def customOffsetD18(aircraftData):
	table = {
		0: 0,
		767: 0.0,
		330: 1.25,
		747: 1.25,
		11: 2.6,
	}
	table777 = {
		0: 0.0,
		200: 0.0,
		300: 7.8,
	}
	table350 = {
		0: 0.0,
		900: 0.0,
		1000: 7.8,
	}
	table787 = {
		0: 0.0,
		8: 2.6,
		9: 6.3,
	}
	if aircraftData.idMajor == 380:
		return (Distance.fromMeters(6.35), Distance.fromMeters(-7.3) )
	else:
		return Distance.fromMeters(HandleAircraftOffsets( aircraftData, 
		{
			777 : (table777, 0),
			787 : (table787, 0),
			350 : (table350, 0),
		},
		table))
		

@AlternativeStopPositions
def customOffsetD20(aircraftData):
	table = {
		0: 0,
		747: 1.3,
		11: 1.3,
		787: 1.3,
		330: 3.2,
		777: 6.0,
		350: 6.0,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetE8(aircraftData):
	table = {
		0: 0,
		170: 1.1,
		190: 1.1,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetE10(aircraftData):
	table = {
		0: 0,
		170: 2.8,
		190: 2.8,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetF12(aircraftData):
	table = {
		0: 0,
		330: 4.1,
		787: 4.1,
		170: 9.7,
		320: 12.6,
		737: 12.6,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetF17(aircraftData):
	table = {
		0: 0,
		42: 3.3,
		1008: 8.7,
		320: 14.7,
		321: 14.7,
		737: 17.7,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetF19(aircraftData):
	table = {
		0: 0,
		320: 6.1,
		170: 6.1,
		737: 9.2,
		190: 9.2,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetF21(aircraftData):
	table = {
		0: 0,
		320: 3.8,
		737: 4.8,
		190: 4.8,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetG41(aircraftData):
	table = {
		0: 0,
		737: 3.4,
		321: 3.4,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetG43(aircraftData):
	table = {
		0: 0,
		737: 4.0,
		321: 4.0,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetG48(aircraftData):
	table = {
		0: 0,
		321: 4.0,
		737: 8.2,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetG50(aircraftData):
	table = {
		0: 0,
		737: 3.1,
		321: 3.1,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

@AlternativeStopPositions
def customOffsetG51(aircraftData):
	table = {
		0: 0,
		737: 2.9,
		321: 2.9,
		}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0))

parkings = {
	GATE_B : {
		None : ( ),
		21    : (PresetNames(DomQF, "", "Bay B"), customOffsetB21),
		22    : (PresetNames(DomQF, "", "Bay B"), customOffsetB22),
		23    : (PresetNames(DomQF, "", "Bay B"), customOffsetB21),
		24    : (PresetNames(DomQF, "", "Bay B"), customOffsetB24),
		25    : (PresetNames(DomQF, "", "Bay B"), customOffsetB25),
		26    : (PresetNames(DomQF, "", "Bay B"), customOffsetB26),
		27    : (PresetNames(DomQF, "", "Bay B"), customOffsetB27),
		28    : (PresetNames(DomQF, "", "Bay B"), customOffsetB28),
		29    : (PresetNames(DomQF, "", "Bay B"), ),
		30    : (PresetNames(DomQF, "", "Bay B"), customOffsetB30),
	},

	GATE_C : {
		None : ( ),
		1    : (PresetNames(DomQF, "", "Bay C"), ),
		2    : (PresetNames(DomQF, "", "Bay C"), ),
		3    : (PresetNames(DomQF, "", "Bay C"), customOffsetC3),
		4    : (PresetNames(DomQF, "", "Bay C"), ),
		5    : (PresetNames(DomQF, "", "Stand C"), ),
		6    : (PresetNames(DomQF, "", "Bay C"), ),
		7    : (PresetNames(DomQF, "", "Bay C"), ),
		8    : (PresetNames(DomQF, "", "Bay C"), ),
		9    : (PresetNames(DomQF, "", "Bay C"), ),
		10   : (PresetNames(DomQF, "", "Bay C"), ),
		11   : (PresetNames(DomQF, "", "Bay C"), customOffsetC11),
		12   : (PresetNames(DomQF, "", "Bay C"), ),
	},

	GATE_D : {
		None : ( ),
		2    : (PresetNames(Intl, "", "Bay D"), ),
		3    : (PresetNames(Intl, "", "Bay D"), ),
		4    : (PresetNames(Intl, "", "Bay D"), ),
		5    : (PresetNames(Intl, "", "Bay D"), customOffsetD5),
		6    : (PresetNames(Intl, "", "Bay D"), ),
		7    : (PresetNames(Intl, "", "Bay D"), customOffsetD7),
		8    : (PresetNames(Intl, "", "Bay D"), customOffsetD8),
		9    : (PresetNames(Intl, "", "Bay D"), customOffsetD9),
		10   : (PresetNames(Intl, "", "Bay D"), customOffsetD10),
		11   : (PresetNames(Intl, "", "Bay D"), customOffsetD11),
		12   : (PresetNames(Intl, "", "Bay D"), customOffsetD12),
		14   : (PresetNames(Intl, "", "Bay D"), customOffsetD14A),
		16   : (PresetNames(Intl, "", "Bay D"), customOffsetD16),
		18   : (PresetNames(Intl, "", "Bay D"), customOffsetD18),
		20   : (PresetNames(Intl, "", "Bay D"), customOffsetD20),

		13   : (PresetNames(ParkingNorth, "", "Stand D"), ),
		15   : (PresetNames(ParkingNorth, "", "Stand D"), ),
		17   : (PresetNames(ParkingNorth, "", "Stand D"), ),
		19   : (PresetNames(ParkingNorth, "", "Stand D"), ),
	},

	GATE_E : {
		None : ( ),
		1    : (PresetNames(DomVA, "", "Bay E"), ),
		2    : (PresetNames(DomVA, "", "Bay E"), ),
		3    : (PresetNames(DomVA, "", "Bay E"), ),
		4    : (PresetNames(DomVA, "", "Bay E"), ),
		5    : (PresetNames(DomVA, "", "Bay E"), ),
		6    : (PresetNames(DomVA, "", "Bay E"), ),
		7    : (PresetNames(DomVA, "", "Bay E"), ),
		8    : (PresetNames(DomVA, "", "Bay E"), customOffsetE8),
		9    : (PresetNames(DomVA, "", "Bay E"), ),
		10   : (PresetNames(DomVA, "", "Bay E"), customOffsetE10),
	},

	GATE_F : {
		None : ( ),
		11   : (PresetNames(DomCUT, "", "Bay F"), ),
		12   : (PresetNames(DomCUT, "", "Bay F"), customOffsetF12),
		13   : (PresetNames(DomCUT, "", "Bay F"), ),
		14   : (PresetNames(DomCUT, "", "Bay F"), ),
		15   : (PresetNames(DomCUT, "", "Bay F"), ),
		16   : (PresetNames(DomCUT, "", "Bay F"), ),
		17   : (PresetNames(DomCUT, "", "Bay F"), customOffsetF17),
		18   : (PresetNames(DomCUT, "", "Bay F"), ),
		19   : (PresetNames(DomCUT, "", "Bay F"), customOffsetF19),
		20   : (PresetNames(DomCUT, "", "Bay F"), ),
		21   : (PresetNames(DomCUT, "", "Bay F"), customOffsetF21),
		22   : (PresetNames(DomCUT, "", "Bay F"), ),
		23   : (PresetNames(DomCUT, "", "Bay F"), ),
		24   : (PresetNames(DomCUT, "", "Bay F"), ),
		25   : (PresetNames(DomCUT, "", "Bay F"), ),
	},

	GATE_G : {
		None : ( ),
		41   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG41),
		42   : (PresetNames(DomJQ, "", "Bay G"), ),
		43   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG43),
		44   : (PresetNames(DomJQ, "", "Bay G"), ),
		45   : (PresetNames(DomJQ, "", "Bay G"), ),
		46   : (PresetNames(DomJQ, "", "Bay G"), ),
		47   : (PresetNames(DomJQ, "", "Bay G"), ),
		48   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG48),
		49   : (PresetNames(DomJQ, "", "Bay G"), ),
		50   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG50),
		51   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG51),
		52   : (PresetNames(DomJQ, "", "Bay G"), customOffsetG51),

		54   : (PresetNames(ParkingWest, "", "Stand G"), ),
		56   : (PresetNames(ParkingWest, "", "Stand G"), ),
		58   : (PresetNames(ParkingWest, "", "Stand G"), ),
		60   : (PresetNames(ParkingWest, "", "Stand G"), ),
		59   : (PresetNames(ParkingWest, "", "Stand G"), ),
		57   : (PresetNames(ParkingWest, "", "Stand G"), ),
	},

	GATE_H : {
		None : ( ),
		1   : (PresetNames(Freight, "", "Stand H"), ),
		2   : (PresetNames(Freight, "", "Stand H"), ),
		3   : (PresetNames(Freight, "", "Stand H"), ),
	},
	
	S_PARKING : {
		None : ( ),
		1    : (ManualNames(MJB, "Parking 1"), ),
		2    : (ManualNames(MJB, "Parking 2"), ),
		3    : (ManualNames(MJB, "Parking 3"), ),
		4    : (ManualNames(MJB, "Parking 4"), ),
		5    : (ManualNames(MJB, "Parking 5"), ),
		6    : (ManualNames(MJB, "Parking 6"), ),
		8    : (ManualNames(MJB, "Parking 8"), ),
		14    : (ManualNames(MJB, "Parking 14"), ),
		15    : (ManualNames(MJB, "Parking 15"), ),
		20    : (ManualNames(Hangar, "Jetstar"), ),
		21    : (ManualNames(Hangar, "Qantas | 1"), ),
		22    : (ManualNames(Hangar, "Qantas | 2"), ),
		},
	SE_PARKING : {
		None : ( ),
		1    : (ManualNames(Hangar, "Virgin Australia | 1"), ),
		3    : (ManualNames(Hangar, "Virgin Australia | 2"), ),
		4    : (ManualNames(Hangar, "Virgin Australia | 3"), ),
		},
}