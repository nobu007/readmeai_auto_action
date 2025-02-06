import os
import subprocess


# This script automates the process of translating a README.md file and creating a pull request.
#
# The script performs the following steps:
# 1. Copies the directory "/usr/src/app/readmeai_auto" to the current directory.
# 2. Checks if the README.md file has changed compared to a previous version.
# 3. If the README.md file has changed, it runs a translation script to translate the README.md file.
# 4. Configures Git settings and creates a new branch for the translated README.md files.
# 5. Adds the translated README.md files and the previous README.md file to the Git staging area.
# 6. Commits the changes with a message indicating the addition of the translated README.md files.
# 7. Pushes the changes to the remote repository and creates a pull request using the GitHub CLI.
# 8. Creates a pull request using the GitHub CLI with the translated README.md files.
#
# Environment Variables:
# - GITHUB_TOKEN: GitHub token for authentication.
# - INPUT_REPO: URL of the GitHub repository.
# - INPUT_FOLDER: Target folder to process.
# - INPUT_EXCLUDE: Comma-separated list of files or directories to exclude.
#
# Files:
# - .previous_readme.md: The previous version of the README.md file.
# - README.md: The current version of the README.md file.
# - README_EN.md: The translated README.md file in English.
# - README_JA.md: The translated README.md file in Japanese.

# 前回のREADME.mdを取得
previous_readme_path = ".previous_readme.md"
current_readme_path = "README.md"

# "/usr/src/app/readmeai_auto"をカレントディレクトリにコピー
subprocess.run(["cp", "-r", "/usr/src/app/readmeai_auto", "."], check=True)

# Exclude specified files or directories
exclude_list = os.environ.get("INPUT_EXCLUDE", "").split(",")
exclude_list = [item.strip() for item in exclude_list if item.strip()]

# Copy the target folder to the current directory
folder = os.environ.get("INPUT_FOLDER", ".")

# README.mdが変更されたかどうかをチェック
if os.path.isfile(previous_readme_path):
    # README.mdが変更されているかチェック
    if subprocess.call(["diff", "-q", current_readme_path, previous_readme_path]) != 0:
        print("README.md has changed.")
        readme_changed = True
    else:
        print("README.md has not changed.")
        readme_changed = False
else:
    print("No previous README found, treating as changed.")
    readme_changed = True

# READMEが変更されている場合のみ翻訳を実行
if readme_changed:
    # READMEを翻訳する処理
    subprocess.run(
        [
            "python",
            "readmeai_auto/readme_translator.py",
            "-l",
            "en",
            "ja",
            "--folder",
            folder,
            "--exclude",
            ",".join(exclude_list),
        ],
        check=True,
    )

    # PRを作成するための情報
    github_token = os.environ.get("GITHUB_TOKEN")
    repo_url = os.environ.get("INPUT_REPO")
    branch_name = f"translate-readme-{os.environ.get('GITHUB_RUN_NUMBER', '')}"

    # カレントディレクトリをsafe.directory設定する
    subprocess.run(
        ["git", "config", "--global", "--add", "safe.directory", os.getcwd()],
        check=True,
    )

    # コミット対象候補
    target_files = ["README_EN.md", "README_JA.md"]

    # GitHub CLIを使って新しいブランチを作成
    subprocess.run(
        ["git", "config", "--global", "user.name", "GitHub Actions"], check=True
    )
    subprocess.run(
        ["git", "config", "--global", "user.email", "actions@github.com"], check=True
    )
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)

    for target_file in target_files:
        if os.path.isfile(target_file):
            print("Adding file to git staging area: ", target_file)
            subprocess.run(["git", "add", target_file], check=True)

    # .previous_readme.mdを含める
    if os.path.isfile(previous_readme_path):
        print("Adding file to git staging area: ", previous_readme_path)
        subprocess.run(["git", "add", previous_readme_path], check=True)

    # 変更がある場合のみPRを作成
    if subprocess.call(["git", "diff", "--cached", "--quiet"]) == 0:
        # 新しいREADMEをコミット
        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                "chore: Add translated README and update previous README",
            ],
            check=True,
        )

        # 変更をリモートリポジトリにプッシュ
        subprocess.run(
            ["git", "push", "--set-upstream", "origin", branch_name], check=True
        )

        # PRを作成
        subprocess.run(
            [
                "gh",
                "pr",
                "create",
                "--base",
                "main",
                "--head",
                branch_name,
                "--title",
                "Translated README (readmeai_auto)",
                "--body",
                "This PR adds a translated version of the README and updates the previous version.",
            ],
            check=True,
        )
    else:
        print("No changes to commit. Skipping pull request creation.")
else:
    print("No changes README.md. Skipping readme_translator.")
