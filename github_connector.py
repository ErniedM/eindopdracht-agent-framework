import git
import os
import json
import shutil

class GitHubConnector:
    def __init__(self, repository_url):
        self.repository_url = repository_url

    def check_for_updates(self):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)

            response = None
            config_file_path = os.path.join(local_directory, "config", "config.txt")
            if os.path.exists(config_file_path):
                with open(config_file_path, "r") as file:
                    response = file.read()

            repo.close()
            shutil.rmtree(local_directory)

            if response:
                return True
            else:
                return False
        except (git.exc.GitCommandError, FileNotFoundError):
            return False

    def get_config(self):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)

            config = None
            config_file_path = os.path.join(local_directory, "config", "config.txt")
            if os.path.exists(config_file_path):
                with open(config_file_path, "r") as file:
                    config = json.load(file)

            repo.close()
            shutil.rmtree(local_directory)

            return config
        except (git.exc.GitCommandError, FileNotFoundError):
            return None

    def download_module_code(self, module_name):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)

            module_file_path = os.path.join(local_directory, "modules", f"{module_name}.py")
            module_code = None
            if os.path.exists(module_file_path):
                with open(module_file_path, "r") as file:
                    module_code = file.read()

            repo.close()
            shutil.rmtree(local_directory)

            return module_code
        except (git.exc.GitCommandError, FileNotFoundError):
            return None

    def log_data(self, data):
        try:
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)

            log_file_path = os.path.join(local_directory, "logs", "log.txt")
            with open(log_file_path, "a") as file:
                file.write(str(data) + "\n")

            repo.git.add(all=True)
            repo.index.commit("Add new log entry")
            origin = repo.remote(name="origin")
            origin.push()

            repo.close()
            shutil.rmtree(local_directory)

            return True
        except (git.exc.GitCommandError, FileNotFoundError):
            return False
