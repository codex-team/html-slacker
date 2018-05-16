from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='html-slacker',
    packages=find_packages(),
    version='0.1.4',
    description='Converts HTML to Slack formatted markdown',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    keywords='slack bot html convert markdown slackbot pythonbot slack html markdown',
    url='https://github.com/codex-team/html-slacker',
    author='CodeX Team',
    author_email='team@ifmo.su',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Environment :: Console',
    ],
    python_requires='>=2.5'
)
