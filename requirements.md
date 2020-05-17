# Requirements of MDO

## Use Cases

* [UC1] MDO will be used for representing knowledge in basic materials science such as solid-state physics and condensed matter theory, especially for representing materials calculations.
* [UC2] MDO will be used as a standard to improve the interoperability among heterogeneous databases in the materials design domain.
* [UC3] MDO will be adapted to (OPTIMADE) to improve the ability of searching.
* [UC4] MDO will be used for representing materials calculation and standardizing the publication of the materials calculation data.

## Competency Questions

* [CQ1] For a given piece of materials data representing a calculation, which software produces the result?
* [CQ2] What is the computational method used in a materials calculation?
* [CQ3] What are the computable properties and the values of them set up for a material calculation?
* [CQ4] What are the input and output structures of a materials calculation?
* [CQ5] What are the point group and space group of the structure?
* [CQ6] What is the point group type of a space group?
* [CQ7] What is the primary repeated lattice type of a structure?
* [CQ8] What is the WHAT FORMULA????? formula of a structure?
* [CQ9] For a specific material and a type of calculation, which calculation over multiple materials databases gives the highest value of a property (e.g., band gap)?
* [CQ10] For a specific material, a type of calculation, and a given range of an output physical property’s value (e.g., band gap), what’s the difference of the computable properties over different calculations?
* [CQ11] For a specific material and a given range of a physical property’s (e.g., band gap), what is the type of the lattice?
* [CQ12] For a specific material and an expected type of output structure, what are the values of computable properties of the calculations?
* [CQ13] Who are the authors of the calculation/data?
* [CQ14] Which software or code does the calculation run with?

* [CQ15] When is the calculation data published to the database?

## Additional Restrictions

* [AR1] A material calculation has exactly one corresponding computational method.
* [AR2] A material calculation could have some computable properties set up during the calculation.
* [AR3] A material calculation has exactly one corresponding input structure and one output structure.
* [AR4] A structure corresponds to one space group type and one point group type.
* [AR5] A space group corresponds to one point group type.
* [AR6] A specific structure has one corresponding lattice type.
* [AR7] A Structure has a specific composition chemical elements.
* [AR8] A piece of data is corresponding to a specific database and software.
