

def innerdiv(fun):
  def inner(a,b):
    if a<b:
      a,b=b,a
      return fun(a,b)
  return inner   

@innerdiv
def div(a,n):
  return a/n

print(div(2,4))


