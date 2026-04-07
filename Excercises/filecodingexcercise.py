countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

print(list(zip(countries, filenames)))
for country, filename in zip(countries, filenames):
    file_write = open(filename, "w")
    file_write.write(country)
    file_write.close
    print(f"{country} {filename} Done")