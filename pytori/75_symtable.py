import symtable

code = "a = 1\nb = 2\nc = a + b"

table = symtable.symtable(code, "<string>", "exec")

print(table.get_identifiers())