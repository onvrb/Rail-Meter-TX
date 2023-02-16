three_phase_dict={
    "Volts_AB": {"id": "Volts_AB", "address": 0x2000, "multiplier": 0.1, "unit": "V", "decimals": 1},
    "Volts_BC": {"id": "Volts_BC", "address": 0x2002, "multiplier": 0.1, "unit": "V", "decimals": 1},
    "Volts_CA": {"id": "Volts_CA", "address": 0x2004, "multiplier": 0.1, "unit": "V", "decimals": 1},
    
    "Volts_L1": {"id": "Volts_L1", "address": 0x2006, "multiplier": 0.1, "unit": "V", "decimals": 1},
    "Volts_L2": {"id": "Volts_L2", "address": 0x2008, "multiplier": 0.1, "unit": "V", "decimals": 1},
    "Volts_L3": {"id": "Volts_L3", "address": 0x200A, "multiplier": 0.1, "unit": "V", "decimals": 1},
    
    "Current_L1": {"id": "Current_L1", "address": 0x200C, "multiplier": 0.001, "unit": "A", "decimals": 3},
    "Current_L2": {"id": "Current_L2", "address": 0x200E, "multiplier": 0.001, "unit": "A", "decimals": 3},
    "Current_L3": {"id": "Current_L3", "address": 0x2010, "multiplier": 0.001, "unit": "A", "decimals": 3},
    
    "Combined_Active_Power": {"id": "Combined_Active_Power", "address": 0x2012, "multiplier": 0.1, "unit": "W", "decimals": 1},
    "Active_Power_L1": {"id": "Active_Power_L1", "address": 0x2014, "multiplier": 0.1, "unit": "W", "decimals": 1},
    "Active_Power_L2": {"id": "Active_Power_L2", "address": 0x2016, "multiplier": 0.1, "unit": "W", "decimals": 1},
    "Active_Power_L3": {"id": "Active_Power_L3", "address": 0x2018, "multiplier": 0.1, "unit": "W", "decimals": 1},
    
    # "Combined_Reactive_Power": {"id": "Combined_Reactive_Power", "address": 0x201A, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L1": {"id": "Reactive_Power_L1", "address": 0x201C, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L2": {"id": "Reactive_Power_L2", "address": 0x201E, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L3": {"id": "Reactive_Power_L3", "address": 0x2020, "multiplier": 0.1, "unit": "var", "decimals": 1},
    
    "Combined_Power_Factor": {"id": "Combined_Power_Factor", "address": 0x202A, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    "Power_Factor_L1": {"id": "Power_Factor_L1", "address": 0x202C, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    "Power_Factor_L2": {"id": "Power_Factor_L2", "address": 0x202E, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    "Power_Factor_L3": {"id": "Power_Factor_L3", "address": 0x2030, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    
    "Frequency_Of_Supply_Voltages": {"id": "Frequency_Of_Supply_Voltages", "address": 0x2044, "multiplier": 0.01, "unit": "Hz", "decimals": 2},
    
    "Total_Import_kWh": {"id": "Total_Import_kWh", "address": 0x101E, "multiplier": 1, "unit": "kWh", "decimals": 3},
    # "Total_Export_kWh": {"id": "Total_Export_kWh", "address": 0x1028, "multiplier": 1, "unit": "kWh", "decimals": 3},
    
    # "Total_Q1_kVArh": {"id": "Total_Q1_kVArh", "address": 0x1032, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q2_kVArh": {"id": "Total_Q2_kVArh", "address": 0x103C, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q3_kVArh": {"id": "Total_Q3_kVArh", "address": 0x1046, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q4_kVArh": {"id": "Total_Q4_kVArh", "address": 0x1050, "multiplier": 1, "unit": "kVArh", "decimals": 3},
}

single_phase_dict={
    # "Volts_AB": {"id": "Volts_AB", "address": 0x2000, "multiplier": 0.1, "unit": "V", "decimals": 1},
    # "Volts_BC": {"id": "Volts_BC", "address": 0x2002, "multiplier": 0.1, "unit": "V", "decimals": 1},
    # "Volts_CA": {"id": "Volts_CA", "address": 0x2004, "multiplier": 0.1, "unit": "V", "decimals": 1},
    
    "Volts_L1": {"id": "Volts_L1", "address": 0x2006, "multiplier": 0.1, "unit": "V", "decimals": 1},
    # "Volts_L2": {"id": "Volts_L2", "address": 0x2008, "multiplier": 0.1, "unit": "V", "decimals": 1},
    # "Volts_L3": {"id": "Volts_L3", "address": 0x200A, "multiplier": 0.1, "unit": "V", "decimals": 1},
    
    "Current_L1": {"id": "Current_L1", "address": 0x200C, "multiplier": 0.001, "unit": "A", "decimals": 3},
    # "Current_L2": {"id": "Current_L2", "address": 0x200E, "multiplier": 0.001, "unit": "A", "decimals": 3},
    # "Current_L3": {"id": "Current_L3", "address": 0x2010, "multiplier": 0.001, "unit": "A", "decimals": 3},
    
    "Combined_Active_Power": {"id": "Combined_Active_Power", "address": 0x2012, "multiplier": 0.1, "unit": "W", "decimals": 1},
    "Active_Power_L1": {"id": "Active_Power_L1", "address": 0x2014, "multiplier": 0.1, "unit": "W", "decimals": 1},
    # "Active_Power_L2": {"id": "Active_Power_L2", "address": 0x2016, "multiplier": 0.1, "unit": "W", "decimals": 1},
    # "Active_Power_L3": {"id": "Active_Power_L3", "address": 0x2018, "multiplier": 0.1, "unit": "W", "decimals": 1},
    
    # "Combined_Reactive_Power": {"id": "Combined_Reactive_Power", "address": 0x201A, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L1": {"id": "Reactive_Power_L1", "address": 0x201C, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L2": {"id": "Reactive_Power_L2", "address": 0x201E, "multiplier": 0.1, "unit": "var", "decimals": 1},
    # "Reactive_Power_L3": {"id": "Reactive_Power_L3", "address": 0x2020, "multiplier": 0.1, "unit": "var", "decimals": 1},
    
    "Combined_Power_Factor": {"id": "Combined_Power_Factor", "address": 0x202A, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    "Power_Factor_L1": {"id": "Power_Factor_L1", "address": 0x202C, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    # "Power_Factor_L2": {"id": "Power_Factor_L2", "address": 0x202E, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    # "Power_Factor_L3": {"id": "Power_Factor_L3", "address": 0x2030, "multiplier": 0.001, "unit": "PF", "decimals": 3},
    
    "Frequency_Of_Supply_Voltages": {"id": "Frequency_Of_Supply_Voltages", "address": 0x2044, "multiplier": 0.01, "unit": "Hz", "decimals": 2},
    
    "Total_Import_kWh": {"id": "Total_Import_kWh", "address": 0x101E, "multiplier": 1, "unit": "kWh", "decimals": 3},
    # "Total_Export_kWh": {"id": "Total_Export_kWh", "address": 0x1028, "multiplier": 1, "unit": "kWh", "decimals": 3},
    
    # "Total_Q1_kVArh": {"id": "Total_Q1_kVArh", "address": 0x1032, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q2_kVArh": {"id": "Total_Q2_kVArh", "address": 0x103C, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q3_kVArh": {"id": "Total_Q3_kVArh", "address": 0x1046, "multiplier": 1, "unit": "kVArh", "decimals": 3},
    # "Total_Q4_kVArh": {"id": "Total_Q4_kVArh", "address": 0x1050, "multiplier": 1, "unit": "kVArh", "decimals": 3},
}
