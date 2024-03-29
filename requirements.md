# Requirements of MDO

## Use Cases

* [UC1] MDO will be used for representing knowledge in basic materials sciencesuch as solid-state physics and condensed matter theory.
* [UC2] MDO will be used for representing materials calculation and standardizing the publication of the materials calculation data.
* [UC3] MDO will be used as a standard to improve the interoperability among heterogeneous databases in the materials design domain.
* [UC4] MDO will be mapped to OPTIMADE’s schema to improve OPTIMADE’s search functionality.

## Competency Questions

* [CQ1] What are the calculated properties and their values produced by a materials calculation?
* [CQ2] What are the input and output structures of a materials calculation?
* [CQ3] What is the space group type of a structure?
* [CQ4] What is the lattice type of a structure?
* [CQ5] What is the chemical formula of a structure?
* [CQ6] For a series of materials calculations, what are the compositions of materials with a specific range of calculated property (e.g., band gap)?
* [CQ7] For a specific material and a given range of a calculated property (e.g., band gap), what is the lattice type of the structure?
* [CQ8] For a specific material and an expected lattice type of output structure, what are the values of calculated properties of the calculations?
* [CQ9] What is the computational method used in a materials calculation?
* [CQ10] What is the value for a specific parameter (e.g., cutoff energy) of the method used for the calculation?
* [CQ11] Which software produced the result of a calculation?
* [CQ12] Who are the authors of the calculation?
* [CQ13] When was the calculation data published to the database?


## Additional Restrictions

* [AR1] A materials property can relate to a structure.
* [AR2] A materials calculation has exactly one corresponding computational method.
* [AR3] A structure corresponds to one specific space group.
* [AR4] A calculation is performed by some software programs or codes.
* [AR5] A structure is a part of some materials.
* [AR6] A structure and a property can be published by references which could be databases or publications.
* [AR7] A calculation can take some structures as input.
* [AR8] A calculation can take some properties as input.
