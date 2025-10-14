# Replit: Deriv Signal-Only Bot


This Replit template provides a signal generator that connects to Deriv, fetches candles, computes EMA crossover + RSI, and prints CALL/PUT signals.


## Setup on Replit
1. Create a new Repl → choose **Import from GitHub** (or create a new Python Repl and paste files).
2. Add a `.env` file (Replit hides this automatically) with:
3. 3. Install packages (Replit usually auto-installs `requirements.txt`).
4. Press **Run**. Watch the console for signals.


## Configuration
Change environment variables in Replit `Secrets` or `.env`:
- `SYMBOL` (e.g. `frxEURUSD`)
- `GRANULARITY` (seconds: 60, 300, 900, ...)
- `EMA_SHORT`, `EMA_LONG`, `RSI_PERIOD`
- `CANDLE_COUNT` (how many historical candles to fetch)


## Notes
- This template **does not place trades** — it's signal-only. Use it to test and tune strategy before automating.
