import yara

rule_source = r"""
rule SilentBanker {
    strings:
        $a = "Banker" nocase
    condition:
        $a
}
"""

rules = yara.compile(source=rule_source)

data = b"This is a SilentBanker trojan sample"

matches = rules.match(data=data)
print(matches)