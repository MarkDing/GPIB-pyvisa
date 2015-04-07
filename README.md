Using pyvisa to control instrument via GPIB
===========================

## 1. Introduction
We have met several issues which related with power on/off operation. The failure rate is extremely low which is not efficiency for manual operation. So we would like to setup an automatic testing environment. The GPIB(General Purpose Interface Bus) is the way to control the instrument. This article shows how to control the Agilent E3631A (Triple Output DC Power Supply).

## 2. GPIB Interface
Here is the Agilent 82357A USB/GPIB Interface in our hand. Following link shows the detailed information. 
http://www.keysight.com/en/pd-1000004416%3Aepsg%3Apro-pn-82357A/usb-gpib-interface?cc=US&lc=eng

## 3. Pyvisa installation
Pyvisa is a Python package for support of the "Virtual Instrument Software Architecture" (VISA), in order to control measurement devices and test equipment via GPIB, RS232, Ethernet or USB.
To install the  pyvisa by using pip:
$ pip install pyvisa 

Detailed information can be found in https://github.com/hgrecco/pyvisa

## 4. NI driver installation
Pyvisa has been tested with NI-VISA 3.2, which needs us to install its driver. 
Download and install NIVISA541full.exe from following link http://www.ni.com/download/ni-visa-5.4.1/4626/en/ 

## 5. Agilent driver installation.
The GPIB interface is Agilent product, which needs its driver installed. 
Download and install the latest IOLibSuite_17_0_19013.exe from following link. 
http://www.keysight.com/main/software.jspx?ckey=1184883&lc=chi&cc=CN&nid=-34027.536881832&id=1184883 

## 6. Using HP Agilent 82357A/82357B GPIB in NI
http://digital.ni.com/public.nsf/allkb/F7C187DBF09EBE1186256F550065BD32
In order to use the NI VISA drivers and both the HP Agilent and NI GPIB devices, you will need to enable: 

* NIVISATulip.dll
* NI 488.2 from within the Agilent libraries

Complete the steps in the following document to enable NIVISATulip.dll:
KnowledgeBase 20KG1C7Z: Can I Use Both National Instruments (GPIB) and Agilent/HP (HPIB) Controllers in the Same System? (http://digital.ni.com/public.nsf/websearch/3B3626D9C1F999218625694200791AD7?OpenDocument)

Complete the following steps to enable NI 488.2 from within Agilent Connection Expert 15.x and 16.x: 

* Select Tools»Agilent 488 from the pulldown menu.
* Select the Agilent 488 Options tab.
* Check Enable Agilent GPIB cards for 488 programs.

## 7. Agilent E3631A spec download
Download spec from  http://www.keysight.com/main/techSupport.jspx?cc=CN&lc=chi&nid=-35721.384004.08&pid=836433&pageMode=OV

Here is part of the command list: 

```
APPLy {P6V|P25V|N25V}[,{<voltage>|DEF|MIN|MAX}[,{ <current>|DEF|MIN|MAX}]]
    APPLy? [{P6V|P25V|N25V}]
OUTPut
    [:STATe] {OFF|ON}
    [:STATe]?
    :TRACk[:STATe] {OFF|ON}
    :TRACk[:STATe]?
```

## 8. Pyvisa tutorial
From pyvisa official website, we can find the tutorial https://pyvisa.readthedocs.org/en/master/tutorial.html. 

Here is the example code to control E3631A output. 

```python
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

```



