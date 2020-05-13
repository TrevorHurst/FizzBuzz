Fizzbuzz = {3: 'Fizz', 5: 'Buzz'}
for i in range(1, 101):
    out = list(dict.fromkeys(Fizzbuzz[j]
               if i % j == 0 else i for j in Fizzbuzz))
    print(out[0] if len(out) < 2
          else ''.join([x for x in out if isinstance(x, str)]))