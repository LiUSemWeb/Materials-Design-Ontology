### SPARQL Query examples to answer Competency Questions

[SPARQL Documentation](https://www.w3.org/TR/rdf-sparql-query/).

CQ1:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?calculation ?Property ?value WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputCalculatedProperty ?Property;
   	       core:hasOutputStructure ?OutputStructure.
  ?Property core:hasPropertyValue ?value.
} 
```

CQ2:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?calculation ?input_structure ?output_structure WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasInputStructure ?input_structure;
   	       core:hasOutputStructure ?output_structure.
} 
```

CQ3:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?calculation ?output_structure ?symbol WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputStructure ?output_structure.
  ?output_structure rdf:type core:Structure;
                    structure:hasSpaceGroup ?spacegroup.
  ?spacegroup rdf:type structure:SpaceGroup;
           structure:hasSpaceGroupSymbol ?symbol.
} 

```

CQ4:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?calculation ?output_structure ?type WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputStructure ?output_structure.
  ?output_structure rdf:type core:Structure;
                    structure:hasLattice ?lattice.
  ?lattice rdf:type structure:Lattice;
           structure:hasLatticeType ?type.
} 

```

CQ5:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?calculation ?OutputStructure ?descriptiveformula WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputStructure ?OutputStructure.
  ?OutputStructure structure:hasComposition ?Composition.
  ?Composition structure:hasDescriptiveFormula 
               ?descriptiveformula.
} 
```

CQ6:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?descriptiveformula ?value WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputCalculatedProperty ?Property;
   	       core:hasOutputStructure ?OutputStructure.
  ?Property core:hasPropertyValue ?value;
   	    core:hasPropertyName ?name.
  ?OutputStructure structure:hasComposition ?Composition.
  ?Composition structure:hasDescriptiveFormula 
               ?descriptiveformula.
  FILTER (?value>5 && ?name="band_gap")
} 
```

CQ7:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?OutputStructure ?value ?type WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputCalculatedProperty ?Property;
   	       core:hasOutputStructure ?OutputStructure.
  ?Property core:hasPropertyValue ?value;
   	    core:hasPropertyName ?name.
  ?OutputStructure structure:hasLattice ?lattice.
  ?lattice structure:hasLatticeType 
               ?type.
  FILTER (?value>5 && ?name="band_gap")
} 
```

CQ8:
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX core: <https://w3id.org/mdo/core/>
PREFIX structure: <https://w3id.org/mdo/structure/>
PREFIX calculation: <https://w3id.org/mdo/calculation/>

SELECT ?OutputStructure ?value ?type WHERE {
  ?calculation rdf:type core:Calculation;
   	       core:hasOutputCalculatedProperty ?Property;
   	       core:hasOutputStructure ?OutputStructure.
  ?Property core:hasPropertyValue ?value;
   	    core:hasPropertyName ?name.
  ?OutputStructure structure:hasLattice ?lattice.
  ?lattice structure:hasLatticeType 
               ?type.
  FILTER (?name="band_gap" && ?type="cubic")
} 
```