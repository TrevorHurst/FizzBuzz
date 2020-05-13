Fizzbuzz = {3: 'Fizz', 5: 'Buzz'}
print('\n'.join(dict.fromkeys([str(i) if i % j != 0 else Fizzbuzz[j] for j in Fizzbuzz for i in range(1, 101)])))