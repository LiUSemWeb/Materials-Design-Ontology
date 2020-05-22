import subprocess
import shlex
import os
import shutil


data_src_dir = './MP-dataset'
data_dst_dir = './sparql-generate/documentset'
new_dst_file = os.path.join(data_dst_dir, 'intermediate.json')
filenames = os.listdir(data_src_dir)
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