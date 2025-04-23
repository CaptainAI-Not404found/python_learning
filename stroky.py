word = "FootBALL, BaskeTball, skATe"
#print(word.count("i"))
#print(word.isupper())
#print(word.find("p"))
hobby = word.split(", ")

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ".join(hobby)
print(result)