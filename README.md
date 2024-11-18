# Test GitHub Actions

This project has been developed to test the GitHub Actions as part of a CI/DC workflow.

## Installation

- Clone the repo
   ``` sh
   sh git clone https://github.com/wake-ua/test-github-actions.git
   ```
- Create a virtual environment (recommended)
   ``` sh
   python3 -m venv myenv
   source myenv/bin/activate
   ```
- Install pip modules from [requirements.txt](requirements.txt)
  ``` sh
  pip install -r requirements.txt
  ```
- Run the tests
  ```sh
  pytest --cov --cov-report term-missing
  ```
  

