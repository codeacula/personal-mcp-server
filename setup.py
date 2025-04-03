from setuptools import setup, find_packages

setup(
    name='codeaculas-personal-mcp-server',
    version='1.0.0',
    author='Codeacula',
    author_email='codeacula@codeacula.com',
    description='An MCP server that implements tasks useful for Codeacula',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi',
        'uvicorn',
        'mcp[cli]',
        'pydantic',
        'modelcontextprotocol',
        'requests==2.26.0',
        'pytest==6.2.5',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)