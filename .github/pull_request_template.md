## Summary
<!-- What changed and which standards/artifacts/tools are affected? -->

## Governance checklist (`A01` / `A04`)
- [ ] Header metadata (`Version`, `Status`, `Last Updated`, `Next Review`) matches `Standards Design/Library-Index.md`
- [ ] Generated files rebuilt if sources changed (`build_tokens_css.py --check`, `build_document_master.py --check`)
- [ ] Pre-Release Gate record (`REC-A04-0xx`) added and registered in `Library-Index.md` (if releasing controlled items)
- [ ] `library-checks` CI run passes and is cited in the `REC-` record (`A04 §5.1.7`)

## Post-merge (required when `Standards Design/` changed)
- [ ] On `main`, run `python3 tools/publish_drive.py --apply` and confirm `python3 tools/publish_drive.py --dry-run --fail-on-drift` exits `0`
