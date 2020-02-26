# Guidelines for contributing

## Table of Contents <!-- omit in toc -->

- [Git](#git)
  - [Get started with Git and GitHub](#get-started-with-git-and-github)
  - [Set up SSH](#set-up-ssh)
  - [Clone or fork the repository](#clone-or-fork-the-repository)
  - [Branch](#branch)
  - [Commit](#commit)
  - [Push](#push)
  - [Pull](#pull)
  - [Git pre commit hooks](#git-pre-commit-hooks)
- [Markdown](#markdown)
- [Python](#python)
  - [VSCode](#vscode)
  - [Python virtual environment tools](#python-virtual-environment-tools)
  - [Python code style](#python-code-style)
- [Docker](#docker)
  - [Docker background](#docker-background)
  - [Pipenv and Docker](#pipenv-and-docker)

## Git

### Get started with Git and GitHub

- Sign up for [GitHub](https://github.com) if you haven't already.
- Install Git
  - Mac:
    - Install [Homebrew](https://brew.sh/).
    - Install Git via Homebrew on the command line: `brew install git`
  - See the [Git Downloads page](https://git-scm.com/downloads) for more options.
  - _Why use Git?_ It allows for maintenance of separate sets of the same code (branches), each with the ability to track and undo changes in high detail.
- The [GitHub Desktop](https://desktop.github.com/) git client provides a user interface that can make Git easier.
- Install Git extensions for your text editor:
  - [Atom](https://atom.io/): [Git and GitHub support](https://github.atom.io/) built-in.
  - [Sublime Text](http://www.sublimetext.com/): [GitSavvy](https://packagecontrol.io/packages/GitSavvy)
  - [vscode](https://code.visualstudio.com/): [Git support](https://code.visualstudio.com/Docs/editor/versioncontrol) built in.
- Git and GitHub resources:
  - [Git docs](https://git-scm.com/)

### Set up SSH

#### Configure Git to connect to GitHub with SSH

[Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/) allows your computer to send information to GitHub over an SSH connection, so you can push changes without having to provide your username and password every time. These steps should only need to be performed once. These steps will allow your computer to connect to GitHub with SSH, and should only need to be performed once for each machine.

- Ensure user name and email are set locally in Git as described in [Configuration](#configuration).
- [Generate an SSH key and add it to the SSH agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

  ```sh
  $ touch ~/.ssh/config
  $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  $ eval "$(ssh-agent -s)"
  $ ssh-add -K ~/.ssh/id_rsa
  ```

  - The config file may need to be manually created with `touch ~/.ssh/config` first.

- [Add SSH key to GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

  ```sh
  $ pbcopy < ~/.ssh/id_rsa.pub
  ```

  - Go to GitHub and paste the key.

- [Check SSH connection](https://help.github.com/articles/testing-your-ssh-connection/)

  ```sh
  $ ssh -T git@github.com
  ```

  - Verify it looks similar to the link above, type `yes`, verify username.
  - The above steps should only need to be done once.

#### Configure repositories to connect to GitHub with SSH

- In addition to setting up your account globally to use SSH, each new repository will need to be configured to push with SSH instead of HTTPS:

  ```sh
  $ cd path/to/repo
  $ git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
  ```

- Git remotes can be viewed with `git remote -v`.
- Make a commit described in [commit](#commit).
- Push the commit as described in [push](#push).
- BOOM! That should work! You should see the push reflected on GitHub.

### Clone or fork the repository

- A **clone** is a copy of a repository on your computer.

  - [GitHub Desktop can be used to clone](https://help.github.com/desktop/guides/getting-started-with-github-desktop/).
  - If cloning from the command line:

    ```sh
    cd path/where/you/want/the/repo
    git clone git@github.com:br3ndonland/template-python.git
    ```

- A **[fork](https://help.github.com/articles/fork-a-repo/)** duplicates the project into the user's GitHub account, and still maintains connection to the original master. Forks can also be cloned.
- If you are not a repository owner, you will not be able to push to the original repository after cloning. Fork the repository on GitHub instead of directly cloning. Changes to forks can be merged into the `upstream master` with pull requests.

### Branch

- **We're currently working directly on the `master` branch.**
- More complex projects frequently use two long-running branches, `master` and `dev`.

  - Commits to `master` and `dev` are usually merge commits from feature branches.
  - Changes are made on temporary feature branches and merged into `dev` with [pull requests](#pull-requests). Guidelines for feature branches:

    - Use a clear, descriptive name for your branch.
    - Prefix the branch name with your initials to indicate that it should be unshared. Other contributors will not add commits to the branch.
    - Command line option: The `checkout -b` command creates a branch and switches to the new branch.

      ```sh
      git checkout -b featurebranchname
      ```

- Pull with rebase to keep branches and forks in sync. Bring in changes from GitHub with `git pull --rebase origin branchname`. This provides a nice linear commit history without unnecessary merge commits.

### Commit

After saving files, changes need to be committed to the Git repository.

- GitHub Desktop provides a user interface to make this easy.
- Command line commits: Simply writing `git commit` instead of `git commit -m "message"` opens the text editor.

  ```sh
  git add --all
  git commit
  ```

#### Best practices for commits

**Make meaningful, cohesive, focused commits.** Commit when an objective has been completed, or before a major change is made. Break changes up into topics so the maintainer can easily accept or reject changes from a pull request.

**Include a commit message.** See [How to make a Git commit message](https://chris.beams.io/posts/git-commit/).

1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
   > A properly formed Git commit subject line should always be able to complete the following sentence: If applied, this commit will _[your subject line here]_
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

   ```text
   Imperative commit title limited to 50 characters
   # Blank line
   - More detailed commit message body
   - List of key points and updates that the commit provides
   - Lines need to be manually wrapped at 72 characters
   ```

### Push

- Changes from forks can be incorporated into the `upstream master` (the original repository) with [pull requests](https://help.github.com/articles/about-pull-requests/). A pull request asks the owner of the master repository to merge changes from the requester's branch or fork to the master repository.
  - Select "New pull request" on the master repository's GitHub page.
  - If you forked the repository, select "Compare across forks." The base fork is the location in the master repository where the changes will go. The head fork is your fork where the changes are located.

### Pull

- Local repositories and forks can be kept in sync with upstream repositories by pulling with rebase. Run `git pull --rebase upstream master`. This keeps the commit history in line with upstream. See the [thoughtbot keeping a GitHub fork updated](https://robots.thoughtbot.com/keeping-a-github-fork-updated) article for a simple explanation.
- Pulls can also be made with merge commits. See the [GitHub Syncing a Fork article](https://help.github.com/articles/syncing-a-fork/). This will allow more separation between local and upstream changes, but will add merge commits. The commit history will diverge from upstream.
- We don't have a specific policy on pulling with rebase vs. merge commits at this time.

#### Best practices for pull requests

- **Submit pull requests for review.** Pull request reviews help improve code. Reviews should be cordial, constructive, and conducted according to the Code of Conduct.
- **Create pull requests from focused feature branches.**
- **Provide a descriptive pull request message.**
  - Use the provided pull request template.
  - List changes with bullet points.
  - Reference other pull requests that may be superseded by this request.

### Git pre commit hooks

- Git pre-commit hooks are managed with [pre-commit](https://pre-commit.com/).
- Included hooks:
  - [Black](https://black.readthedocs.io/en/stable/version_control_integration.html) (see [Python code style](#python-code-style))
  - [Flake8 Python linting](https://flake8.pycqa.org/en/latest/user/using-hooks.html) (see [Python code style](#python-code-style))
  - [mypy static type checking](https://github.com/pre-commit/mirrors-mypy)
  - [Prettier](https://prettier.io/docs/en/precommit.html) (see [Markdown](#markdown))
  - [Check for added large files](https://github.com/pre-commit/pre-commit-hooks): Useful to avoid committing large files from [Git LFS](https://git-lfs.github.com/) to the Git repo.
- After cloning the repository, install the pre-commit hooks using either your system installation of pre-commit, or the pre-commit included with the Python virtual environment.

  ```sh
  ❯ cd path/to/repo
  # System option
  ❯ pre-commit install
  # Pipenv option
  ❯ pipenv install --dev
  ❯ pipenv shell
  template-python-hash ❯ pre-commit install
  ```

- [pre-commit.yml](.github/workflows/pre-commit.yml) is a [GitHub Actions](https://github.com/features/actions) workflow that runs pre-commit with each pull request or push to the master branch.
  - [GitHub Help: actions](https://help.github.com/en/actions)
  - [GitHub actions marketplace: pre-commit](https://github.com/marketplace/actions/pre-commit)
  - [GitHub repo: pre-commit/action](https://github.com/pre-commit/action)

## Markdown

- Markdown was written with the [Markdown All in One VSCode extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), and autoformatted with [Prettier](https://prettier.io/) using the [Prettier VSCode extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

## Python

### VSCode

- [Microsoft Visual Studio Code](https://code.visualstudio.com/) (VSCode) is a cross-platform open-source text editor with powerful Python features.
- Helpful VSCode resources:
  - [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
  - [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
  - [Editing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/editing)

### Python virtual environment tools

#### `venv`

Python 3 is bundled with the [`venv` module](https://docs.python.org/3/tutorial/venv.html) for creation of virtual environments.

1. **Install and activate Python virtual environment**: The shell commands in the code block below will create a Python virtual environment, activate the virtual environment and display a modified virtual environment prompt
2. **Install required Python modules into the virtual environment**: Use `pip` to install required modules listed in _requirements.txt_. The modules will be installed locally within the virtual environment. The _requirements.txt_ file was generated by running `pip freeze > requirements.txt`.
3. **Start application**: Use the appropriate command to start your application within the virtual environment. For Flask, this is usually `python app.py` or `python -m flask run`.

```sh
~
❯ cd path/to/repo

# 1. install and activate virtual env
~/path/to/repo
❯ python3 -m venv venv
~/path/to/repo
❯ . venv/bin/activate

# 2. install modules
~/path/to/repo
(venv) path ❯ pip install -r requirements.txt

# 3. run app: the example below works for Flask
~/path/to/repo
(venv) path ❯ python app.py
```

#### Pipenv

- **[Pipenv](https://pipenv.readthedocs.io/en/latest/)** was used to manage the development virtual environment for this project.

  - Install Pipenv with a system package manager like [Homebrew](https://brew.sh/), or with the Python package manager `pip`.
  - Use Pipenv to install the virtual environment from the _Pipfile_ with `pipenv install --dev`.

    - The `--dev` flag was used to accommodate pre-release packages such as the Black autoformatter (see [code style](#python-code-style) below).
    - When generating the initial _Pipfile_ containing the Black dev package, the `--pre` flag added a line to the _Pipfile_ to allow pre-release packages. (TOML format):

      ```toml
      [pipenv]
      allow_prereleases = true
      ```

    - Further information can be found in the [Pipenv docs](https://pipenv.readthedocs.io/en/latest/basics/#specifying-versions-of-a-package).

  - Activate the virtual environment with `pipenv shell`.

- VSCode can be configured to recognize the Pipenv virtual environment. See [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).
  - _Command Palette -> Python: Select Interpreter_. Select virtual environment.
  - _Command Palette -> Python: Create Terminal_. Creates a terminal and automatically activates the virtual environment. If the virtual environment is set as the interpreter for the workspace, new terminal windows will automatically start in the virtual environment.
- **The future of Pipenv is unclear.** It went all of 2019 without a major release, and has many bugs. Jacob Kaplan-Moss (Django co-creator) has commented on how "the lead of Pipenv was someone with a history of not treating his collaborators well," and on the "bugs and rapid API changes" of Pipenv. Many developers are switching to [Poetry](https://python-poetry.org).
  - [Jacob Kaplan-Moss | Blog 20191111: My Python development environment, 2020 edition](https://jacobian.org/2019/nov/11/python-environment-2020/)
  - [Telnyx | 20200124 Nick Timkovich: RIP Pipenv](https://medium.com/telnyx-engineering/rip-pipenv-tried-too-hard-do-what-you-need-with-pip-tools-d500edc161d4)

#### Poetry

### Python code style

- Python 3 (modern Python) was used. Python 2 (legacy Python) is nearing its [end of life](https://pythonclock.org/).
- Python code was linted with [Flake8](https://flake8.readthedocs.io/en/latest/) and autoformatted with [Black](https://black.readthedocs.io/en/stable/).
- Black is still considered a pre-release. As described in [Pipenv](#pipenv), the `--dev` and `--pre` flags are needed to install Black within a Pipenv.
- Git pre-commit hooks have been installed for the [Black autoformatter](https://black.readthedocs.io/en/stable/version_control_integration.html) and [Flake8 linter](https://flake8.pycqa.org/en/latest/user/using-hooks.html).
- Within Python modules, `import` statements are organized alphabetically, and followed by `from` statements, which are also in alphabetical order.
- In general, a [Pythonic](https://docs.python-guide.org/writing/style/) code style following the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) was used. [Foolish consistency](https://pep8.org) was avoided.

## Docker

### Docker background

- **[Docker](https://www.docker.com/)** is a technology for running lightweight virtual machines called **containers**.
  - An **image** is the executable set of files read by Docker.
  - A **container** is a running image.
  - The **[Dockerfile](https://docs.docker.com/engine/reference/builder/)** tells Docker how to build the container.
- VSCode has built-in Docker features. See [Working with Docker in VSCode](https://code.visualstudio.com/docs/azure/docker) and the [VSCode tutorial on deploying Python with Docker](https://code.visualstudio.com/docs/python/tutorial-deploy-containers).
- To install Docker tools locally:
  - Ubuntu Linux: follow the [instructions for Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/), making sure to follow the [postinstallation steps](https://docs.docker.com/install/linux/linux-postinstall/) to activate the Docker daemon.
  - macOS and Windows: install [Docker Desktop](https://www.docker.com/products/docker-desktop) (available via [Homebrew](https://brew.sh) with `brew cask install docker`).
- To build this Docker image and run the container:

  ```sh
  ~
  ❯ cd path/to/repo
  ~/path/to/repo
  ❯ docker build . -t template-python:latest
  ~/path/to/repo
  ❯ docker run -d -p 80:80 template-python:latest
  ```

  - `-t` web tells Docker to name the image `template-python`. Adding `.` builds from the current directory.
  - `-d` runs the container in detached mode. Docker will display the container hash and return the terminal prompt.
  - `-p 80:80` maps the http port 80 from your local machine to port 80 in the container.
  - A tag can be specified with `name:tag`, otherwise, the tag `latest` will be used.

- <details><summary>Expand this details element for more <a href="https://docs.docker.com/engine/reference/commandline/cli/">useful Docker commands</a>.</summary>

  ```sh
  # Log in with Docker Hub credentials to pull images
  docker login
  # List images
  docker image ls
  # List containers
  docker container ls
  # Inspect a container (web in this example) and return the IP Address
  docker inspect web | grep IPAddress
  # Stop a container
  docker container stop # container hash
  # Remove a downloaded image
  docker image rm # image hash or name
  # Remove a container
  docker container rm # container hash
  # Prune images
  docker image prune
  # Prune stopped containers (completely wipes them and resets their state)
  docker container prune
  # Connect to running container (sort of like SSH)
  docker ps # get ID/hash of container you want to connect to
  docker exec -it [ID] /bin/bash
  # Or, connect as root:
  docker exec -u 0 -it [ID] /bin/bash
  # Copy file to/from container:
  docker cp [container_name]:/path/to/file destination.file
  ```

  </summary>

### Pipenv and Docker

- There are a few [adjustments](https://stackoverflow.com/a/49705601) needed to enable Pipenv and Docker to work together.
- Pipenv must first be installed with `pip`.
- Python dependencies are then installed from _Pipfile.lock_.

  - Docker containers don't need virtual environments, so the `--system` flag is used to install packages into the container's global Python installation. Thus, it is not necessary to enter the virtual environment with `pipenv shell` before starting the application.
  - The `--deploy` flag causes the build to fail if the _Pipfile.lock_ is out of date.
  - The `--ignore-pipfile` flag tells Pipenv to use the _Pipfile.lock_ for installation instead of the _Pipfile_.

  ```dockerfile
  # Pull an image: alpine images are tightly controlled and small in size
  FROM python:3.7-alpine
  LABEL app=template-python
  WORKDIR /app
  # Copy the directory to /app in the container
  COPY . /app
  # Install Pipenv
  RUN python -m pip install pipenv
  # Install packages from Pipfile.lock, configured for Docker deployments
  RUN pipenv install --system --deploy --ignore-pipfile
  # Run the application
  CMD ["python", "app.py"]
  ```
