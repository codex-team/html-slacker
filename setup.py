import sys
from setuptools import setup, find_packages
from os.path import join, dirname

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    name='html-slacker',
    packages=find_packages(),
    version='0.1.6',
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
    setup_requires=pytest_runner,
    tests_require=["pytest"],
    python_requires='>=2.5'
)
