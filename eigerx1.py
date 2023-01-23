
def countErrors(products, productPrices, productSold, soldPrice):
    
    errors = 0
    for i in range(len(productSold)):
        index = products.index(productSold[i])
        if soldPrice[i] != productPrices[index]:
            errors += 1
    return errors


print(countErrors(
    products=['rice', 'sugar', 'wheat', 'cheese'],
    productPrices=[16.89, 56.92, 20.89, 345.99],
    productSold=['rice', 'cheese', 'cheese'],
    soldPrice=[18.99, 400.89, 9.9]
)) 
