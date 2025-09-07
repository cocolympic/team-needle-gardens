import encodings
import pkgutil

all_encodings = [name for _, name, _ in pkgutil.iter_modules(encodings.__path__)]
print(all_encodings[:20]) 