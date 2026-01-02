"""Setup configuration for raspi package."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="raspi",
    version="0.1.0",
    author="EthanThePhoenix38",
    description="Configuration basique à distance pour Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EthanThePhoenix38/raspi",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "flake8",
            "mypy",
            "pytest",
            "pytest-cov",
            "pre-commit",
            "bandit",
            "safety",
        ],
    },
)
