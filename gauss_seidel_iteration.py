class GaussSeidelIteration:
    def __init__(self, values, errors):
        self.values = values
        self.errors = errors
        self.max_error = max(errors)

    def __str__(self):
        return f'values={self.values},errors={self.errors},max_error={self.max_error}'
