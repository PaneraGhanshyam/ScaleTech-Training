# Training Progress

## 2026-08-17

### What I Learned

- Set up and configured the GitHub CLI (`gh`) on Garuda Linux.
- Learned the difference between Git and GitHub CLI and when CLI-based GitHub operations are useful.
- Configured GitHub CLI authentication using a Personal Access Token (PAT).
- Learned about fine-grained Personal Access Tokens and the principle of least privilege.
- Understood the difference between fine-grained and classic PATs and restricted the training repository token to the required permissions.
- Verified GitHub SSH authentication and configured the repository to use SSH for Git operations.
- Created and organized the `ScaleTech-Training` GitHub repository.
- Learned about Git repository structure, branches, remotes, commits, and repository synchronization.
- Created a basic folder structure for Stage 1 training.
- Learned about multiple Python installations on Linux and how `PATH` determines which Python executable is used.
- Identified Python 3.14.7 and Python 3.11.16 installations on the system.
- Created an isolated Python 3.11.16 virtual environment using `venv`.
- Learned the purpose and structure of `.venv`, including `bin`, `lib`, `include`, and `pyvenv.cfg`.
- Learned how to verify the Python interpreter used by a virtual environment.
- Learned how `pip` works inside a virtual environment.
- Installed the `requests` package and observed its dependencies.
- Learned about dependency management and created `requirements.txt` using `pip freeze`.
- Configured `.gitignore` to exclude the virtual environment and company-provided training roadmap from Git.

### Tasks / Activities

- Installed and configured GitHub CLI.
- Authenticated GitHub CLI using a fine-grained PAT.
- Verified SSH authentication with GitHub.
- Created and renamed the training repository.
- Configured the Git remote using SSH.
- Created the initial Stage 1 repository structure.
- Created a Python 3.11 virtual environment.
- Activated and verified the virtual environment using Fish.
- Installed `requests` using `pip`.
- Generated `requirements.txt`.
- Started configuring `.gitignore`.

### Key Takeaways / Challenges

- Git and GitHub are related but serve different purposes: Git handles version control, while GitHub provides hosting and collaboration features.
- GitHub CLI provides command-line access to GitHub functionality, while Git itself handles version-control operations.
- SSH keys and Personal Access Tokens serve different authentication purposes and can be used together.
- Fine-grained PATs provide more restrictive repository and permission control than classic PATs.
- Virtual environments allow project dependencies to remain isolated from system-wide Python packages.
- Multiple Python versions can coexist on Linux without changing the system default Python.
- `python3.11 -m venv .venv` allows the project to explicitly use Python 3.11 instead of the system Python 3.14.
- `requirements.txt` allows project dependencies to be recorded and recreated on another system.
- Learned that Git does not track empty directories and that `.gitignore` prevents files such as `.venv` from being tracked.

### Progress / Updates

- Initial GitHub repository and local development environment are configured.
- Python 3.11.16 virtual environment is ready for the training.
- Package management and dependency tracking have been introduced.
- Python programming concepts have not been started yet; they will begin in the next training session.