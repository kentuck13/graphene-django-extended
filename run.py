klass = type('MyKlass', (object,), {
    'a': 1
})
print(klass().a)
