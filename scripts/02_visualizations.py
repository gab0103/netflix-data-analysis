import pandas as pd
import matplotlib.pyplot as plt

print("="*60)
print("FASE 2: VISUALIZZAZIONI")
print("="*60)

# Carica il dataset già pulito
df_clean = pd.read_csv("../outputs/netflix_clean.csv")
df_clean["date_added"] = pd.to_datetime(df_clean["date_added"])

# --- GRAFICO 1: Crescita contenuti nel tempo ---
df_clean["anno_aggiunta"] = df_clean["date_added"].dt.year
conteggio = df_clean.groupby(["anno_aggiunta", "type"]).size().unstack()

conteggio.plot(kind="line", marker="o", figsize=(10, 6))
plt.title("Crescita contenuti Netflix nel tempo")
plt.xlabel("Anno di aggiunta")
plt.ylabel("Numero di titoli")
plt.legend(title="Tipo")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("../outputs/01_grafico_crescita_netflix.png")
plt.show()

# --- GRAFICO 2: Top 10 paesi produttori ---
paesi = df_clean[df_clean["country"] != "Non specificato"]["country"]
paesi_esplosi = paesi.str.split(", ").explode().str.strip()
top_paesi = paesi_esplosi.value_counts().head(10)

plt.figure(figsize=(10, 6))
top_paesi.plot(kind="barh")
plt.title("Top 10 paesi produttori di contenuti Netflix")
plt.xlabel("Numero di titoli")
plt.ylabel("Paese")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../outputs/02_grafico_top_paesi.png")
plt.show()

# --- GRAFICO 3: Top 10 generi ---
generi_esplosi = df_clean["listed_in"].str.split(", ").explode().str.strip()
top_generi = generi_esplosi.value_counts().head(10)

plt.figure(figsize=(10, 6))
top_generi.plot(kind="barh", color="darkorange")
plt.title("Top 10 generi più presenti su Netflix")
plt.xlabel("Numero di titoli")
plt.ylabel("Genere")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../outputs/03_grafico_top_generi.png")
plt.show()

print("\nTutti i grafici salvati nella cartella outputs/")
