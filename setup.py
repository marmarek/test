import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='pkg1',
        version='1.0.0',
        packages=setuptools.find_packages(exclude=['pkg1.mod1']),
)
