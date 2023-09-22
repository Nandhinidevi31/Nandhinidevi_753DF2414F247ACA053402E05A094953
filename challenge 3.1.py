def linearSearchProduct (productList, targetProduct):

   indices=[]

   for index, product in enumerate   (productList):

     if product==targetProduct:               indices.append(index)

   return indices

products=["pen", "pencil", "erasers ", "pencil", "scale ", "sharpener","pencil"]

target="pencil"

target2="inkpen"
target3="blackpen"

result=linearSearchProduct (products, target)

print (result)