# Pull Request Pair Practice

## What to do

1. Make sure you have [VSCode](https://code.visualstudio.com/)

2. Clone this repo

```bash
git clone https://github.com/EDGENortheastern/pull-request-pair-practice.git
```

or (with [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent))

```bash
git clone git@github.com:EDGENortheastern/pull-request-pair-practice.git
```

2. Navigate to your local project folder:

```bash
cd pull-request-pair-practice
```

3. Create a virtual environment

```bash
python3 -m venv venv
```

4. Activate the virtual environment

```bash
source venv/bin/activate
```

5. Install Pytest

```bash
pip3 install pytest
```

5. Run the tests

```bash
pytest #run tests
```

6. Choose a ticket to do (see Project linked to this repo) and a pair for pair programming

7. Do the ticket as a pair, make sure you pass the tests

8. Make a branch on your local

```bash
git checkout -b my-branch-name
```

9. Add to stageing

```bash
git add .
```

10. Commit

```bash
git commit -m "Explain your commit in present simple, e.g., Adds more tests"
```

11. Try pushing to remote

```bash
git push
```

12. Make a remote branch and push to it (`git push` will generate a suggestion):

```bash
git push --set-upstream origin main
```

13. On GitHub (this repo) find a green button on the yellow background and open a Pull Request

10. Pin some classmates to review your code

11. When got positive review - Merge!
