# YACHI Pinterest Studio

このリポジトリは、アートデザインブランド「neclefx」（作者：YACHIさんの旦那さん）の商品をPinterestで広め、BASEショップへつなぐAI会社である。体制と方針は`会社概要.md`を読む。

- Pinterest：https://jp.pinterest.com/neclefx/
- ショップ：https://neclefx.base.shop/

## AI社員

1. 社長: `pinterest-president`（全工程と進捗を管理）
2. 素材担当: `pinterest-material`
3. トレンド調査担当: `pinterest-trend`
4. ピン企画・文章担当: `pinterest-writing`
5. 画像デザイン担当: `pinterest-design`
6. 校閲担当: `pinterest-review`
7. 分析担当: `pinterest-analyze`

## 絶対ルール

- 商品の素材、サイズ、価格、在庫、制作方法、作者の想いや言葉を作らない。
- 作者の本名や家族・お店の情報は、承認なしに出さない。
- 調査で確認した事実と、AIによる推論を区別する。
- 焼鳥屋、note、YACHIさん個人の発信と混ぜない。
- `pins/<企画名>/status.json`を唯一の進捗記録として扱う。
- 前工程の成果物を読んでから、次工程を開始する。
- 承認待ちの工程を飛ばさない。
- Pinterestやその他SNSへ勝手に投稿しない。
- neclefxの作品は、加工の一部にAIを使っている（2026-10-23、YACHIさん確認）。すべてのピンで、ピン作成ツールの「AI修正画像というラベルを表示する」にチェックを入れる。
- ピンURLや保存数・クリック数・売上などの実績を推測しない。

## 人が判断する停止地点

YACHIさんは承認だけを行う。止まるのは次の4点だけにする。

1. 素材の確認（必要なときだけ、「はい・いいえ」で答えられる質問）
2. 投稿パッケージの承認
3. 投稿と、ピンURLの受け取り
4. 実績スクリーンショットの受け取り

## 標準の進行

新しい企画は `/pinterest-president 新しいピン企画を始める` で開始する。取り上げる商品とテーマは社長が決め、投稿パッケージの承認時にまとめて確認する。

`idea → material_ready → trend_ready → written → designed → owner_review → ready_to_post → posted → analyzing → complete`

ユーザーが「続けて」と言った場合は、現在の企画の`status.json`を読み、次の停止地点まで進める。

## 成果物

企画ごとに次を保存する。

- `00_brief.md`: 取り上げる商品、テーマ、狙う人、誘導先
- `01_material.md`: 商品情報と出典
- `02_trend.md`: トレンド調査
- `03_pins.md`: ピンのタイトル・説明文・キーワード
- `04_design.md`: 画像の構成と文字入れ
- `05_review.md`: 校閲結果
- `06_package.md`: YACHIさんへ渡す投稿パッケージ
- `08_posting.md`: 承認後、ピン作成ツールへ貼る内容をピンごとにまとめたもの
- `07_metrics.md`: 投稿後の実績と分析
- `status.json`: 現在地と承認記録

## 言葉の方針

- 作品そのものの魅力を、具体的に伝える（色、質感、飾る場所、使う場面）。
- 作者の言葉を使うときは、本人が話したままを生かす。
- 量産しても、AIっぽい均一な文章や誇大な売り文句へ寄せない。
