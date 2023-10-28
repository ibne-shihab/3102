# the hypothesis with the most specific values
hypothesis = None
# function to check if an example is consistent with the hypothesis
def is_consistent(example, hypothesis):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != example[i]:
            return False
    return True
# Find-S algorithm
def find_s(training_data):
    global hypothesis
    for example in training_data:
        x, y = example[:-1], example[-1]
        # If it's a positive example, update the hypothesis
        if y == 'Yes':
            if hypothesis is None:
                hypothesis = list(x)
            else:
                for i in range(len(hypothesis)):
                    if x[i] != hypothesis[i]:
                        hypothesis[i] = '?'
#the training data
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Yes'],
    ['Cloudy', 'Cold', 'High', 'Weak', 'No'],
    ['Rainy', 'Cold', 'High', 'Weak', 'No']
]
# Apply algorithm
find_s(training_data)
# Print the final hypothesis
print("Final Hypothesis:", hypothesis)