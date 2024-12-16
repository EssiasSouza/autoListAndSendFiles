import os
import lib_applogs2_1_0 as log
import json
import shutil

# Ler arquivo de texto com os códigos serem enviados.
# Transformar tudo em código de 5 digito
# Definir razão de uso
# Varrer os caminhos de pastas disponíveis para envio.
# Gerar lista de caminhos.
# Copiar arquivos para cada pasta listada.
# Gerar logs

log.log_print('info', 'Iniciando aplicação.')

with open('settings.json', 'r') as file:
    settings = json.load(file)

for item in settings:

    if 'PARAMETERS' in item:
        parameter = item['PARAMETERS']
        if 'root_folder' in parameter:
            search_dir = parameter['root_folder']
        if 'filesSource' in parameter:
            filesSource = parameter['filesSource']
        if 'SubFolders' in parameter:
            SubFolders = parameter['SubFolders']
        if 'Destinations' in parameter:
            Destinations = parameter['Destinations']


input_file = Destinations
output_file = 'destinos.txt'

if not os.path.exists(search_dir):
    print(f"O diretório {search_dir} não existe.")
    exit()

with open(input_file, 'r', encoding='utf-8') as f:
    draw_patterns = [line.strip().lower() for line in f]
search_patterns = []
for t in draw_patterns:
    if len(t) < 4:
        listItem = f'00{t}'
    elif len(t) < 5:
        listItem = f'0{t}'
    else:
        listItem = t
    search_patterns.append(listItem)

# Verificar se lista de padrões não está vazia
if not search_patterns:
    log.log_print("A lista de padrões de busca está vazia.")
    exit()

broom_dir = []
dir_list_found = []

for folder in os.listdir(search_dir):
    folder_path = os.path.join(search_dir, folder)
    broom_dir.append(folder)

def find_matching_paths(broom_dir, search_patterns):
    results_found = []
    results_not_found = []
    for pattern in search_patterns:
        found = False
        for path in broom_dir:
            if str(pattern) in path:
                results_found.append(path)
                found = True
                break
        if not found:
            results_not_found.append(f"not found {pattern}")
    return results_found, results_not_found

def concat_path(search_dir, resultsFound):
    fullPaths = []
    for i in resultsFound:
        concat = f'{search_dir}\{i}'
        fullPaths.append(concat)
    return fullPaths


resultsFound, resultsNotFound = find_matching_paths(broom_dir, search_patterns)
results = concat_path(search_dir, resultsFound)
number_of_results = len(resultsFound)
log.log_print('info', f'Found {number_of_results} folders')
log.log_print('info', "--- LIST OF FOLDERS ---")
for path_dir in results:
    log.log_print('info', f'{path_dir}')

for fails in resultsNotFound:
    log.log_print('warning', fails)


# Copying files from folder aqruivos.

def copy_all_files(source_directory, destination_directory, SubFolders):
    if len(SubFolders) >= 1:
        destination_directory = f"{destination_directory}\\{SubFolders}"
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    for item in os.listdir(source_directory):
        source_path = os.path.join(source_directory, item)
        destination_path = os.path.join(destination_directory, item)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            log.log_print('info', f"Copy from: {source_path} to: {destination_path}")

log.log_print('info', 'Starting file copy process')
log.log_print('info', 'The files below will be copied')
source_directory = filesSource


for path_dir in results:
    destination_directory = path_dir
    source_directory = filesSource
    copy_all_files(source_directory, destination_directory, SubFolders)

log.log_print('info', 'Process finished!')