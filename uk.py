united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# print(united_kingdom)

# Change the capital of Wales to Cardiff
united_kingdom[1]["capital"]= "Cardiff"
# print(united_kingdom)

# Create a Northern Ireland entry and add it to the existing dictionary list
NI = {
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast",
  }

united_kingdom.append(NI)
# print()
# print()

# print(united_kingdom)
# country = 0

poptotal = 0

for country in united_kingdom:
    print(country["name"])
    poptotal = (country["population"]) + poptotal
    
print(f"Total Population is {poptotal}")