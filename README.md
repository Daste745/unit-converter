[![asciicast](https://asciinema.org/a/VMG1OfLOPesv5FMxwnQcQTuKq.svg)](https://asciinema.org/a/VMG1OfLOPesv5FMxwnQcQTuKq)

# Features
- Fully customizable conversion ratios (through the conversions.json file).
- Fuzzy unit name matching (km -> kilometers, m^2 -> meters squared)

## Conversions structure
```
"unit_type": {
    "base": "unit_name",
    "conversions": {
        "unit_name": ratio,
        "unit_name": ratio
        ...
    },
    "abbreviations": {
        "abbrebiation": "full_name",
        "abbrebiation": "full_name"
        ...
    }
}
...
```
This program can only convert units from the same unit_type group. Make sure the base unit's conversion ratio is 1.
