from better_profanity import profanity
sentences = []
# Add Your words Here
bad_words = ["nigga","negro", "uncle tom", "Jim Crow", "squaw"]

with open('tweets.txt', 'r') as f:
    for line in f.readlines():
        if line:
            sentences.append(line)

profanity.load_censor_words(bad_words)
with open("output.txt", "w") as f:
    for sentence in sentences:
        count = 0
        if profanity.contains_profanity(sentence):
            words = sentence.split()
            censored = profanity.censor(sentence,"*")
            count = censored.count('*') // 4
            output = "{} - {}".format(censored.strip(), count)
            f.write(output)
            f.write("\n")
        else:
            censored = profanity.censor(sentence,"*")
            output = "{} - {}".format(censored.strip(), count)
            f.write(output)
            f.write("\n")

    
