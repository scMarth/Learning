import os

print('character used by the operating system to separate pathname components: {}'.format(os.sep))
workspace =  os.path.dirname(os.path.abspath(__file__))
print('workspace: {}'.format(workspace))
print(os.sep.join([workspace, 'test-directory']))
