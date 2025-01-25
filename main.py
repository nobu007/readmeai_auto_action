import os
import subprocess

# 前回のREADME.mdを取得
previous_readme_path = ".previous_readme.md"
current_readme_path = "README.md"

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
        ]
    )

    # PRを作成するための情報
    github_token = os.environ.get("GITHUB_TOKEN")
    repo_url = os.environ.get("INPUT_REPO")
    branch_name = "translate-readme"

    # コミット対象候補
    target_files = ["README_EN.md", "README_JA.md"]

    # GitHub CLIを使って新しいブランチを作成
    subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions"])
    subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"])
    subprocess.run(["git", "checkout", "-b", branch_name])

    for target_file in target_files:
        if os.path.isfile(target_file):
            subprocess.run(["git", "add", target_file])

    # .previous_readme.mdを含める
    if os.path.isfile(previous_readme_path):
        subprocess.run(["git", "add", previous_readme_path])

    # 新しいREADMEをコミット
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            "chore: Add translated README and update previous README",
        ]
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
        ]
    )
