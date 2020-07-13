import sys
import os
import shutil
import json


database_folder = {'MP':'./MP-dataset', 'AFLOW':'./AFLOW-dataset', 'NOMAD':'./NOMAD-dataset', 'OPTIMADE':'./OPTIMADE-dataset'}
database_mapping = {'MP':'mp-mappings.rqg', 'AFLOW':'aflow-mappings.rqg', 'NOMAD':'nomad-mappings.rqg', 'OPTIMADE':'optimade-mappings.rqg'}

data_dst_dir = './sparql-generate/documentset'
new_dst_file = os.path.join(data_dst_dir, 'intermediate.json')

# To modify the configuration for SPARQL-Generate
def construct_conf(database):
	data={}
	data['documentset'] = []
	data['documentset'].append({
    'mediatype': 'application/json',
    'path': 'documentset/intermediate.json',
    'uri': 'http://example.com/intermediate.json'})
	data['query'] = database_mapping[database]
	data['namedqueries'] = []
	data['graph'] = 'dataset/default.ttl'
	data['namedgraphs'] = []
	data['loglevel'] = 5
	with open('./sparql-generate/sparql-generate-conf.json', 'w') as outfile:
		json.dump(data, outfile)


def main(argv):
	if len(argv) < 2:
		print('Please provide at least one database.')
		sys.exit(1)
	
	for database in argv[1:]:
		data_src_dir = database_folder[database]
		filenames = os.listdir(data_src_dir)
		print(filenames)
		construct_conf(database)
		i = 0
		for filename in filenames:
			if os.path.splitext(filename)[1] == '.json':
				src_file = os.path.join(data_src_dir, filename)
				shutil.copy(src_file, data_dst_dir)
				dst_file = os.path.join(data_dst_dir, filename)
				os.rename(dst_file, new_dst_file)
				# execute sparqlgenerate command
				output_file = 'output' + str(i) + '.ttl'
				log_file = 'output' + str(i) + '.log'
				sqlgenerate_command = 'java -jar ./sparql-generate/sparql-generate-2.0.jar -d ./sparql-generate -o '+ database_folder[database] + '/'+ output_file + ' -f'+ database_folder[database] +'/' + log_file
				os.system(sqlgenerate_command)
				os.remove(new_dst_file)
				i += 1

if __name__ == "__main__":
  main(sys.argv)


 
