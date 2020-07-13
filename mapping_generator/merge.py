import os
import sys

database_folder = {'MP':'./MP-dataset', 'AFLOW':'./AFLOW-dataset', 'NOMAD':'./NOMAD-dataset', 'OPTIMADE':'./OPTIMADE-dataset'}

def main(argv):
	if len(argv) < 2:
		print('Please provide at least one database.')
		sys.exit(1)
	
	for database in argv[1:]:
		input_parameter_str = ''
		data_src_dir = database_folder[database]
		filenames = os.listdir(data_src_dir)
		print(filenames)
		i = 0
		for filename in filenames:
			if os.path.splitext(filename)[0][0:6] == 'output' and os.path.splitext(filename)[1] == '.ttl':
				file_path = database_folder[database] +'/'+ filename
				input_parameter_str += file_path
				input_parameter_str += ' '
		merge_command = './apache-jena-3.14.0/bin/riot --time --output=Turtle ' + input_parameter_str + '>' + database_folder[database] + '/merged.ttl'
		print(merge_command)
		os.system(merge_command)


if __name__ == "__main__":
  main(sys.argv)


