#CountOnMe Makefile

PYTH = python3
ZIP = xseman06_xgrecn00_xbaumg01_xpogad00
GUI = CountOnMeGUI.py
PROFIL = Standart_deviation.py
TESTS = Lib_tests.py
UT = unittest

# PHONY Declaration
.PHONY: help all pack clean test doc run profile

help:
	@echo "Simple calculator named CountOnMe																				"
	@echo "Usage: make (OPTIONS)																							"
	@echo "-----------------------------------------------------------------------------------------------------------------"
	@echo "OPTIONS: (please choose one of the options below)					  		 									"
	@echo "	help: 	 prints usage of the Makefile (with a description of what needs to be done before starting the program) "
	@echo "	all:  	 compiles the whole project, including the profiling program											"
	@echo "	pack: 	 zips the project so that it can be submitted															"
	@echo "	test: 	 runs math library tests																				"
	@echo "	run:	 runs the calculator																					"
	@echo "	doc:	 starts the documentation of the project																"
	@echo "	profile: runs the program for calculation of decisive derivant for profiling									"
	@echo "	clean: 	 deletes all files that should not be committed  													  	"

# Option that installs all the required packages for the calculator to run
all:
	sudo apt install python3 && sudo apt install python3-pip && sudo apt install python3-tk

# Option that packs and makes the zip of the contents of the project for handing out the project
pack: clean
	rm -rf ../../$(ZIP).zip ../../$(ZIP)
	cd ../../ && mkdir $(ZIP)
	zip -r $(ZIP).zip 
	rm -rf ../../$(ZIPNAME)

# Option that cleans (removes) all the files and directories that aren't necessary for handing out the project
clean:
	rm -rf __pycache__
	rm -f doxygen_errors.log

# Option that runs the test for the math library
test: $(TESTS)
	$(PYTH) -m $(UT) $<

# Option that start the documentation of
doc: clean
	doxygen

# Option that will run the calculator
run: $(GUI)
	$(PYTH) $<

# Option that runs the profiling
profile: $(PROFIL) 
	@ $(PYTH) $< *.txt