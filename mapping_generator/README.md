# Mappings, SPARQL-GENERATE Scripts and Scripts for merging RDFs

This folder contains the mappings between MDO and main materials databases (Materials Project, AFLOW, NOMAD) and OPTIMADE, and scripts for merging multiple RDF tutrle files. The former is achieved by SPARQL-GENERATE, the latter is achieved by Apache-Jena-3.14.0.

# Run
Dependencies:
* SPARQL-GENERATE [https://github.com/sparql-generate/sparql-generate/releases/tag/2.0.0]
* Riot tool in Apache-Jena-3.14-0 [https://jena.apache.org/download/]
* Python libraries that imported in rdf-generator.py and merge.py

To map the data to RDF based on the mappings on single database:
```
python rdf-generator.py MP
```
or multiple databases:
```
python rdf-generator.py MP AFLOW NOMAD OPTIMADE
```

To merge multiple turtle files for single database:
```
python merge.py MP
```
or multiple databases:
```
python merge.py MP AFLOW NOMAD OPTIMADE
```
# Execute SPARQL queries on the data
Dependencies:
* Blazegraph [https://github.com/blazegraph/database/releases]

After download the jar file of Blazegraph, simplt run:
```
java -jar bigdata.jar
```
If everything went well, you can now perform URI lookups, For instance, access the URI shown after running above command in your browser such as:
```
http://192.168.0.8:9999/bigdata/
```
Then you can go to the UPDATE tab to upload the RDF data and QUERY to execute the SPARQL queries.
 


