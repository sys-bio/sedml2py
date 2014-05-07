import SedmlToRr as s2p

#execfile("C:/TEMP/app2simworking.py");
#ret = s2p.sedml_to_python("C:/TEMP/app2sim/app2sim.sedml")
ret = s2p.sedml_to_python("C:/TEMP/asedmlComplex/asedmlComplex.sedml")
#ret = s2p.sedml_to_python("C:/TEMP/asedml3repeat/asedml3repeat.sedml")
#execfile("C:/TEMP/asedml3repeat/asedml3repeat.py")
#ret = s2p.sedml_to_python("C:/TEMP/app2sim.sedx")
#ret = s2p.sedml_to_python("C:/TEMP/BioModel1.sedml")
exec ret

