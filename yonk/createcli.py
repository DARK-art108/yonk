import argparse
import os

def gen_structure(name):
    os.mkdir(name)
    os.mkdir(os.path.join(name, 'data'))
    os.mkdir(os.path.join(name+'/data', "processed"))
    os.mkdir(os.path.join(name+'/data', "raw"))
    os.mkdir(os.path.join(name, 'docs'))
    os.mkdir(os.path.join(name, 'saved_models'))

    os.mkdir(os.path.join(name, 'notebooks'))
    os.close(fd=os.open(os.path.join(name+'/notebooks', 'experiments.ipynb'), os.O_CREAT))


    os.mkdir(os.path.join(name, 'tests'))
    os.close(os.open(os.path.join(name+'/tests', 'test_python.py'), os.O_CREAT))


    os.mkdir(os.path.join(name, 'src'))
    os.close(os.open(os.path.join(name+'/src', '__init__.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'config.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'data.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'encoders.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'evaluate.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'models.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'serving.py'), os.O_CREAT))
    os.close(os.open(os.path.join(name+'/src', 'train.py'), os.O_CREAT))

    with open(os.path.join(name, 'README.md'), 'w') as f:
        f.write('# {}\n\nDescription of the project.'.format(name))
    print('Project "{}" created successfully!'.format(name))

    os.close(os.open(os.path.join(name, 'requirements.txt'), os.O_CREAT))
    

