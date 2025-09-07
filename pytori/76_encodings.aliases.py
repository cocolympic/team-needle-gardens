import encodings.aliases

aliases = encodings.aliases.aliases

for k, v in list(aliases.items())[:20]:
    print(f"{k} -> {v}")