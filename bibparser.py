from pybtex.database.input import bibtex
import pybtex

pybtex.errors.set_strict_mode(False)

name = "sciencedirect"
pre_reject_path = "example/reject.bib"
pre_accept_path = "example/accept.bib"
new_path = "example/new.bib"
output_path = "example/out.bib"

# Load new_path into new_bib_data and actual_
parser = bibtex.Parser()
new_bib_data = parser.parse_file(new_path)
parserA = bibtex.Parser()
actual_bib_data = parserA.parse_file(new_path)

# Load already rejected entries
parser2 = bibtex.Parser()
pre_reject_data = parser2.parse_file(pre_reject_path)

# Load already accepted entries
parser3 = bibtex.Parser()
pre_accept_data = parser3.parse_file(pre_accept_path)

# List of ids to remove
ids_to_remove = []
# number of already rejeced and already accepted entries
num_reject = 0
num_accept = 0

# Compare entries in new_bib_data by title and year with the entries in pre_reject_data
# If title and year match, remove entry from actual_bib_data
for id in new_bib_data.entries:
	entry_new = new_bib_data.entries[id]
	for id2 in pre_reject_data.entries:
		entry_reject = pre_reject_data.entries[id2]
		if entry_new.fields['title'] == entry_reject.fields['title'] and entry_new.fields['year'] == entry_reject.fields['year']:
			# Ad id to list of ids to remove
			ids_to_remove.append(id)
			# Increment number of already rejected entries
			num_reject += 1

# Compare entries in new_bib_data by title and year with the entries in pre_accept_data
# If title and year match, remove entry from actual_bib_data
for id in new_bib_data.entries:
	entry_new = new_bib_data.entries[id]
	for id2 in pre_accept_data.entries:
		entry_accept = pre_accept_data.entries[id2]
		if entry_new.fields['title'] == entry_accept.fields['title'] and entry_new.fields['year'] == entry_accept.fields['year']:
			# Ad id to list of ids to remove
			ids_to_remove.append(id)
			# Increment number of already accepted entries
			num_accept += 1

# Remove entries from actual_bib_data
for id in ids_to_remove:
	actual_bib_data.entries.pop(id)

# Export actual_bib_data to output_path
with open(output_path, "w", encoding="utf-8") as fp:
	fp.write(actual_bib_data.to_string("bibtex").replace("\\\\", "\\"))

# Print number of already rejected and already accepted entries
print("Number of already rejected entries: " + str(num_reject))
print("Number of already accepted entries: " + str(num_accept))