import pytictoc
import pandas as pd

df = pd.DataFrame(data={'foo': [94.54, 92.46], 'bar': [34.21, 31.67]})

print(df)

def getfoobar(d):
    return {'foo': d.foo, 'bar': d.bar}


### Method A
print(getfoobar(d=df.loc[0]))
print(getfoobar(d=df.loc[1]))

### Method B
print({'foo': df.loc[0].foo, 'bar': df.loc[0].bar})
print({'foo': df.loc[1].foo, 'bar': df.loc[1].bar})

### Method C
for i in range(len(df)):
    print(getfoobar(d=df.loc[i]))

### Method D
[ print(getfoobar(d=df.loc[i])) for i in range(len(df))]



### Solution - or at least how to analyze this

### Method A
tickerA = pytictoc.TicToc()
tickerA.tic()
print(getfoobar(d=df.loc[0]))
print(getfoobar(d=df.loc[1]))
print(tickerA.toc())

### Method B
tickerB = pytictoc.TicToc()
tickerB.tic()
print({'foo': df.loc[0].foo, 'bar': df.loc[0].bar})
print({'foo': df.loc[1].foo, 'bar': df.loc[1].bar})
print(tickerB.tocvalue())

### Method C
tickerC = pytictoc.TicToc()
tickerC.tic()
for i in range(len(df)):
    print(getfoobar(d=df.loc[i]))
print(tickerC.tocvalue())

### Method D
tickerD = pytictoc.TicToc()
tickerD.tic()
[ print(getfoobar(d=df.loc[i])) for i in range(len(df))]
print(tickerD.tocvalue())
