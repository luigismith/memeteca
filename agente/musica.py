# -*- coding: utf-8 -*-
"""
MEMETECA — la traccia musicale dei Reel.

Un brano originale sintetizzato qui: nessun campione, nessun diritto altrui,
quindi nessun rights management che possa silenziare il video. Lo-fi minimale
e asciutto, come la grafica: cassa morbida, charleston, un basso che gira su
quattro accordi minori e un blip melodico raro.

    python musica.py [durata_secondi]   # genera ../assets/musica_reel.wav
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import pathlib
import sys
import wave

import numpy as np

SR = 44100
BPM = 92
QUI = pathlib.Path(__file__).parent


def _adsr(n, a=0.005, d=0.12, s=0.25, r=0.05):
    t = np.linspace(0, 1, n)
    env = np.where(t < a, t / a,
          np.where(t < a + d, 1 - (1 - s) * (t - a) / d, s))
    coda = int(r * n)
    if coda:
        env[-coda:] = env[-coda:] * np.linspace(1, 0, coda)
    return env


def kick(dur=0.28):
    n = int(SR * dur)
    t = np.arange(n) / SR
    freq = 105 * np.exp(-t * 22) + 44
    fase = 2 * np.pi * np.cumsum(freq) / SR
    return np.sin(fase) * np.exp(-t * 9) * 0.9


def hat(dur=0.05, ampiezza=0.16):
    n = int(SR * dur)
    rumore = np.random.default_rng(7).standard_normal(n)
    rumore = np.diff(rumore, prepend=0)          # filtro passa-alto grezzo
    return rumore / np.max(np.abs(rumore)) * np.exp(-np.arange(n) / (SR * 0.012)) * ampiezza


def nota(freq, dur, vol=0.3, timbro="basso"):
    n = int(SR * dur)
    t = np.arange(n) / SR
    if timbro == "basso":
        onda = np.sign(np.sin(2 * np.pi * freq * t)) * 0.35 + np.sin(2 * np.pi * freq * t) * 0.65
    else:
        onda = np.sin(2 * np.pi * freq * t) + 0.4 * np.sin(2 * np.pi * freq * 2 * t)
    return onda * _adsr(n) * vol


def genera(durata=28.0):
    battito = 60 / BPM                       # un quarto
    n_tot = int(SR * durata)
    out = np.zeros(n_tot)

    def metti(seg, t0):
        i = int(t0 * SR)
        j = min(i + len(seg), n_tot)
        if i < n_tot:
            out[i:j] += seg[: j - i]

    # giro in la minore: Am - F - C - G (fondamentali basse)
    giro = [110.0, 87.31, 65.41, 98.0]
    t = 0.0
    barra = 0
    while t < durata:
        fondo = giro[barra % 4]
        # cassa sull'1 e sul 3
        metti(kick(), t)
        metti(kick(), t + 2 * battito)
        # charleston in ottavi, con accento levare
        for k in range(8):
            metti(hat(ampiezza=0.2 if k % 2 else 0.12), t + k * battito / 2)
        # basso: fondamentale sull'1, quinta sul 3.5
        metti(nota(fondo, battito * 1.6, 0.34), t)
        metti(nota(fondo * 1.5, battito * 0.8, 0.22), t + 2.5 * battito)
        # blip melodico raro (ogni due battute, ottava alta)
        if barra % 2 == 1:
            metti(nota(fondo * 4, battito * 0.5, 0.10, "blip"), t + 3 * battito)
        t += 4 * battito
        barra += 1

    # respiro iniziale e coda in dissolvenza
    out[: int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))
    coda = int(1.2 * SR)
    out[-coda:] *= np.linspace(1, 0, coda)

    out = np.tanh(out * 1.1) * 0.85          # limiter morbido
    dati = (out * 32767).astype(np.int16)

    dest = QUI.parent / "assets" / "musica_reel.wav"
    with wave.open(str(dest), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(dati.tobytes())
    return dest


if __name__ == "__main__":
    d = float(sys.argv[1]) if len(sys.argv) > 1 else 28.0
    print(genera(d))
