

ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2: # raise Exception("Products cart count not matching")
    pass

assert (ItemsInCart == 0)

# try, catch block
try:
    with open("lol.txt", 'r') as reader:
        reader.read()

except Exception as e:
    print("Somehow I reached this block because there is failure in try block")
    print(e) # prints exact error from python

finally:
    print("cleaning up resources") # this block is always executed wherever except block is executed or not

    

