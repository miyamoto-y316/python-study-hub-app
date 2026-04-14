# 環境構築手順

Python仮想環境（venv）作成
```Bash
python3 -m venv .venv
```

.gitignore作成
```Bash
touch .gitignore
```

.gitignore更新
```
# 仮想環境
.venv/

# Pythonキャッシュ
__pycache__/
*.pyc

# 環境変数
.env

# OSファイル
.DS_Store
```

7. pipアップグレード
```Bash
pip install --upgrade pip
```

9. Reflexインストール
```Bash
pip install reflex
```

10. Reflexプロジェクト作成
```Bash
reflex init
```

11. 開発サーバー起動
```Bash
reflex run
```

12. ブラウザで確認
```Bash
http://localhost: 3000
```