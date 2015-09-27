# Introduction #
OpenProc is an Open Source Process Modelling Application.
It will primarily be based on a fluid flow model based on simple components - pipes, pumps, valves, vessels etc.
It will also be able to model other process parameters such as fluid and pipework temperatures, heat transfer through heat exchangers etc.

The objective of the project is to provide a free-open-source solver for these common engineering problems.  It is intended to bridge the gap between simple 'back of the envelope' calculations and detailed analysis using commercial process modelling applications such as Hysis or Flowmaster.

There will be three distinct modules to the project -  A graphical user interface to build the model, a solver, and a back-end post processor for data visualisation.

The bulk of the code will be written in Python for portability, but the solver may use native code for speed if necessary.

**NOTE:  There is no code associated with this project yet - these pages set out the design intent before coding starts!!!**

# Processes to Model #
OpenProc will basically be a network solver for both steady state and transient response.
The basic network construction is described in NetworkDescription.  The following processes will be supported:
  1. FluidFlowInConduits - pipes, pumps, vessels, valves etc.
  1. ThermalAnalysis     - Thermal conduction in solids, convection and radiation.

# Technologies to Use #
The bulk of the application will be written in Python for portability.  The GUI will use either GTK or QT bindings for python.

The main data file containing the model will be XML, as will the model output.

I will attempt to use numPy code for the solver, but it is possible that a native code solver will be written from scratch for speed.

A facility will be provided to write python code that will be called before and after each iteration of the solver.  The code will have complete access to the dataset to allow for custom models (such as control systems, fault simulation etc.) to be included.

# Database #
The model will need a significant amount of material properties data values to be useful.  A database of standard properties will be provided as a separate XML file, but it will be possible to define properties within the model itself if required.