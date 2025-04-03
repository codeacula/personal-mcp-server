from setuptools import setup, find_packages

setup(
    name='mcp-server',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A minimal MCP server implementation',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
        # e.g., 'Flask>=1.1.2',
        # 'FastAPI>=0.63.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)