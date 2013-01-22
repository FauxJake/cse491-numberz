import fib

for n, i in zip(range(3), fib.fib()):
    
    print n,",",i

# additional questions to address:
# - what the heck do 'zip' and 'range' do, and why are they there?
#   zip takes the two series and makes associates them.
