import pathlib

PATH = pathlib.Path(
    "C:\\Users\\Joanete\\Documents\\datasets\\kdd_cup_1999\\kddcup.data"
)

print(PATH.exists())

try:
    with open(PATH, "r") as f:
        f.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")


print("LIDO COM SUCESSO!")
