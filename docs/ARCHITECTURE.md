# Architecture

## 1. Ingest

각 뉴스 공급자를 독립 어댑터로 연결하고 원문, 시각, 출처, 티커 후보를 표준 형식으로
변환합니다.

## 2. Process

유사 뉴스를 묶고 주제별로 순서화한 뒤, 방송에 사용할 근거와 가격 snapshot을 하나의
Story Packet으로 만듭니다.

## 3. Script and validation

Story Packet만 사용해 A/B 대화를 생성합니다. 이후 코드가 가격 문장을 확정값으로
교체하고 티커·수치·방향을 검사합니다.

## 4. Media

A/B 음색을 고정해 TTS를 생성하고 차트, 지수판, 캐릭터 장면과 결합합니다. 롱폼의
주제 경계를 이용해 1분 미만 숏폼을 만듭니다.

## 5. Publish and metadata

롱폼과 각 숏폼의 실제 대본 범위에서 제목, 설명, 태그, 해시태그를 생성합니다. 게시
영수증을 저장해 중복 업로드를 막습니다.

## 설계 경계

```text
Collectors -> Normalized Items -> Story Groups -> Story Packets
          -> Dialogue Script -> Deterministic Validation
          -> TTS + Visual Assets -> Long-form
          -> Topic Clips -> Shorts / Reels
          -> Platform Metadata -> Publish Receipts
```

각 단계는 파일 산출물과 완료 영수증을 남깁니다. 따라서 음성 합성까지 끝난 상태에서
차트나 자막만 수정할 경우 전체 작업을 다시 실행하지 않고 해당 단계부터 재개할 수
있습니다.

