# Setup Guide

## Create a New Directory and Initialize Python Environment

```bash
# Create a new directory for the project
mkdir playwright-automation && cd playwright-automation

# Initialize a Python virtual environment
python -m venv venv         # Create a virtual environment
source venv/bin/activate    # Activate the virtual environment on Linux/Mac
# For Windows use: .\venv\Scripts\activate

# Upgrade pip and install Playwright
pip install --upgrade pip
pip install playwright

# Install the required browsers
playwright install
npm install @playwright/test

```

## Install Playwright Extension for youre IDE

Nice to have, it would be helpful in constructing and visualizing automations

## Run automations scripts

To run an example automation script you can refer to the example.py file

```bash
python example.py

```