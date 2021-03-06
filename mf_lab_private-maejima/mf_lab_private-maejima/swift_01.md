Title: SWIFTについて（概要編）<br>
Date: 2018-06-28 00:00<br>
Category: financial

**（内部向け）**<br>
現在参画中の金融案件で外部連携に使われている金融取引メッセージ（SWIFT）について<br>
キャッチアップする機会がありましたので何回かに分けて記事にしていきたいと思います。

## SWIFTとは

国際銀行間通信協会：Society for Worldwide Interbank Financial Telecommunication<br>
（金融メッセージ通信を国際的なネットワークにより提供する組織）

## 組織

種類：金融機関保有の協同組合　※ベルギー法人

## 背景・設立

- 1960年代の国際的な金融取引の急拡大
- 中央決済機関が存在しない為、個別のコルレス契約
- テレックス処理による負荷増大

上記の状況から、共通ネットワーク・標準化フォーマットでの<br>
コルレス・バンキング業務処理が必要となり、通信フォーマット統一が検討された。

- 1973年：設立
- 1977年：サービス開始
- 現在：200カ国以上で利用

## 金融機関ニーズ

  - 顧客：口座明細、入金通知
  - 他行：支払指図、取引確認
  - 本部：各種報告

## SWIFTフォーマットとは

銀行取引、送金指図などの送受信に使われる世界標準のファイルフォーマット。

その他の標準フォーマットとしては、ISO20022（XMLの規格）が次世代の標準とされてきている。

## SWIFTのサービス

- メッセージング・サービス
  - FINサービス
     - メッセージの送受信
     - 中核サービス、MT(Message Type)により業務
  - InterActサービス
     - メッセージ交換サービス
  - FileActサービス
     - ファイル転送サービス
  - Browseサービス
     - 顧客へポータルによる情報を提供する仕組み

- FINサービスの特徴
  - ストア＆フォワード方式
     - 送信メッセージはSWIFTシステム内のキューに蓄積され、受信側が受信可能となった時点で配信される
  - PKIに基づく安全性
     - 公開鍵暗号（PKI）を使用し、「認証」や「データの完全性」を実現している
  - CUGによるコントロール
     - CUG（クローズド・ユーザー・グループ）のルールに基づき、メッセージチェックを行う
  - フォーマットチェック機能
     - 「MT」（Message Type）と呼ばれるSWIFTメッセージ基準に準拠したメッセージとなっているか検証する
  - 否認防止機能
     - 送受信者が事後に、送受信の事実を否認できない仕組みを持っている

次回は、メッセージの構成や分類などの中身について書いていきたいと思います。