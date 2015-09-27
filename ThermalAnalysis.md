This page will describe the nodes and links that can be defined to produce a thermal model using OpenProc.

# Node Types #
  1. Heat Balance:  The solver varies the temperature of heat balance nodes to achieve the required balance between heat flows in to and out of the node.  A source term can be defined to either input or remove heat at a fixed rate from the node in addition to the links connecting to it.
  1. Temperature:  Temperature nodes have a fixed temperature.  Heat will be input or removed from the node by the solver to maintain the temperature at the required value.

# Link Types #
  1. Conduction:  Simple thermal condution link with a thermal conductance defined.
  1. Convection:  Thermal convection link with a convection hA defined (heat transfer coefficient x Area).
  1. Radiation:   Thermal radiation link with a radiative conductance defined.


# Combined Fluid/Thermal Solution #
How do we do this?  Will need a different link which has both thermal and fluid flow properties?  OR should they all have both properties?  Bit of thinking required for this....