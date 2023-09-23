name: �Զ�����README

on:
  schedule:
    - cron: '0 */2 * * *' # ÿ2Сʱִ��һ��

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: ����ֿ�
        uses: actions/checkout@v2

      - name: ���� README.md
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          echo date > runtime.txt
          git add .
          git commit -m "Update README.md and timestamp [skip ci]"
          git push

      - name: ����ʱ���
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          TZ='Asia/Shanghai' git commit --allow-empty -m "Update timestamp [skip ci]" --date="$(date +'%Y-%m-%dT%H:%M:%S%z')"
          git push
