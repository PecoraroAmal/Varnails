import os

def create_folder_structure():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    website_folder = os.path.join(base_folder)

    folders = [
        "Home",
        "Contattami",
        "Corsi-Effettuati",
        "Trattamenti",
        "Nails"
    ]

    for folder in folders:
        current_folder = os.path.join(website_folder, folder)
        if not os.path.exists(current_folder):
            os.makedirs(current_folder)

        # Aggiungi una sotto-cartella 'nomecartella-immagini' in ogni cartella
        image_folder = os.path.join(current_folder, f"{folder.lower()}-immagini")
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        if folder in ["Anime", "Videogiochi"]:
            create_file(current_folder, f"{folder.lower()}.html")
            create_file(current_folder, f"{folder.lower()}.css")
            create_file(current_folder, f"{folder.lower()}.js", ["barra.css", "barra.js"])

        elif folder not in ["BarraDiNavigazioneComuneTraHome"]:
            create_file(current_folder, f"{folder.lower()}.html")
            create_file(current_folder, f"{folder.lower()}.css")
            create_file(current_folder, f"{folder.lower()}.js")

    print("Struttura delle cartelle e dei file creata con successo!")

def create_file(folder, file_name, includes=None):
    file_path = os.path.join(folder, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            if includes:
                for include_file in includes:
                    file.write(f'/*include {include_file}*/\n')
            file.write('')

if __name__ == "__main__":
    create_folder_structure()
