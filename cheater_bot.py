from scipy import stats

def calculate_fair_probability(results):
    #Results are given as: ["Heads", "Tails"]
    heads_count = 0
    for i in results:
        if i == "Heads":
            heads_count += 1

    #What was the probabiltity that the results were true, given that the blob was either fair or a cheater.
    probability_given_fair = stats.binom.pmf(heads_count, len(results), 0.5)
    probability_given_cheater = stats.binom.pmf(heads_count, len(results), 0.75)

    #Given that these results happened, look at the ratio between them, as each one is equally as likely
    #We can compare them to work out the probability it is either fair or a blob.

    blob_fair_probability = probability_given_fair / (probability_given_fair + probability_given_cheater)
    return blob_fair_probability

def evaluate_flip_gain(results):
    blob_fair1 = calculate_fair_probability(results)
    print("Probability of it being fair before,", blob_fair1)
    #If flip gain is more than flip gain after 1 extra flip then the function should commit to a blob.
    #New nformation has to justify spending an extra token.

    if blob_fair1 > 0.5:
        current_flip_gain = 15*blob_fair1 - 30*(1-blob_fair1)
        blob_fair2 = calculate_fair_probability(results + ["Heads"])
        error_cost = (abs(blob_fair1 - blob_fair2) * 45 * (1-blob_fair1) * 0.75) - 1 
        print(error_cost)
    else:
        current_flip_gain = 15*(1-blob_fair1) - 30*(blob_fair1)
        blob_fair2 = calculate_fair_probability(results + ["Tails"]) 
        error_cost = (abs(blob_fair1 - blob_fair2) * 45 * blob_fair1 * 0.5) - 1  
        print(error_cost)

    if error_cost > 0:
        return "Flip again"
    elif blob_fair1 > 0.5:
        return "Fair"
    else:
        return "Cheater"


print(evaluate_flip_gain(["Heads", "Heads", "Heads", "Heads", "Heads", "Heads"]))
