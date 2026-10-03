# Netflix Content Analysis

Analisi esplorativa del catalogo Netflix: pulizia dati con pandas e visualizzazioni con matplotlib.

## Dataset
Catalogo titoli Netflix (film e serie TV), 8.807 titoli con informazioni su regista, cast, paese, data di aggiunta, rating, durata e generi.

## Struttura del progetto
- `data/` — dataset originale
- `scripts/01_data_cleaning.py` — pulizia dati: gestione valori mancanti, conversione date, separazione durata (minuti per film, stagioni per serie TV)
- `scripts/02_visualizations.py` — generazione dei grafici
- `outputs/` — dataset pulito e grafici generati

## Pulizia dati
- Conversione `date_added` in formato data
- Valori mancanti in director, cast, country, rating sostituiti con "Non specificato" invece di eliminare righe
- Colonna `duration` separata in valore numerico + unità di misura (minuti per i film, stagioni per le serie TV)
- Rimozione delle righe (13 su 8.807) senza data di aggiunta o durata valida

## Visualizzazioni
1. **Crescita contenuti nel tempo** — film vs serie TV aggiunti per anno, mostra la forte crescita del catalogo tra il 2016 e il 2019
2. **Top 10 paesi produttori** — Stati Uniti nettamente al primo posto, seguiti da India e Regno Unito
3. **Top 10 generi** — International Movies e Dramas sono i generi più rappresentati

## Strumenti utilizzati
Python, pandas, matplotlib
