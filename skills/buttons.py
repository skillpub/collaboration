'''shows the buttons'''

print({'buttons':['get all things done', 'stop the world', 'take a breath']})

choice = input('your choice?')

if len(choice) > 0: 
    print(choice + ' is great choice!')
else:
    print('not to choose is also a choice')
