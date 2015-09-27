The fluid flow model will be based on the standard methodology for determining the flow resistance of pipes, valves and fitings described in [Crane](http://www.flowoffluids.com/tp410.htm).
For the purposes of fluid flow modelling the following node and link types will be defined:


# Node Types #
  1. Mass Balance:  Mass Balance nodes are simple connections between pipes, pumps etc.  The solver will vary the pressure of the node to achieve a mass balance.   For most mass balance nodes it will solve for zero mass difference between the flow rates in to and out of the node.  A source term can be defined for the node which is a fixed flow rate into or out of the node if required.
  1. Pressure:  Pressure nodes have fixed pressure.  The solver will alter the pressures of other nodes to achieve a mass balance without altering the pressures of these nodes.
  1. Volume:  Do we need a separate node type for volumes such as storage vessels?  Could it just be a Mass Balance node with a volume property?

# Link Types #
  1. Pipe:  A pipe of specified length, diameter and surface roughness.  This will allow the flow rate to be calculated using Darcy's Formula.
  1. Elbow:  A pipe Elbow
  1. Reducer:  A pipe Reducer
  1. CPump:  A centrifugal pump
  1. DPump:  A positive displacement pump
  1. Valve:  A valve, which is a flow resistance, defined by valve position and type.