import re

# Must match:
# "John Cena"
# "Anya Taylor-Joy"
# "D'Angelo"
# Must NOT match: empty string, lowercase names, numbers, multiple spaces
name_regex = re.compile(
    r"[A-Z][a-z]*(?:[\'-][A-Z][a-z]+| [A-Z][a-z]+)*"
)

# Must match:
# "5555555555"
# "555-555-5555"
# "(555) 555-5555"
phone_regex = re.compile(
    r"(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})"
)

# Must match:
# "johncena@wwe.com"
# "john.cena@wwe.com"
# "john.cena123@wwe.com"
# Must NOT start with a number
# Must NOT contain $ or missing domain
email_regex = re.compile(
    r"[a-zA-Z][a-zA-Z0-9]*(?:\.[a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]+"
)
