from urllib.parse import quote
import argparse
from termcolor import colored





parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--string', help='String para codificar em Unicode')
group.add_argument('-w', '--file', help='Nome do arquivo para codificar em Unicode')
parser.add_argument('-n', '--num', type=int, default=1, help='Número de vezes para codificar em URL (padrão: 1)')
args = parser.parse_args()



if args.string:
    input_string = args.string
else:
    try:
        with open(args.file,'r') as file:
            input_string = file.read()
    except FileExistsError:
        print("Arquivo não encontrado!")
        exit()

url_encoded = input_string

for _ in range(args.num):
    url_encoded = quote(url_encoded)

print(colored(url_encoded, "green", attrs=["bold"]))
