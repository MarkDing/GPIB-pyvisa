import visa


rm = visa.ResourceManager()
res = rm.list_resources()
print("Find following resources: ")
print(res)
print("Opening " + res[-1])

inst = rm.open_resource(res[-1])

# When sending command to E3631A, The "Rmt" and "Adrs" icon are on on the display
# panel. All input from panel are inactived, util you press "Store/Local" button.

inst.query("*IDN?")

inst.write("INST P6V") # Select +6V output
inst.write("VOLT 2.0") # Set output voltage to 3.0 V
inst.write("CURR 1.0") # Set output current to 1.0 A

# The APPLy command provides the most straightforward method to program the
# power supply over the remote interface.
#  inst.write("APPL P6V, 3.0, 1.0")


# power on/off
inst.write("OUTP OFF")
inst.write("OUTP ON")
