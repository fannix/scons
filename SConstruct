import os
import SCons
from util import preprocess_lines
env = Environment(ENV = os.environ)

def preprocess(target, source, env):
    '''Preprocess the raw text.'''
    # Read in the data.
    with open(str(source[0]), 'r') as raw_file:
        raw_lines = raw_file.readlines()
        lines =  raw_lines[9:]
    processed = preprocess_lines(lines)
    with open(str(target[0]), 'w') as target_file:
        for line in processed:
            target_file.write(line+"\n")

# Convert the delimiter from semicolon to tab, remove whitespace.
env.Command(target='fr.txt', source='fr-raw.txt', action=preprocess)
# Better specify the dependency explicitly when using Command().
env.Depends('fr.txt', 'fr-raw.txt')

#bld = Builder(action = 'python ../text_to_vec.py -s $TARGET < $SOURCE') 
#env['BUILDERS']['Span'] = bld
#env.Span('fr.span', 'fr.txt')

span = env.Command('fr.span', 'fr.txt', 'python ../text_to_vec.py -s $TARGET < $SOURCE')
project = env.Command('fr.vec','fr.txt',
    'python ../text_to_vec.py -p fr.span -t 0 < $SOURCE > $TARGET')
env.Depends(project, span)
