# Simple Thermal Model #
This is a trivial model with two fixed temperature nodes joined by a liner thermal conductor.
Note that values are assumed to be fixed constants unless one of the following keys
are provided "expr='yes'" means that the value is calculated as a python expression.
"calc='yes'" - the value is to be calculated by the solver, and the value provided is just an initial guess.
```
<xml>
<import file="matdb.xml">

<node type="T">
   <name>Cold End</name>
   <num>0</num>
   <temp>273</temp>
   <gui_pos x="0", y="0", z="0">
   <note>Cold end of bar fixed at zero degC</note>
</node>

<node type="T">
   <name>Hot End</name>
   <num>1</num>
   <temp>373</temp>
   <gui_pos x="1", y="0", z="0">
   <note>Hot end of bar fixed at 100 degC</note>
</node>

<link type="TL">
  <name>steel bar</name>
  <num>0</num>
  <nodes>
     0
     1
  </nodes>
  <A expr="yes">0.01x0.05</A>
  <L>0.1</L>
  <k expr="yes">interp(matdb_k_steel,0.5*(node(0).temp+node(1).temp)</k>
  <GL expr="yes">k*A/L</GL>

</xml>

```

# Materials Database #
This is an example of a supplementary XML file used to store a database of material properties.  In this case only a single one dimensional (vector) array is defined, which is the thermal conductivity of mild steel.  **NOTE - do not use this, the numbers are made up because I do not have my data book handy**
```
<xml>
   <vector>
      <num>0</num>
      <name>k_steel</name>
      <values>
         173  0.20
         273  0.15
         373  0.13
         473  0.10
      </values>
   </vector>
</xml>
```