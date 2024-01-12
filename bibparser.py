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

# Compare entries in new_bib_data by title, author and year with the entries in pre_reject_data
# If all three are equal, the entry is added to ids_to_remove
# if two them are equal the entry is added to the corresponding list
for id in new_bib_data.entries:
    entry = new_bib_data.entries[id]
    # print id
    print(id)
    for id2 in pre_reject_data.entries:
        entry2 = pre_reject_data.entries[id2]
        # Sort the Person entries in entry.persons["author"] by result of str(Person)
        entry.persons["author"].sort(key=lambda x: str(x))
        # same for entry2
        entry2.persons["author"].sort(key=lambda x: str(x))
        # Check if title, author and year exist in both entries
        if ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"])
             or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]))
                and "author" in entry.persons and "author" in entry2.persons and "year" in entry.fields and "year" in entry2.fields
                and entry.persons["author"] == entry2.persons["author"]
                and entry.fields["year"] == entry2.fields["year"]):
                ids_to_remove.append(entry.key)
                num_reject += 1
                break;
        # Check if title and year exist in both entries
        elif ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"])
                or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]))
              and "year" in entry.fields
              and "year" in entry2.fields and entry.fields["title"] == entry2.fields["title"]
              and entry.fields["year"] == entry2.fields["year"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove, if
            # repeat asking till the user say y or n
            print("#######################################################")
            print("#######################################################")
            print("Title and year match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break;
        # Check if author and year exist in both entries
        elif ("author" in entry.persons and "author" in entry2.persons and "year" in entry.fields
              and "year" in entry2.fields and entry.persons["author"] == entry2.persons["author"]
              and entry.fields["year"] == entry2.fields["year"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Author and year match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break;
        # Check if title and author exist in both entries
        elif ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"]
                or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"])))
              and "author" in entry.persons and "author" in entry2.persons
              and entry.persons["author"] == entry2.persons["author"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Title and author match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break
        # Check if only title exists and is equal in both entries
        elif ("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Title match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break
        # Check if only booktitle exists and is equal in both entries
        elif ("booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Booktitle match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break

# Compare entries in new_bib_data by title, author and year with the entries in pre_accept_data
# If all three are equal, the entry is added to ids_to_remove
# if two them are equal the entry is added to the corresponding list
for id in new_bib_data.entries:
    entry = new_bib_data.entries[id]
    for id2 in pre_accept_data.entries:
        entry2 = pre_accept_data.entries[id2]
        # Sort the Person entries in entry.persons["author"] by result of str(Person)
        entry.persons["author"].sort(key=lambda x: str(x))
        # same for entry2
        entry2.persons["author"].sort(key=lambda x: str(x))
        # Check if title, author and year exist in both entries
        if ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"])
             or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]))
                and "author" in entry.persons and "author" in entry2.persons and "year" in entry.fields and "year" in entry2.fields
                and entry.persons["author"] == entry2.persons["author"]
                and entry.fields["year"] == entry2.fields["year"]):
                ids_to_remove.append(entry.key)
                num_accept += 1
                break;
        # Check if title and year exist in both entries
        elif ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"])
                or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]))
              and "year" in entry.fields
              and "year" in entry2.fields and entry.fields["title"] == entry2.fields["title"]
              and entry.fields["year"] == entry2.fields["year"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Title and year match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
                break
        # Check if title and author exist in both entries
        # Check if author and year exist in both entries
        elif ("author" in entry.persons and "author" in entry2.persons and "year" in entry.fields
              and "year" in entry2.fields and entry.persons["author"] == entry2.persons["author"]
              and entry.fields["year"] == entry2.fields["year"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Author and year match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_accept += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
                break
        # Check if title and author exist in both entries
        elif ((("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"]
                or ("title" not in entry.fields and "booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"])))
              and "author" in entry.persons and "author" in entry2.persons
              and entry.persons["author"] == entry2.persons["author"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Title and author match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                print(answer)
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_accept += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break
        # Check if only title exists and is equal in both entries
        elif ("title" in entry.fields and "title" in entry2.fields and entry.fields["title"] == entry2.fields["title"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Title match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_accept += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break
        # Check if only booktitle exists and is equal in both entries
        elif ("booktitle" in entry.fields and "booktitle" in entry2.fields and entry.fields["booktitle"] == entry2.fields["booktitle"]):
            # Ask user if the entries are the same and if yes, add the entry to ids_to_remove
            print("#######################################################")
            print("#######################################################")
            print("Booktitle match:")
            print(entry.to_string("bibtex"))
            print(entry2.to_string("bibtex"))
            print("Is this the same entry? (y/n)")
            while True:
                answer = input()
                if answer == "y":
                    ids_to_remove.append(entry.key)
                    num_reject += 1
                    break
                elif answer == "n":
                    break
                else:
                    print("Please enter y or n")
            break


# Remove all entries in ids_to_remove from actual_bib_data
for id in ids_to_remove:
    actual_bib_data.entries.pop(id)

# Print number of already rejected and already accepted entries
print("Number of already rejected entries: " + str(num_reject))
print("Number of already accepted entries: " + str(num_accept))

# Write new_bib_data to output_path
with open(output_path, "w", encoding="utf-8") as fp:
    fp.write(actual_bib_data.to_string("bibtex").replace("\\\\", "\\"))
