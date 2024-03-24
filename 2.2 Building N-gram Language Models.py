def process_text(text):
    text = text.lower()
    return text

def tokenize(text):
    return text.split()

def padSequence(sequence_, ngram_, is_pad_left_ = True, is_pad_right_ = True,
                pad_left_token_ = "<s>", pad_right_token_ = "</s>"):
    assert isinstance(sequence_, list), "sequence_ is not list"
    if (is_pad_left_):
        i = 0
        while (i < ngram_ - 1):
            sequence_.insert(0, pad_left_token_)
            i += 1
    if (is_pad_right_):
        i = 0
        while (i < ngram_ - 1):
            sequence_.append(pad_right_token_)
            i += 1
    return sequence_

def generate_ngrams(words, n):
    # TODO: Implement the logic to generate n-grams from the list of words
    # words = padSequence(sequence_=words, ngram_=n)
    res = []
    res = [' '.join(words[i:i + n]) for i in range(len(words) - n + 1)]
    # print(res)
    return res

def count_ngrams(ngrams):
    ngram_counts = {}
    for ngram in ngrams:
        if ngram in ngram_counts:
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
    return ngram_counts

def is_near(lhs, rhs, delta=0.01):
    return(abs(lhs - rhs) < delta)

def calculate_ngram_probabilities(ngram_counts):
    total_ngrams = sum(ngram_counts.values())
    ngram_probabilities = {ngram: count / total_ngrams for ngram, count in ngram_counts.items()}
    # print(sum(ngram_probabilities.values()))
    assert is_near(sum(ngram_probabilities.values()),1), "error: sum(prob) != 1"
    return ngram_probabilities

def query_ngram_probability(ngram, ngram_probabilities):
    # print(ngram_probabilities)
    # print(ngram_probabilities.get(ngram,1))
    return ngram_probabilities.get(ngram, 0)

def main():
    text = "Your text here. It can be any string that you want to analyze."
    #text = """In the realm of natural language processing, understanding and manipulating text data is essential. The journey into this fascinating field begins with the basics of tokenization and normalization, laying the groundwork for more complex operations."""


    processed_text = process_text(text)
    words = tokenize(processed_text)

    # Generate n-grams
    unigrams = generate_ngrams(words, 1)
    bigrams = generate_ngrams(words, 2)
    trigrams = generate_ngrams(words, 3)

    # Count and calculate probabilities
    unigram_counts = count_ngrams(unigrams)
    unigram_probabilities = calculate_ngram_probabilities(unigram_counts)
    bigram_counts = count_ngrams(bigrams)
    bigram_probabilities = calculate_ngram_probabilities(bigram_counts)
    trigram_counts = count_ngrams(trigrams)
    trigram_probabilities = calculate_ngram_probabilities(trigram_counts)

    # Example query (Replace "your ngram here" with actual n-grams to test)
    print("Unigram Probability:", query_ngram_probability("your", unigram_probabilities))
    print("Bigram Probability:", query_ngram_probability("your ngram", bigram_probabilities))
    print("Trigram Probability:", query_ngram_probability("your ngram here", trigram_probabilities))
