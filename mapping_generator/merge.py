import subprocess
import shlex
import os
import shutil


rdf_filenames = os.listdir('./RDF-output')
input_parameter_str = ''
for index in range(len(rdf_filenames)-1):
    filename = './RDF-output/output' + str(index) + '.ttl'
    input_parameter_str += filename
    input_parameter_str += ' '
merge_command = './apache-jena-3.14.0/bin/riot --time --output=Turtle ' + input_parameter_str + '> merged.ttl'
print(merge_command)
os.system(merge_command)