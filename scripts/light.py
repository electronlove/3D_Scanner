#!/user/bin/python
import tsl2591

tsl = tsl2591.Tsl2591() # initialize
full, ir = tsl.get_full_luminosity() #read raw values (full spectrum and ir spectrum)
lux = tsl.calculate_lux(full, ir) # convert raw values to lux 
for i in range(0,10000):
	print lux, full, ir

