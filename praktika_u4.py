def get_summ(one, two, delimiter=' '):
    one = str(one)
    two = str(two)
    summ = str(f'{one}{delimiter}{two}')
    return summ
    
result = get_summ('learn', 'python')

print(result.upper())