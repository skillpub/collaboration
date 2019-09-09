'''NASA helper logs'''

fname = 'skillpub.log'
f = open('../../logs/'+fname,'r')
s = f.readlines()
s.reverse()
data = '\n'.join(s)
f.close()

print({fname:data})
