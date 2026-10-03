import pandas as pd

print("="*60)
print("FASE 1: PULIZIA DATI")
print("="*60)

# Carica il dataset
df = pd.read_csv("../data/netflix_titles.csv")
print(f"\nDataset originale: {df.shape[0]} righe, {df.shape[1]} colonne")
print(f"Valori mancanti per colonna:\n{df.isna().sum()}")

# Converte la data in formato data vera e propria
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")

# Riempie i valori mancanti con un'etichetta invece di lasciarli vuoti
df["director"] = df["director"].fillna("Non specificato")
df["cast"] = df["cast"].fillna("Non specificato")
df["country"] = df["country"].fillna("Non specificato")
df["rating"] = df["rating"].fillna("Non specificato")

# Separa la durata in un numero e un'unità di misura (min per film, stagioni per serie TV)
df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["duration_unit"] = df["duration"].apply(
    lambda x: "min" if isinstance(x, str) and "min" in x else "season"
)

# Elimina le pochissime righe dove mancano ancora data o durata
df_clean = df.dropna(subset=["date_added", "duration_num"])
print(f"\nRighe prima della pulizia finale: {len(df)}")
print(f"Righe dopo la pulizia finale: {len(df_clean)}")

# Salva il dataset pulito, pronto per i grafici
df_clean.to_csv("../outputs/netflix_clean.csv", index=False)
print("\nDataset pulito salvato in outputs/netflix_clean.csv")
