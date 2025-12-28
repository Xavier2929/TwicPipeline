import os

twic_folder = os.getenv("TWIC_FILES_FOLDER")
output_dir = os.getenv("COMBINED_TWIC_FOLDER")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "combined.pgn")

with open(output_file, "a", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(twic_folder)):
        if filename.lower().endswith(".pgn"):
            print("Agregando:", filename)
            file_path = os.path.join(twic_folder, filename)

            with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                content = infile.read().strip()
                if content:  # evita agregar bloques vacíos
                    outfile.write("\n\n")  # separador PGN
                    outfile.write(content)

print("PGNS combined (append):", output_file)
