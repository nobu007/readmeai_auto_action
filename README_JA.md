<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">READMEAI_AUTO_ACTION</h1></p>
<p align="center">
	<em>AI搭載のREADME翻訳：手間いらずでグローバルな展開を実現。
</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">以下のツールと技術で構築されています：</p>
<p align="center">
	<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=default&logo=dotenv&logoColor=black" alt=".ENV">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>
<br>

##  目次

- [ 概要](#-概要)
- [ 機能](#-機能)
- [ プロジェクト構成](#-プロジェクト構成)
  - [ プロジェクトインデックス](#-プロジェクトインデックス)
- [ はじめに](#-はじめに)
  - [ 前提条件](#-前提条件)
  - [ インストール](#-インストール)
  - [ 使用方法](#-使用方法)
  - [ テスト](#-テスト)
- [ プロジェクトロードマップ](#-プロジェクトロードマップ)
- [ 貢献](#-貢献)
- [ ライセンス](#-ライセンス)
- [ 謝辞](#-謝辞)

---

##  概要

readmeaiautoactionは、GitHubリポジトリの多言語README生成を自動化します。GoogleのGemini APIを使用してREADMEを複数の言語に翻訳し、ドキュメント作成を効率化し、国際的なリーチを向上させます。このGitHub Actionは、多言語ドキュメントを必要とする開発者向けのCI/CDプロセスを簡素化します。

---

##  機能

|      | 機能         | 概要       |
| :--- | :---:           | :---          |
| ⚙️  | **アーキテクチャ**  | <ul><li>異なる環境間で一貫した実行を可能にするため、`<Docker>`コンテナ化されたアーキテクチャを利用しています。`Dockerfile`を参照してください。</li><li>README翻訳のために、`<Python>` 3.12ベースのアプリケーション（`readme_translator.py`）を使用しています。</li><li>`.env`で設定されているように、言語翻訳のために`<Google Gemini API>`に依存しています。</li><li>自動デプロイのために、GitHub Actionsワークフロー（`.github/workflows`内の`dd`）を使用しています。</li></ul> |
| 🔩 | **コード品質**  | <ul><li>提供されたコンテキストでは、コード品質は明示的に評価されていません。`readme_translator.py`およびその他のPythonスクリプトのさらなる分析が必要です。</li><li>依存関係管理は、`<pip>`と`requirements.txt`を介して処理されます。</li><li>`.env`と`.env.example`の使用は、安全な構成管理の試みを示唆しています。</li><li>リンティングまたはコードスタイル強制ツールは明示的に言及されていません。</li></ul> |
| 📄 | **ドキュメント** | <ul><li>ドキュメントは複数のファイルタイプ（`yml`、`txt`、`example`、`py`）に分散しており、統合が必要であることを示しています。`primary_language`出力を参照してください。</li><li>`action.yml`は、GitHub Actionの機能を記述しています。</li><li>`Dockerfile`は、コンテナのビルドプロセスを詳しく説明しています。</li><li>`requirements.txt`は、プロジェクトの依存関係をリストしています。</li></ul> |
| 🔌 | **統合**  | <ul><li>翻訳サービスのために`<Google Gemini API>`と統合します。</li><li>コンテナ化とデプロイのために`<Docker>`を使用します。</li><li>CI/CD自動化のために`<GitHub Actions>`を活用します。</li><li>依存関係管理のために`<pip>`を使用します。</li></ul> |
| 🧩 | **モジュール性**    | <ul><li>このプロジェクトは、異なる機能（例：`readme_translator.py`、`action.yml`、`Dockerfile`）のために個別のファイルを持つモジュール式であるように見えます。</li><li>`readme_translator.py`自体のモジュール性の程度は指定されていません。</li><li>依存関係は`requirements.txt`に明確に定義されています。</li><li>モジュール性を完全に評価するには、コードベースのさらなる分析が必要です。</li></ul> |
| 🧪 | **テスト**       | <ul><li>明示的なテストフレームワークまたは戦略は言及されていません。</li><li>提供されたコンテキストには、ユニットテスト、統合テスト、またはその他のテスト方法に関する情報がありません。</li><li>`test_commands`変数はテストの可能性を示唆していますが、具体的なコマンドは提供されていません。</li><li>包括的なテストを追加することで、プロジェクトの信頼性が大幅に向上します。</li></ul> |

---

##  プロジェクト構成

```sh
└── readmeai_auto_action/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── action.yml
    └── readmeai_auto
        ├── .env
        ├── .env.example
        ├── .gitignore
        ├── LICENSE
        ├── README.md
        ├── README_DE.md
        ├── README_EN.md
        ├── README_ES.md
        ├── README_FR.md
        ├── README_JA.md
        ├── README_KO.md
        ├── README_RU.md
        ├── README_ZH.md
        ├── readme_translator.py
        └── requirements.txt
```

###  プロジェクトインデックス
<details open>
	<summary><b><code>READMEAI_AUTO_ACTION/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/action.yml'>action.yml</a></b></td>
				<td>- `action.yml`ファイルは、GitHub Actionを定義します<br>- これは、指定されたリポジトリの多言語でのREADME生成を自動化します<br>- このアクションは、リポジトリURLとターゲット言語を入力として受け取り、オプションでファイルまたはディレクトリの除外を許可します<br>- 実行にはカスタムDockerイメージを利用します<br>- このアクションは、プロジェクトのCI/CDパイプライン内の異なる言語間でのドキュメント作成を効率化します。</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Dockerfileは、README翻訳アプリケーションのランタイム環境を構築します<br>- Python 3.12ベースイメージを活用し、`readmeai_auto`リポジトリをクローンし、依存関係をインストールし、Pythonスクリプト（`readme_translator.py`）を実行して、英語と日本語の間でREADMEを翻訳します<br>- 結果のコンテナは、README翻訳プロセスを自動化します。</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- readmeai_auto Submodule -->
		<summary><b>readmeai_auto</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/readmeai_auto/requirements.txt'>requirements.txt</a></b></td>
				<td>- `requirements.txt`は、プロジェクトの外部依存関係を指定します<br>- これにより、`readmeai_auto`アプリケーションがGoogle Generative AI APIにアクセスし、`python-dotenv`によって管理される環境変数を利用できるようになります<br>- これらの依存関係は、アプリケーションの中核機能に不可欠であり、Googleの大規模言語モデルとのインタラクションを可能にします。</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/readmeai_auto/.env'>.env</a></b></td>
				<td>- `.env`ファイルは、Gemini APIキーを保存し、readmeai_autoアプリケーションの認証資格情報を提供します<br>- これにより、Gemini APIとのインタラクションが容易になり、アプリケーションがGeminiの機能を活用できるようになります<br>- このキーは、アプリケーションの中核的な操作に不可欠であり、外部サービスへの安全なアクセスを確保します<br>- その存在は、システム全体の機能に不可欠です。</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/readmeai_auto/.env.example'>.env.example</a></b></td>
				<td>- `.env.example`ファイルは、環境変数のテンプレートを提供します<br>- これは、特にGemini APIキーを設定し、readmeai_autoプロジェクトのGemini APIとのインタラクションに不可欠です<br>- これにより、機密性の高い資格情報の安全な保存が保証され、セキュリティと保守性の向上のためにメインコードベースから分離されます<br>- このファイルの目的は、Geminiサービスとのシームレスな統合を容易にすることです。</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/readmeai_auto/readme_translator.py'>readme_translator.py</a></b></td>
				<td>- `readme_translator.py`スクリプトは、READMEファイルの翻訳を自動化します<br>- これは、Gemini APIを活用して、ソースREADMEを複数の言語に翻訳し、Markdownフォーマットと技術的な正確性を維持します<br>- このスクリプトは、入力ファイルとターゲット言語を指定するためのコマンドラインインターフェースを提供し、定義済みの言語セットをサポートします<br>- 翻訳されたREADMEは新しいファイルとして保存されます。</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='/home/jinno/git/readmeai_auto_action/blob/master/.github/workflows/dd'>dd</a></b></td>
						<td>- ワークフロースクリプトは、デプロイを自動化します<br>- これは、プロジェクトの継続的インテグレーション/継続的デプロイメント（CI/CD）パイプラインの重要なコンポーネントであり、シームレスで自動化されたリリースを保証します<br>- このスクリプトは、ビルド、テスト、およびデプロイプロセスを管理し、ソフトウェア配信ライフサイクルを効率化し、効率を向上させます<br>- 広範なプロジェクト構造内での統合は、信頼性と一貫性のあるデプロイを促進します。</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  はじめに

###  前提条件

readmeaiauto_actionを始める前に、ランタイム環境が次の要件を満たしていることを確認してください。

- **プログラミング言語：** エラー検出 primary_language: {'yml': 1, 'txt': 1, 'example': 1, 'py': 1}
- **パッケージマネージャ：** Pip
- **コンテナランタイム：** Docker

###  インストール

次のいずれかの方法を使用して、readmeaiauto_actionをインストールします。

**ソースからビルド：**

1. readmeai_auto_actionリポジトリをクローンします。
```sh
❯ git clone ../readmeai_auto_action
```

2. プロジェクトディレクトリに移動します。
```sh
❯ cd readmeai_auto_action
```

3. プロジェクトの依存関係をインストールします。


**`pip`の使用** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```


**`docker`の使用** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t git/readmeai_auto_action .
```

###  使用方法
次のコマンドを使用してreadmeaiauto_actionを実行します。
**`pip`の使用** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


**`docker`の使用** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  テスト
次のコマンドを使用してテストスイートを実行します。
**`pip`の使用** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```

---
##  プロジェクトロードマップ

- [X] **`タスク 1`**: <strike>機能1を実装する。</strike>
- [ ] **`タスク 2`**: 機能2を実装する。
- [ ] **`タスク 3`**: 機能3を実装する。

---

##  貢献

- **💬 [ディスカッションに参加](https://LOCAL/git/readmeai_auto_action/discussions)**：洞察を共有したり、フィードバックを提供したり、質問したりできます。
- **🐛 [問題を報告](https://LOCAL/git/readmeai_auto_action/issues)**：`readmeai_auto_action`プロジェクトで見つかったバグを提出するか、機能リクエストを記録します。
- **💡 [プルリクエストを送信](https://LOCAL/git/readmeai_auto_action/blob/main/CONTRIBUTING.md)**：オープンなPRを確認し、独自のPRを送信してください。

<details closed>
<summary>貢献ガイドライン</summary>

1. **リポジトリをフォークする**: プロジェクトリポジトリをLOCALアカウントにフォークすることから始めます。
2. **ローカルにクローン**: Gitクライアントを使用して、フォークしたリポジトリをローカルマシンにクローンします。
   ```sh
   git clone /home/jinno/git/readmeai_auto_action
   ```
3. **新しいブランチを作成**: 常に新しいブランチで作業し、わかりやすい名前を付けます。
   ```sh
   git checkout -b new-feature-x
   ```
4. **変更を加える**: ローカルで変更を開発およびテストします。
5. **変更をコミット**: 更新内容を説明する明確なメッセージでコミットします。
   ```sh
   git commit -m '新しい機能xを実装しました。'
   ```
6. **LOCALにプッシュ**: 変更をフォークしたリポジトリにプッシュします。
   ```sh
   git push origin new-feature-x
   ```
7. **プルリクエストを送信**: 元のプロジェクトリポジトリに対してPRを作成します。変更点とその動機を明確に説明します。
8. **レビュー**: PRがレビューされ承認されると、メインブランチにマージされます。ご貢献おめでとうございます！
</details>

<details closed>
<summary>コントリビューターグラフ</summary>
<br>
<p align="left">
   <a href="https://LOCAL{/git/readmeai_auto_action/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=git/readmeai_auto_action">
   </a>
</p>
</details>

---

##  ライセンス

このプロジェクトは、[SELECT-A-LICENSE](https://choosealicense.com/licenses)ライセンスの下で保護されています。詳細については、[LICENSE](https://choosealicense.com/licenses/)ファイルを参照してください。

---

##  謝辞

- ここに、リソース、コントリビューター、インスピレーションなどをリストしてください。

---
