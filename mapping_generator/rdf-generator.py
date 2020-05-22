import subprocess
import shlex
import os
import shutil
import time
t = 2


data_src_dir = './MP-dataset'
data_dst_dir = './sparql-generate/documentset'
new_dst_file = os.path.join(data_dst_dir, 'intermediate.json')
filenames = os.listdir(data_src_dir)
command1 = '/Users/huali50/Downloads/apache-jena-3.14.0/bin/riot --time --output=Turtle ./test1.ttl ./test2.ttl > output5.ttl'
sparqlgenerate_command = 'java -jar sparql-generate-2.0.jar -d ./MP -o test2.out -f test2.log'
#args = shlex.split(command1)
#subprocess.Popen(args)
#os.popen(command1)
#os.system(command1)
print(filenames)
num_file = len(filenames)
for i, filename in enumerate(filenames):
    src_file = os.path.join(data_src_dir, filename)
    shutil.copy(src_file, data_dst_dir)
    dst_file = os.path.join(data_dst_dir, filename)
    os.rename(dst_file, new_dst_file)
    # execute sparqlgenerate command
    output_file = 'output' + str(i) + '.ttl'
    log_file = 'output' + str(i) + '.log'
    sqlgenerate_command = 'java -jar sparql-generate-2.0.jar -d ./sparql-generate -o ./RDF-output/' + output_file + ' -f ./log/' + log_file
    os.system(sqlgenerate_command)
    os.remove(new_dst_file)