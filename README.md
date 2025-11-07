# Cryptanalysis - Vigenere, DLP & RSA

Tools, datasets, and experiment notes for attacking Vigenere substitutions with a hill-climbing heuristic, experimenting with discrete logarithm computations (Baby-Step Giant-Step), and revisiting RSA attacks (classic + Wiener). The repository keeps every resource we used for coursework-sized cryptanalytic experiments so you can reproduce the results or build on top of them.

---

## Features
- **Automated Vigenere breaker** - `cryptanalyse.py` leverages n-gram statistics (2 <= n <= 5) and a hill-climbing search to recover the substitution alphabet for English and French corpora.
- **Curated language models** - `DATA/Dict_ngramm` stores mono- through pentagram frequency tables along with helper scripts to rebuild them from corpora.
- **Reference labs** - `src/vigenere`, `src/DLP-BSGS`, and `src/RSA` contain the original teaching material, test vectors, and PDFs that motivated the project.
- **Reproducible experiments** - the `scripts/` directory holds utilities for generating LaTeX tables, stress-testing fitness functions, and producing publication-ready figures.

---

## Repository Layout
```
Cryptanalysis_Vigenere_DLP_RSA/
|-- cryptanalyse.py          # Main CLI for hill-climbing Vigenere decryption
|-- src/                     # Core implementations (Vigenere, DLP/BSGS, RSA)
|-- scripts/                 # Data-prep and analysis helpers
|-- DATA/                    # N-gram statistics, plots, latex-ready tables
|-- text/                    # Sample cipher/plain texts in EN and FR
|-- requirements.txt         # Python dependencies
|-- Rapport.pdf              # Project report (FR)
`-- LICENSE                  # Project license
```

---

## Requirements & Installation
1. **Python**: 3.9+ is recommended (NumPy + Matplotlib support).
2. **Install dependencies**:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # or source .venv/bin/activate on Unix
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Usage
Run the hill-climbing cryptanalyst from the repository root:

```powershell
python cryptanalyse.py <NGRAM> <PATH_TO_CIPHERTEXT> <LANG>
```

**Arguments**
- `NGRAM`: integer in `[2,5]`. Higher N captures more context but increases search time.
- `PATH_TO_CIPHERTEXT`: text file to analyze. The helper routines automatically strip non-alphabet characters and uppercase the input.
- `LANG`: `EN` (English) or `FR` (French). This toggles the language model used in scoring.

**Example**
```powershell
python cryptanalyse.py 4 text/EN/txtCLAIRE_1500_EN.txt EN
```

**Output**
- Console: recovered substitution key, fitness score, Pearson correlation, and runtime.
- File: `text/textDECHIFRE.txt` is overwritten with a side-by-side view of the ciphertext, decrypted text, and the discovered key.

---

## Data & Supporting Material
- `DATA/Dict_ngramm/stats_EN|FR`: precomputed n-gram distributions used during scoring (`cipher.ngram`).
- `DATA/stats_ngramm` and `DATA/courbe`: raw statistics plus PNG curves for quick inspection.
- `DATA/DATA4LATEX`: CSV exports ready to drop into LaTeX tables when reporting optimal iteration counts.
- `text/EN` and `text/FR`: sample plaintexts/ciphertexts used during testing.

All large PDFs (e.g., `Rapport.pdf`, lab handouts inside `src/*`) remain in-place for reference; feel free to move them under `docs/` if you prefer a lighter working tree.

---

## Helper Scripts
| Script | Purpose |
| --- | --- |
| `scripts/creer_stats.py` | Builds frequency dictionaries (`ngrams.txt`) from clean corpora. |
| `scripts/creerTABLE.py` | Aggregates benchmark runs into CSV summaries. |
| `scripts/stats_fit_1_2.py` | Compares two fitness scoring strategies on shared datasets. |
| `scripts/personstats.py` | Generates personalized statistics based on provided text corpora. |
| `scripts/CSV2LATEX.py` | Converts CSV exports into LaTeX tables for reports/publications. |

Each script contains inline documentation describing its CLI parameters; run them with `python scripts/<name>.py --help` to see the options.

---

## Extra Modules
- `src/vigenere`: legacy implementation, regression tests, and course handouts; useful for comparing earlier iterations with the streamlined `cryptanalyse.py`.
- `src/DLP-BSGS`: Baby-Step Giant-Step discrete logarithm utilities plus maths refresher PDFs.
- `src/RSA`: RSA toolkit (key generation, Wiener-style attack demos) accompanied by exercises and solutions.

These folders are self-contained; activate your virtual environment and run their respective `test-*.py` files to reproduce the exercises.

---

## Contributing
Improvements are welcome -- whether that is extending the hill-climbing heuristics, porting the tooling to another language, or trimming the dataset footprint. Please open an issue or pull request describing the change along with any reproducibility notes (test inputs, parameter choices, etc.).

---

## License
This project is distributed under the terms of the license stored in `LICENSE`. Review it before reusing the code or the datasets.




