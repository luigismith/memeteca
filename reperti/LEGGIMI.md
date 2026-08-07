# reperti/

Qui vanno i fotogrammi e gli screenshot veri, quelli che finiscono nel riquadro
in cima alla copertina.

1. Metti il file qui, con un nome che dica di che scheda è: `003_amici_miei.jpg`
2. In `agente/contenuti.py`, nella scheda, aggiungi:

```python
"reperto": {"tipo": "immagine", "bollo": "Il fotogramma",
  "file": "003_amici_miei.jpg",
  "fonte": "Fotogramma da «Amici miei» (1975), regia di Mario Monicelli. "
           "Citazione a fini di critica e discussione (art. 70 L. 633/1941)."},
```

3. `python agente/pubblica.py genera`

Se il file non c'è, il reperto viene omesso senza errori.

Regole in `docs/08_REPERTI.md`: breve, attribuito, solo in copertina, e mai più
di un terzo delle schede.
