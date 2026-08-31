# Overseas Video Translation Pipeline

## Human or catalog input

1. Select one economic or industrial topic.
2. Select three source videos with complementary roles.
3. Provide or approve one thumbnail.

When the topic already exists in the catalog, this stage needs no web search or CLI generation.

## Automated stages

```text
Topic + three URLs
  -> preserve full source videos and captions
  -> select complete evidence clips
  -> GPT-5.6 Luna A/B commentary
  -> validate timestamps and exact transcript anchors
  -> translate selected subtitle cues
  -> fixed A/B voice synthesis
  -> bilingual source renders
  -> 40-minute long-form assembly
  -> six vertical clips
  -> metadata and publish receipts
```

Source clips, transcripts, research plan, production plan, audio timeline, rendered clips, final video,
shorts and upload receipts remain in the episode directory. The queue publisher refuses `test` and
`no_upload` episodes.

## Inventory policy

- Minimum ready inventory: 3 episodes
- Target ready inventory: 6 episodes
- Normal publishing: Monday, Saturday and Sunday at noon KST
- Market-holiday fallback: consume one ready episode in the unused morning slot

The publisher is fail-closed: it only accepts `state=ready`, `publish=true`, and rejects
`upload_blocked=true`. A long form, thumbnail, description, and exactly six rendered short forms
must all exist before the episode can leave the inventory queue.
