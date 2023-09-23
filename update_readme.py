name: 自动更新README

on:
  schedule:
    - cron: '0 */2 * * *' # 每2小时执行一次

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: 检出仓库
        uses: actions/checkout@v2

      - name: 更新 README.md
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          echo date > runtime.txt
          git add .
          git commit -m "Update README.md and timestamp [skip ci]"
          git push

      - name: 更新时间戳
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          TZ='Asia/Shanghai' git commit --allow-empty -m "Update timestamp [skip ci]" --date="$(date +'%Y-%m-%dT%H:%M:%S%z')"
          git push
